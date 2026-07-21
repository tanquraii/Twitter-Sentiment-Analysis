from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import joblib

class Text(BaseModel):
    sentence: str

hf_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
model = joblib.load("model.pkl")

app = FastAPI()

@app.post("/text_post")
def read_root(text: Text):
    embeddings = hf_model.encode(text.sentence)

    prediction = model.predict([embeddings])

    message = [
        "Thanks for a good feedback!" if prediction == 0 
        else "We are sorry to hear that!" if prediction == 1 
        else "Thanks for the feedback!" if prediction == 2 
        else "Thanks for reaching out!"  # Final fallback required
    ]

    return {"prediction": message}