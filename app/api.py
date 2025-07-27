from fastapi import APIRouter
from pydantic import BaseModel
from app.prefect_flows import image_generation_flow

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate-image")
async def generate_image_endpoint(req: PromptRequest):
    try:
        url = image_generation_flow(req.prompt)
        return {"imageUrl": url}
    except Exception as e:
        return {"error": str(e)}
