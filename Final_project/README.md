<div align="center">
  <h1>CHATBOT Dash with Gemini and Google Search</h1>
</div>


# Image Album
<div align="center">
  <img src="https://github.com/Anonsuksak/DADS5001_tool/assets/148941448/eabfa338-cb27-4e71-beaf-74cad9910f84" alt="Screen Shot 2567-05-14 at 12 13 04" width="200"/>
  <img src="https://github.com/Anonsuksak/DADS5001_tool/assets/148941448/0a13bc36-ac2a-4d0a-9df0-f26cf7c0911f" alt="Screen Shot 2567-05-14 at 12 16 03" width="200"/>
  <img src="https://github.com/Anonsuksak/DADS5001_tool/assets/148941448/180af5d4-294e-4ef5-b983-978413efe05a" alt="Screen Shot 2567-05-14 at 12 40 30" width="200"/>
</div>

# Instruction
1. To utilize Gemini AI, install the following libraries using the command.
```sh
pip install google-generativeai
pip install dash
```
2. Git clone or download "app.py" and "system_instruction.txt" to your computer.
```sh
git clone https://github.com/Anonsuksak/DADS5001_tool/Final_project.git
```
3. Edit app.py by using your Gemini and Google search API keys and search engine ID using the steps below:
<br><br>
3.1 You can get "YOUR API KEY" by using Google AI Studio
```sh
genai.configure(api_key="YOUR API KEY")
```

```sh
def google_search(query):
    api_key = 'YOUR API KEY'
    search_engine_id = 'YOUR SEARCH ENGINE ID'
```
You can get "YOUR API KEY" by using Custom Search JSON API 
<img width="635" alt="Screen Shot 2567-05-14 at 13 32 57" src="https://github.com/Anonsuksak/DADS5001_tool/assets/148941448/ef7a045e-bc04-43ae-8525-6cd138d2889d">

and "YOUR SEARCH ENGINE ID" by using Programmable Search Engine(free edition) by Google

5. Run it in the terminal or Run without Debugging, preferably using VS Code 
```sh
python app.py
```

<br><br>
You can view our presentation by scanning the QR code below:

<img width="263" alt="Screen Shot 2567-05-14 at 12 22 48" src="https://github.com/Anonsuksak/DADS5001_tool/assets/148941448/4e99cf4d-5f6f-4546-b52d-f5886e5e720b">
