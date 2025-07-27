# prefect_flows.py
from prefect import flow, task
from typing import List
from app.services.replicate_service import generate_image  # function async call to Replicate API

@task
async def call_image_generation(prompt: str) -> str:
    image_url = await generate_image(prompt)
    return image_url

@flow
def image_generation_flow(prompt: str) -> str:
    url = call_image_generation(prompt)
    return url
