from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router as api_router

app = FastAPI()

# Cho phép frontend gọi API từ Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Hoặc giới hạn với domain cụ thể
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
