import os
import asyncio
import httpx
from dotenv import load_dotenv

load_dotenv()

REPLICATE_API_URL = "https://api.replicate.com/v1/models/prunaai/wan-image/predictions"
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

headers = {
    "Authorization": f"Bearer {REPLICATE_API_TOKEN}",
    "Content-Type": "application/json"
}

async def poll_until_done(get_url: str, timeout: int = 300, interval: int = 2):
    async with httpx.AsyncClient(timeout=timeout) as client:
        for _ in range(timeout // interval):
            response = await client.get(get_url, headers=headers)
            response.raise_for_status()
            data = response.json()

            status = data.get("status")
            if status in ("succeeded", "failed", "canceled"):
                return data

            await asyncio.sleep(interval)

        raise TimeoutError("Polling timed out")

async def generate_image(prompt: str, seed: int = -1):
    json_data = {
        "input": {
            "prompt": prompt,
            "seed": seed
        }
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        # Step 1: Gửi yêu cầu tạo ảnh
        response = await client.post(REPLICATE_API_URL, headers=headers, json=json_data)
        response.raise_for_status()
        prediction = response.json()

    # Step 2: Poll kết quả liên tục cho đến khi xong
    get_url = prediction["urls"]["get"]
    final_result = await poll_until_done(get_url)

    return final_result.get("output")
