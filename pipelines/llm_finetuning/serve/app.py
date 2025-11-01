from fastapi import FastAPI
from pydantic import BaseModel
from model_loader import load_model, generate

app = FastAPI()
model, tokenizer = load_model()

class GenReq(BaseModel):
    prompt: str
    max_tokens: int = 256

@app.post("/generate")
def gen(req: GenReq):
    result = generate(model, tokenizer, req.prompt, req.max_tokens)
    return {"output": result}
