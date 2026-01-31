from TTS.api import TTS
import os

OUTPUT_DIR = "../../backend/output/audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

def generate(text: str, filename: str):
    path = os.path.join(OUTPUT_DIR, filename)
    tts.tts_to_file(text=text, file_path=path)
    print(f"Audio saved at {path}")


if __name__ == "__main__":
    generate(
        "Once upon a time, in a mysterious forest...",
        "scene_1.wav"
    )
