# AI Background Remover

A simple web application that removes image backgrounds using an open‑source AI model (rembg).  
The project provides a FastAPI backend and a minimal frontend that allows users to upload an image and download a transparent PNG.


## Features

-  Upload an image via browser
-  AI-powered background removal using `rembg`
- Transparent PNG output
- FastAPI 
- Model loaded only once (Singleton pattern)
- Simple HTML/CSS/JS frontend
- Works on CPU 



## Tech Stack

- **Backend:** FastAPI
- **AI Model:** rembg (RMBG‑v2.0)
- **Frontend:** HTML, CSS, JavaScript
- **Image Processing:** Pillow
- **Server:** Uvicorn


## Create Virtual environment
- python -m venv venv
- venv\Scripts\activate   # Windows
- pip install -r requirements.txt

## Run the application 

- uvicorn main:app --host 0.0.0.0 --port 8000