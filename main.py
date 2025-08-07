from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse
from utils import download_video
import uvicorn

app = FastAPI( 
    title="Vidozer API",
    description="Download videos from YouTube, Instagram, etc.",
    version="1.0.0"
)

@app.post("/download")
async def download(url: str = Form(...), platform: str = Form(...)):
    try:
        path = await download_video(url, platform)
        return FileResponse(path, filename=path.split("/")[-1], media_type='video/mp4')
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)


