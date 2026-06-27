# AI Debugging Assistant

An AI-powered debugging assistant built using **FastAPI**, **Groq API**, and **Llama 3.3 70B Versatile**. The application helps developers understand programming errors by providing clear explanations, identifying probable causes, and suggesting practical solutions.

The assistant accepts compiler errors, runtime exceptions, stack traces, or general coding problems through a simple web interface. It then uses a Large Language Model (LLM) to analyze the input and generate structured responses that help users debug their code more effectively.

## Features

* Explain compiler and runtime error messages.
* Identify possible causes of errors.
* Suggest practical debugging steps and solutions.
* Clean and responsive web interface.
* FastAPI backend with REST API architecture.
* Integration with Groq's Llama 3.3 70B Versatile model.
* Markdown-formatted AI responses for improved readability.

## Tech Stack

### Backend

* Python
* FastAPI
* Groq API
* Pydantic
* Jinja2
* Uvicorn

### Frontend

* HTML5
* CSS3
* JavaScript

### AI Model

* Llama 3.3 70B Versatile (Groq)

## Project Structure

```
AI-Debugging-Assistant/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── envi/
```

## Installation

1. Clone the repository.

2. Create a virtual environment.

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Create a `.env` file and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

5. Start the FastAPI server:

```
uvicorn main:app --reload
```

6. Open your browser and visit:

```
http://127.0.0.1:8000
```

## Example Use Cases

* Understanding Python exceptions
* Explaining C/C++ compiler errors
* JavaScript runtime errors
* Java stack traces
* SQL errors
* General programming questions
* Debugging multi-line error logs

## Future Improvements

* Conversation history
* Authentication and user accounts
* File upload for source code and log files
* Syntax-highlighted code blocks
* Multi-model AI support
* Export responses as PDF or Markdown
* Dark mode
* Conversation memory using a database

## License

This project is intended for educational and portfolio purposes.

