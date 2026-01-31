from diffusers import StableDiffusionPipeline
import torch

print("Downloading Stable Diffusion model...")

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

pipe.save_pretrained("./model")

print("Model downloaded and saved locally.")
