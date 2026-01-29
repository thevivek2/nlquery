from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from ollama import chat
from fastapi.responses import FileResponse, JSONResponse
from Schema import SCHEMA
from Rules import RULES
import uvicorn
from pathlib import Path
from sentence_transformers import SentenceTransformer
import faiss
import json


embedder = SentenceTransformer(
    "all-MiniLM-L6-v2",
    cache_folder="models/sentence-transformers",
    local_files_only=True
)

app = FastAPI()
BASE_DIR = Path(__file__).parent

@app.get("/")
def home():
    return FileResponse(BASE_DIR / "templates" / "index.html")

@app.get("/nl-to-sql")
def nl_to_sql(prompt: str = Query(..., description="Natural language query")):
    index = faiss.read_index("index/vector_store/schema_index.faiss")
    with open("index/vector_store/schema_chunks.json", "r") as f:
        chunks = json.load(f)
    
    query_emb = embedder.encode([prompt])
    
    distances, indices = index.search(query_emb, 2)
    retrieved_chunks = [chunks[i] for i in indices[0]]
    chunksStr = ""
    chunksStr += "\n".join(retrieved_chunks)

    response = chat(model="phi4",
                    messages=[{"role": "system", "content": chunksStr},
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
    uvicorn.run(app, host="127.0.0.1", port=8001)



