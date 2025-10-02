from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def welcome():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>FastAPI - Практическая работа</title>
            
        </head>
        <body>
            <div class="container">
                <h1> FastAPI Практическая работа</h1>
                <div class="info">
                    <p>Работу выполнил:</p>
                    <p class="student-name">Гаврилов А.А.</p>
                </div>
                <div class="info">
                    <p>Группа: <span class="group">ИВТ-432Б</span></p>
                </div>
                <div>
                    <span class="badge">Python</span>
                    <span class="badge">FastAPI</span>
                    <span class="badge">Docker</span>
                </div>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/api/info")
async def get_info() -> dict:
    return {
        "student": "Гаврилов А.А.",
        "group": "ИВТ-432Б",
        "work": "Практическая работа №3 - FastAPI",
        "technologies": ["Python", "FastAPI", "Uvicorn", "Docker"]
    }
