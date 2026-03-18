from sentence_transformers import SentenceTransformer

# Initialize embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Store embeddings in memory (simple version)
documents = []
embeddings = []

def store_data(data):
    global documents, embeddings

    # Avoid reloading again and again
    if documents:
        return

    for item in data:
        documents.append(item["content"])
        emb = model.encode(item["content"])
        embeddings.append(emb)

def search(query):
    query_emb = model.encode(query)

    # Compute similarity manually
    scores = []
    for emb in embeddings:
        score = sum(a*b for a, b in zip(query_emb, emb))
        scores.append(score)

    # Get top 2 results
    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:2]

    return [documents[i] for i in top_indices]