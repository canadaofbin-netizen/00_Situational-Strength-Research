import sys
import chromadb
from chromadb.utils import embedding_functions

def get_collection(collection_name="semantic_wiki"):
    # Store DB locally in the .chromadb folder
    client = chromadb.PersistentClient(path="./.chromadb")
    
    # Use the free huggingface embedding model
    # Note: the first time this runs, it downloads the model (~80MB)
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    
    collection = client.get_or_create_collection(
        name=collection_name, 
        embedding_function=sentence_transformer_ef
    )
    return collection

def add_documents(docs, ids, metadatas=None):
    collection = get_collection()
    collection.add(
        documents=docs,
        ids=ids,
        metadatas=metadatas
    )
    print(f"Added {len(docs)} documents to ChromaDB.")

def search_documents(query, n_results=3):
    collection = get_collection()
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vector_db.py [search|add] ...")
        sys.exit(1)
        
    action = sys.argv[1]
    
    if action == "search":
        if len(sys.argv) < 3:
            print("Please provide a search query.")
            sys.exit(1)
        query = " ".join(sys.argv[2:])
        results = search_documents(query)
        import json
        print(json.dumps(results, indent=2, ensure_ascii=False))
        
    elif action == "add":
        # python vector_db.py add "doc_id" "Text content goes here"
        if len(sys.argv) < 4:
            print("Usage: python vector_db.py add <id> <text>")
            sys.exit(1)
        doc_id = sys.argv[2]
        text = sys.argv[3]
        add_documents([text], [doc_id])
