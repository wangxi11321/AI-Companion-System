from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn
import os

from app.routers.tools import router as tools_router

app = FastAPI(
    title="客户研判系统",
    description="留学机构客户研判模块 - 集成Dify接口",
    version="1.0.0"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

index_html_path = os.path.join(FRONTEND_DIR, "index.html")
if os.path.exists(index_html_path):
    with open(index_html_path, "r", encoding="utf-8") as f:
        HTML_CONTENT = f.read()
else:
    HTML_CONTENT = "<h1>客户研判系统</h1>"

app.mount("/frontend", StaticFiles(directory=FRONTEND_DIR), name="frontend")
app.include_router(tools_router, prefix="/api/tools", tags=["Tools"])

@app.get("/", response_class=HTMLResponse, description="前端页面")
async def root():
    return HTML_CONTENT

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

@app.get("/api")
async def api_info():
    return {
        "message": "欢迎使用客户研判系统",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "create_customer": "POST /api/tools/create_customer"
        }
    }

if __name__ == "__main__":
    print("=" * 60)
    print("🤖 客户研判系统 v1.0.0")
    print("=" * 60)
    print("🌐 前端页面: http://127.0.0.1:8000/")
    print("📚 API文档:  http://127.0.0.1:8000/docs")
    print("🏥 健康检查: http://127.0.0.1:8000/health")
    print("🔧 研判接口: POST /api/tools/create_customer")
    print("=" * 60)
    
    uvicorn.run("app_with_frontend:app", host="127.0.0.1", port=8000, reload=True)