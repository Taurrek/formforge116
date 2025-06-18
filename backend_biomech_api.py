from fastapi import FastAPI
from pydantic import BaseModel
from modules.biomech_model import BiomechModel

app = FastAPI()
model = BiomechModel()

class CalibIn(BaseModel):
    joint_angles: dict
    subject_info: dict

class PredictIn(BaseModel):
    joint_df: list

@app.post("/api/biomech/calibrate")
def calibrate(data: CalibIn):
    params = model.calibrate(data.joint_angles, data.subject_info)
    return {"calibration_params": params}

@app.post("/api/biomech/predict")
def predict(data: PredictIn):
    result = model.predict_risk(data.joint_df)
    return result
