from diffusers import StableDiffusionPipeline
from diffusers.training_utils import train_text_to_image_lora

train_text_to_image_lora(
    pretrained_model_name_or_path="runwayml/stable-diffusion-v1-5",
    instance_data_dir="character_images",
    output_dir="lora_output",
    instance_prompt="photo of main_character",
    resolution=512,
    train_batch_size=1,
    max_train_steps=800
)
