from app.core.llm import generate_story_text
from app.core.image_generator import generate_image
from app.core.voice_generator import generate_voice
import os


def generate_full_story(prompt: str, output_dir="backend/output"):
    os.makedirs(output_dir, exist_ok=True)

    text = generate_story_text(prompt)

    image_path = f"{output_dir}/scene.png"
    audio_path = f"{output_dir}/scene.wav"

    generate_image(prompt, image_path)
    generate_voice(text, audio_path)

    return {
        "text": text,
        "image": image_path,
        "audio": audio_path
    }
