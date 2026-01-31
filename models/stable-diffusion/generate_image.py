from diffusers import StableDiffusionPipeline
import torch
import os

MODEL_PATH = "./model"
OUTPUT_DIR = "../../backend/output/images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate(prompt: str, filename: str):
    image = pipe(prompt).images[0]
    path = os.path.join(OUTPUT_DIR, filename)
    image.save(path)
    print(f"Image saved at {path}")


if __name__ == "__main__":
    generate(
        "cinematic fantasy forest, dramatic lighting",
        "scene_1.png"
    )
