# Ollama FastAPI Project

This project is a FastAPI application that integrates with the Ollama API to generate text based on user-provided prompts. It provides both GET and POST endpoints for interacting with the API.

## Features
- **POST /generate**: Accepts a JSON body with a `prompt` field and returns generated text in JSON format.
- **GET /generate**: Accepts a query parameter `prompt` and returns the generated text rendered as an HTML page.

## Requirements
The project requires the following Python packages:

- `fastapi`
- `uvicorn`
- `ollama`
- `python-dotenv`
- `requests`

These dependencies are listed in the `requirements.txt` file.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Ollama
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .venv\Scripts\Activate
     ```
   - On Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API**:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints

### POST /generate
- **Description**: Generates text based on the provided prompt.
- **Request Body**:
  ```json
  {
    "prompt": "Your prompt here"
  }
  ```
- **Response**:
  ```json
  {
    "response": "Generated text here"
  }
  ```

### GET /generate
- **Description**: Generates text based on the provided prompt and renders it as an HTML page.
- **Query Parameter**:
  - `prompt`: The text prompt to generate a response for.
- **Response**: An HTML page displaying the generated text.

## Example Usage

### POST Request
Using `curl`:
```bash
curl -X POST "http://127.0.0.1:8000/generate" -H "Content-Type: application/json" -d '{"prompt": "Hello, how are you?"}'
```

### GET Request
Visit the following URL in your browser:
```
http://127.0.0.1:8000/generate?prompt=Hello
```

## License
This project is licensed under the MIT License.