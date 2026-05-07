import os
from pathlib import Path

def test_pubsub_summary_content():
    pubsub_file = Path("docs/ingestion/pubsub.md")
    
    with open(pubsub_file, "r", encoding="utf-8") as f:
        content = f.read()
        
        # Check for key sections
        assert "## High-Signal Summary" in content, "Missing High-Signal Summary section"
        assert "## Key Concepts" in content, "Missing Key Concepts section"
        
        # Check for 2026 features (expected after implementation)
        assert "BigQuery Subscriptions" in content, "BigQuery Subscriptions should be mentioned"
        assert "Filtering" in content, "Filtering should be mentioned"
        assert "Dead Letter Topics" in content, "Dead Letter Topics should be mentioned"

if __name__ == "__main__":
    try:
        test_pubsub_summary_content()
        print("Pub/Sub Summary Tests Passed!")
    except AssertionError as e:
        print(f"Test Failed: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
