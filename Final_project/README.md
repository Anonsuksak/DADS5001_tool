<div align="center">
  <h1>Thai Chatbot Dash with Gemini and Google Search</h1>
</div>

# Team Members<br>
6610412005 Nawinda Amadtohed<br>
6610412009 Anon Suksak<br>
6610412010 Satakun Termthaimongkong<br>

# GSAS Chat 2024 interface
<div align="center">
  <img src="https://github.com/Anonsuksak/DADS5001_tool/assets/148941448/eabfa338-cb27-4e71-beaf-74cad9910f84" alt="Screen Shot 2567-05-14 at 12 13 04" width="200"/>
  <img src="https://github.com/Anonsuksak/DADS5001_tool/assets/148941448/0a13bc36-ac2a-4d0a-9df0-f26cf7c0911f" alt="Screen Shot 2567-05-14 at 12 16 03" width="200"/>
  <img src="https://github.com/Anonsuksak/DADS5001_tool/assets/148941448/180af5d4-294e-4ef5-b983-978413efe05a" alt="Screen Shot 2567-05-14 at 12 40 30" width="200"/>
</div>

# Example of usage video
https://github.com/Anonsuksak/DADS5001_tool/assets/148941448/2e73c4d9-c6f1-4c36-81a3-c8f9d9658784


# Workflow
<img width="782" alt="Screen Shot 2567-05-14 at 14 09 55" src="https://github.com/Anonsuksak/DADS5001_tool/assets/148941448/9c7c0a81-255a-4de6-b88a-45edece798ab">

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
3. Edit app.py by using your Gemini and Google search API keys and search engine ID using the steps below:<br>

For Gemini API line 16, You can get "YOUR API KEY" by using Google AI Studio.
```python
genai.configure(api_key="YOUR API KEY")
```
For Google search API keys line 58 and search engine ID line 59, you can get "YOUR API KEY" by using Custom Search JSON API and "YOUR SEARCH ENGINE ID" by using Programmable Search Engine(free edition) by Google.
```python
def google_search(query):
    api_key = 'YOUR API KEY'
    search_engine_id = 'YOUR SEARCH ENGINE ID'
```
4. Run it in the terminal or Run without Debugging, preferably using VS Code 
```python
python app.py
```
# Limitation
Only Text to Text generation

# Our Presentation
You can view our presentation by scanning the QR code below:

<img width="263" alt="Screen Shot 2567-05-14 at 12 22 48" src="https://github.com/Anonsuksak/DADS5001_tool/assets/148941448/4e99cf4d-5f6f-4546-b52d-f5886e5e720b">

# References
1. Coding Money for Gemini chatbot example - https://www.youtube.com/watch?v=_HNMEGkjzsE
2. Frank Adams for LLM workflow  - https://medium.com/@FrankAdams7/unleashing-the-power-of-large-language-models-building-an-ai-chatbot-for-private-knowledge-base-eb8cf31c7fcc
3. Thakorn.T for embedding knowledge - https://www.tangerine.co.th/blogs/data-analytics-artificial-intelligence/generative-ai-vertor-embedding/
4. Hugging Face for chatbot ideas - https://huggingface.co/spaces?search=gemini
