import os

# --- TRAINING EXAMPLE ONLY: DO NOT USE REAL SECRETS ---

# 1. Fake GitHub Personal Access Token (PAT)
# Pattern: starts with 'ghp_' followed by 36 alphanumeric characters
GITHUB_TOKEN = "ghp_n0tArEaLt0kEnJuStF0rTrAiNiNgPurp0s3s"

# 2. Fake AWS Access Key ID
# Pattern: starts with 'AKIA' followed by 16 uppercase alphanumeric characters
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

def connect_to_api():
    print(f"Using token: {GITHUB_TOKEN}")
    print("Attempting to connect...")

if __name__ == "__main__":
    connect_to_api()
