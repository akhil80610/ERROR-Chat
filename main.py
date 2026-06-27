print("THIS IS THE CORRECT MAIN.PY")
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

print("=" * 50)
print("Running main.py from:")
print(__file__)
print("Current Working Directory:")
print(os.getcwd())
print("=" * 50)

load_dotenv()

app = FastAPI()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

SYSTEM_PROMPT = """
    You are an expert software debugging assistant.

    Your task is:
    - Explain the meaning of the error.
    - Explain the probable causes.
    - Give possible solutions.
    - Use bullet points.
    - If the error log is incomplete, mention that.
    """

@app.post("/predict")
def predict(data: PromptRequest):
    

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": data.prompt
        }
    ]
    )

    return {
        "response": response.choices[0].message.content
    }