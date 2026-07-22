# 1. Import the library
from inference_sdk import InferenceHTTPClient
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env and loads its variables into the environment

apiKey = os.getenv("API_KEY")

# 2. Connect to your workflow
client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=apiKey
)

# 3. Run your workflow on an image
result = client.run_workflow(
    workspace_name="kinish-sathish",
    workflow_id="football-players-detection-v1-logic",
    images={
        "image": "test_images/spainportugal232018.png" # Path to your image file
    },
    use_cache=True # Speeds up repeated requests
)

# 4. Get your results
print(result[0]['json_parser_output_2'])
