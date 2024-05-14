#$ pip install google-generativeai
#$ pip install dash

import dash
from dash import dcc, html, callback_context
from dash.dependencies import Input, Output, State
import google.generativeai as genai
import pandas as pd
from datetime import datetime
import requests
from urllib.parse import quote_plus

# Initialize Dash app
app = dash.Dash(__name__)

genai.configure(api_key="AIzaSyDlzbJO6zS8lSSycVF-9HViolElQVENYJQ")

# Set up the model
generation_config = {
    "temperature": 0.45,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# เปิดไฟล์ .txt เพื่ออ่านข้อความ
with open('system_instruction.txt', 'r', encoding='utf-8') as file:
    system_instruction = file.read()

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=system_instruction,
    safety_settings=safety_settings
)

# Function to perform Google search
def google_search(query):
    api_key = 'AIzaSyAxdaQude_KwEpa-RzWOD7BTh0jbjbSO6g'
    search_engine_id = '1373717699f114c7e'
    encoded_query = quote_plus(query)
    url = f'https://www.googleapis.com/customsearch/v1?q={encoded_query}&key={api_key}&cx={search_engine_id}'
    response = requests.get(url)
    data = response.json()
    # Extract relevant information from the response
    search_results = data.get('items', [])
    formatted_results = []
    for result in search_results:
        title = result.get('title')
        link = result.get('link')
        formatted_results.append({'title': title, 'link': link})
    return formatted_results

# Define app layout
app.layout = html.Div([
    html.Div([
        html.Img(src='https://raw.githubusercontent.com/Naswinda/Projects/dads5001/Pics_Chat/LOGOO.png', style={'height': '80px', 'width': 'auto'}),
        html.H1("GSAS Chat 2024", style={'margin': '10px 0', 'color': '#FFFFFF', 'background-color': '#233858', 'padding': '10px'})
    ], style={'text-align': 'center', 'margin-bottom': '20px', 'background-color': '#233858'}),
    html.Div(id='chat-container', style={'height': '340px', 'overflow-y': 'scroll', 'border': '1px solid #ccc', 'border-radius': '5px', 'padding': '10px', 'background-color': '#FFFFFF'}),
    html.Div([
        dcc.Input(
            id='user-input',
            type='text',
            placeholder='Enter your message...',
            style={'width': 'calc(80% - 40px)', 'display': 'inline-block', 'border': '1px solid #ccc', 'border-radius': '5px', 'padding': '10px', 'margin-top': '10px', 'font-size': '16px'},
            debounce=True,
        ),
        html.Button('Submit', id='submit-button', n_clicks=0,
                    style={'height': '40px', 'display': 'inline-block', 'marginLeft': '10px', 'font-weight': 'bold'}),
        html.Button('Gsearch', id='search-button', n_clicks=0,
                    style={'height': '40px', 'display': 'inline-block', 'marginLeft': '10px', 'font-weight': 'bold'}),
        html.Button('End Conversation', id='end-conversation-button', n_clicks=0,
                    style={'height': '40px', 'display': 'inline-block', 'marginLeft': '10px', 'font-weight': 'bold'})
    ]),
    dcc.Loading(
    id="loading-output",
    type="default",
    children=html.Div(id="loading-output-1", style={"color": "#FF6347"}),
    style={"position": "fixed", "top": "50%", "left": "50%", "transform": "translate(-50%, -50%)"}
    ),
    dcc.Store(id='session-chat', storage_type='memory', data=[]),
], style={'padding': '20px', 'background-color': '#FF7F50'})

# Define callback to generate response and update display
@app.callback(
    [Output('chat-container', 'children'),
    Output('session-chat', 'data'),
    Output("loading-output", "children")],
    [Input('submit-button', 'n_clicks'),
     Input('end-conversation-button', 'n_clicks'),
     Input('search-button', 'n_clicks')],
    [State('user-input', 'value'),
     State('session-chat', 'data')]
)
def generate_response(submit_clicks, end_clicks, search_clicks, convo, chat_history):
    ctx = callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'end-conversation-button':
            df = pd.DataFrame(chat_history)
            df.to_excel('chat_log.xlsx', index=False)         
            chat_history.clear()
            return [], chat_history, None  # เคลียร์หน้าการค้นหาเมื่อกดปุ่ม 'End Conversation'
        elif button_id == 'search-button':
            # Perform Google search and display results
            search_results = google_search(convo)
            search_bubbles = []
            for result in search_results:
                search_bubble = html.Div([
                    html.A(result['title'], href=result['link'], target='_blank', style={'color': 'green', 'text-decoration': 'underline'}),
                    html.P(result['link'], style={'color': '#999999'})
                ], style={'marginBottom': '10px'})
                search_bubbles.append(search_bubble)
            chat_history.append({'user': convo, 'user_timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'bot': search_bubbles, 'bot_timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            return search_bubbles, chat_history, None

    if submit_clicks > 0 and convo:
        # Append user input with timestamp to chat history
        user_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_message = f"{convo}"

        # Generate response using Gemini AI model
        response = model.generate_content(convo)

        # Append bot response with timestamp to chat history
        bot_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bot_message = f"{response.text}"

        chat_history.append({'user': user_message, 'user_timestamp': user_timestamp, 'bot': bot_message, 'bot_timestamp': bot_timestamp})

        # Create chat bubbles for display
        chat_bubbles = []
        for entry in chat_history:
            chat_bubble_user = html.Div([
                html.Div(entry['user'], style={'text-align': 'right', 'color': 'blue', 'margin-bottom': '10px'}),
                html.Div(entry['user_timestamp'], style={'textAlign': 'right', 'color': '#999999', 'fontSize': '12px'}),
                ], style={'backgroundColor': '#F4F4F4', 'padding': '10px', 'marginBottom': '10px', 'borderRadius': '10px'})
            chat_bubble_bot = html.Div([
                html.Div(entry['bot'], style={'text-align': 'left', 'color': 'green', 'margin-bottom': '10px'}),
                html.Div(entry['bot_timestamp'], style={'textAlign': 'left', 'color': '#999999', 'fontSize': '12px'}),
                ], style={'backgroundColor': '#F4F4F4', 'padding': '10px', 'marginBottom': '10px', 'borderRadius': '10px'})
            chat_bubbles.extend([chat_bubble_user, chat_bubble_bot])
        
        return chat_bubbles, chat_history, None
    else:
        return [], chat_history, None


# Callback to submit form on pressing Enter
@app.callback(
    Output('submit-button', 'n_clicks'),
    [Input('user-input', 'n_submit')],
    [State('submit-button', 'n_clicks')]
)
def submit_on_enter(n_submit, n_clicks):
    return n_clicks + 1 if n_submit else n_clicks

# Callback to clear input after submitting
@app.callback(
    Output('user-input', 'value'),
    [Input('submit-button', 'n_clicks'),
     Input('search-button', 'n_clicks')],
    [State('user-input', 'value')]
)
def clear_input(n_clicks_submit, n_clicks_search, input_value):
    ctx = callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'submit-button' or button_id == 'search-button':
            return ''
    return input_value


if __name__ == '__main__':
    app.run_server(debug=False)
