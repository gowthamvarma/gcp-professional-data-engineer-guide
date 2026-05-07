import os
from pathlib import Path

def test_ingestion_files_exist():
    base_dir = Path("docs/ingestion")
    index_file = base_dir / "index.md"
    pubsub_file = base_dir / "pubsub.md"
    
    assert index_file.exists(), f"{index_file} does not exist"
    assert pubsub_file.exists(), f"{pubsub_file} does not exist"

def test_ingestion_headers():
    index_file = Path("docs/ingestion/index.md")
    pubsub_file = Path("docs/ingestion/pubsub.md")
    
    with open(index_file, "r") as f:
        content = f.read()
        assert content.startswith("# Domain 1: Data Ingestion and Messaging"), "Index header mismatch"
        
    with open(pubsub_file, "r") as f:
        content = f.read()
        assert content.startswith("# Pub/Sub: Messaging and Streaming"), "Pub/Sub header mismatch"

if __name__ == "__main__":
    try:
        test_ingestion_files_exist()
        test_ingestion_headers()
        print("Tests Passed!")
    except AssertionError as e:
        print(f"Test Failed: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
