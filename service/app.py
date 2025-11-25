from fastapi import FastAPI
from joblib import load

from service.schemas import ClientInput
from service.preprocess import preprocess_input

app = FastAPI(title="Bank Churn Prediction API", version="1.0")

bundle = load("service/model.joblib")
model = bundle["model"]
meta = bundle["meta"]

feature_cols = meta["feature_cols"]
cat_cols = meta["cat_cols"]

@app.post("/predict")
def predict(client: ClientInput):
    data = client.dict()

    df = preprocess_input(data, feature_cols, cat_cols)

    proba = float(model.predict_proba(df)[0][1])
    pred = int(proba >= 0.5)

    return {
        "probability": proba,
        "prediction": pred
    }
