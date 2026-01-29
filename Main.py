from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from ollama import chat
from fastapi.responses import FileResponse, JSONResponse
from Schema import SCHEMA
from Rules import RULES
import uvicorn
from pathlib import Path


app = FastAPI()
BASE_DIR = Path(__file__).parent

@app.get("/")
def home():
    return FileResponse(BASE_DIR / "templates" / "index.html")

@app.get("/nl-to-sql")
def nl_to_sql(prompt: str = Query(..., description="Natural language query")):
    response = chat(model="phi",
                    messages=[{"role": "system", "content": SCHEMA},
                              {"role": "assistant", "content": RULES},
                              {"role": "user", "content": prompt}],
                    keep_alive= True
        )
    return JSONResponse({
        "prompt": prompt,
        "sql": clean_sql(response["message"]["content"].strip())
    })


def clean_sql(text: str) -> str:
    return text.replace("```sql", "").replace("```", "").strip()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



