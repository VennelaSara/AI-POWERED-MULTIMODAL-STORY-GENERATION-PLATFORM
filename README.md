# AI-Powered Multimodal Story Generation Platform

## Overview
End-to-end AI system that generates illustrated, narrated stories using
local LLMs, Stable Diffusion, and neural TTS.

## Architecture
React → FastAPI → Celery → AI Models → PostgreSQL

## Key Features
- Multimodal story generation
- Character consistency (embeddings + LoRA)
- Scene-level regeneration
- Async processing with Celery
- Real-time WebSocket updates
- 100% zero-cost local stack

## Tech Stack
FastAPI, React, PostgreSQL, Redis, Celery, Stable Diffusion, Ollama, Coqui TTS
