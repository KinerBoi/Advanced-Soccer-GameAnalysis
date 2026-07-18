import os
from dotenv import load_dotenv
from roboflow import Roboflow

load_dotenv()

rf = Roboflow(api_key=os.getenv("ROBOFLOW_API_KEY"))
project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
version = project.version(20)
dataset = version.download("coco")
print(f"Dataset downloaded to: {dataset.location}")