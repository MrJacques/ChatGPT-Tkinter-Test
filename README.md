# ChatGPT-Tkinter-Test

This is a very simple tkinter python program that calls the ChatGPT API.

Basically...

- Get an API key from OpenAI
- Setup the venv
- Install requirements
- Run Chat.py
- Enter API key
- Start asking questions

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python chat.py
```

> **Warning**
>
>This will create an api_key.pickle that contains the API key.  You will want to keep this a secret.

> **Note**
>
>This chat does not retain context between questions.  In other words, you cannot ask follow up questions

The basics of this came from ChapGPT itself and a udemy class.

https://cognizant.udemy.com/course/create-a-chatgpt-ai-bot-with-tkinter/

