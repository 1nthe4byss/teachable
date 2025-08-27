from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List

app = FastAPI()

# setting up templates
templates =Jinja2Templates(directory="templates")

# setting up static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get-started", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("templates.html", {"request": request})

@app.get("/FAQ", response_class=HTMLResponse)
async def faq(request: Request):
    return templates.TemplateResponse("faq.html", {"request": request})


# post request routes for training and prediction
@app.post("/train")
async def train(files: List[UploadFile] = File(...), labels: List[str] = Form(...)):
    # TODO: Implement training logic here
    return {"message": "Training started"}

@app.post("/predict")
async def predict(image: UploadFile = File(...), model: str = Form(...)):
    # TODO: Implement prediction logic here
    return {"message": "Prediction started"}
