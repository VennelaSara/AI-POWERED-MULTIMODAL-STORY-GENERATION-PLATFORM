from TTS.api import TTS

print("Downloading TTS model...")

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

print("TTS model ready.")
