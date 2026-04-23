from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import Response, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from bg_remover import BackgroundRemover

app = FastAPI(title="Background Removal API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_methods=["*"],
    allow_headers=["*"],
)

bg_remover = BackgroundRemover()

app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid image file")

    try:
        image_bytes = await file.read()
        output_png = bg_remover.remove_background(image_bytes)

        return Response(
            content=output_png,
            media_type="image/png",
            headers={
                "Content-Disposition": "inline; filename=output.png"
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
