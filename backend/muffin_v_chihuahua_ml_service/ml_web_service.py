import io

from PIL import Image
from fastapi import FastAPI, File, UploadFile

from classifier import predict_class_for

app = FastAPI()


@app.get("/")
def read_root():
    return {"Status": "UP"}


@app.post("/predict/")
async def create_file(file: UploadFile = File(...)):
    img = Image.open(io.BytesIO(file.file.read())).convert('RGB').resize((299, 299), Image.NEAREST)
    preds = predict_class_for(img)
    return {"filename": list((x[0], x[1], float(x[2])) for x in preds)}
