Bank Churn Prediction Service predicts customer churn probability.
Built with CatBoost, FastAPI, and fully packaged in Docker.

Features:
- Predicts churn probability (float) and churn label (0/1)
- REST API built with FastAPI
- Dockerized for easy deployment
- Includes trained CatBoost model (model.joblib)
- Simple, clean project structure

Project Structure:

bank_churn:
- bank_churn_tz.ipynb
- service:
    - app.py
    - preprocess.py 
    - schemas.py 
- model.joblib
- requirements.txt
- Dockerfile
- README.md

Run with Docker - build the image (commands):
- docker build -t churn-api .
Run the container:
- docker run -p 8000:8000 churn-api
Visit the API docs:
- http://localhost:8000/docs
- Example Request (POST /predict)
{
  "фамилия": "Иванов",
  "кредитный_рейтинг": 610,
  "город": "Ташкент",
  "пол": "Мужской",
  "возраст": 42,
  "стаж_в_банке": 5,
  "баланс_депозита": 150000.5,
  "число_продуктов": 2,
  "есть_кредитка": 1,
  "активный_клиент": 1,
  "оценочная_зарплата": 230000.0,
  "баланс_депозита_missing": 0
}

Example response:
{
  "probability": 0.055851354908599625,
  "prediction": 0
}

Notes:
CatBoost handles categorical features and missing values internally
Preprocessing for inference is minimal and defined in preprocess.py
The API requires all input fields defined in schemas.py