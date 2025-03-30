# To execute - copy and paste following in terminal after activating virtual environment:  
# 1. .venv/Scripts/Activate (Windows) or source .venv/bin/activate (Linux/Mac) to activate the virtual environment
# 2. uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
from pydantic import BaseModel
import ollama

app = FastAPI()

# Define a request body schema
class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_post(request: PromptRequest):
    """
    Generate text based on the provided prompt using the Ollama API (POST method).
    """
    try:
        # Call the Ollama API to generate text
        response = ollama.chat(model="llama2", messages=[{"role": "user", "content": request.prompt}])
        
        # Return the generated text
        return {"response": response["message"]["content"]}
    except Exception as e:
        # Handle any errors that occur during text generation
        return {"error": str(e)}

@app.get("/generate", response_class=HTMLResponse)
async def get_generate_html(prompt: str):
    """
    Get the generated text based on the provided prompt using the Ollama API (GET method).
    Render the response as HTML.
    """
    try:
        # Call the Ollama API to generate text
        response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
        generated_text = response["message"]["content"]

        # Render the response as HTML
        html_content = f"""
        <html>
            <head><title>Generated Text</title></head>
            <body>
                <h1>Generated Text</h1>
                <p>{generated_text}</p>
            </body>
        </html>
        """
        return HTMLResponse(content=html_content)
    except Exception as e:
        # Handle any errors that occur during text generation
        error_html = f"""
        <html>
            <head><title>Error</title></head>
            <body>
                <h1>Error</h1>
                <p>{str(e)}</p>
            </body>
        </html>
        """
        return HTMLResponse(content=error_html, status_code=500)