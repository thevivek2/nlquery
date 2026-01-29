from sentence_transformers import SentenceTransformer
import faiss
import json
import os


# ----  Create a metadata file with mutiple table, columns, relationship  
#       based on template (see : supported_meatadata_template.md) format, save it
# ----- that can be used here as input 
# ---------- Step 1: Load schema ----------
SCHEMA_PATH = r"C:\Work\Projects\codespaces-jupyter\new_output\metadata.json"

print("reading metadata files")
with open(SCHEMA_PATH, "r") as f:
    schema = json.load(f)

print("Flatten schema into text chunks")
# ---------- Step 2: Flatten schema into text chunks ----------
chunks = []

for table in schema.get("tables", []):
    table_name = table.get("name")
    table_desc = table.get("description", "")

    # Table-level chunk
    table_chunk = (
        f"Table: {table_name}\n"
        f"Description: {table_desc}\n"
        f"Row count: {table.get('row_count')}\n"
        f"Source: {table.get('source_id')}"
    )
    chunks.append(table_chunk)

    # Column-level chunks
    for col in table.get("columns", []):
        col_chunk = (
            f"Table: {table_name}\n"
            f"Column: {col.get('name')}\n"
            f"Description: {col.get('description')}\n"
            f"Type: {col.get('inferred_type')}\n"
            f"Nullable: {col.get('nullable')}\n"
            f"PII: {col.get('pii', {}).get('flag')}\n"
            f"Distinct count: {col.get('distinct_count')}\n"
            f"Examples: {col.get('examples')[:3]}"
        )
        chunks.append(col_chunk)

print(f"Generated {len(chunks)} chunks")

# ---------- Step 3: Generate embeddings ----------
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(chunks, convert_to_numpy=True, show_progress_bar=True)

# ---------- Step 4: Create FAISS index ----------
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# ---------- Step 5: Persist index and chunks ----------
os.makedirs("vector_store", exist_ok=True)

faiss.write_index(index, "vector_store/schema_index.faiss")

with open("vector_store/schema_chunks.json", "w") as f:
    json.dump(chunks, f, indent=2)

print("FAISS index and chunks saved")
