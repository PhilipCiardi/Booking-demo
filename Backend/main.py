from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
STATIC_DIR = os.path.join(BASE_DIR, "static")

if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def read_index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))


@app.get("/boka_behandling")
def read_boka_behandling():
    return FileResponse(os.path.join(FRONTEND_DIR, "boka_behandling.html"))