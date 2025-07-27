echo "🔧 Cài đặt xong, khởi chạy FastAPI..."
prefect server start
uvicorn app.main:app --host 0.0.0.0 --port $PORT