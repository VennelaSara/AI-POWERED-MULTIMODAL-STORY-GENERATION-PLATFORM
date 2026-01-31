import subprocess
import json

def generate_story(prompt: str):
    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )
    return {
        "chapters": [
            {"scene": "Opening", "text": result.stdout}
        ]
    }
