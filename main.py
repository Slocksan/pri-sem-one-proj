from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


# Dependency
def getTranslator():
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

    def getTranslate(textToTranslate: str) -> str:
        input_ids = tokenizer.encode(textToTranslate, return_tensors="pt")
        outputs = model.generate(input_ids)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)

    yield getTranslate


@app.get("/translate", response_model=str)
def translate(textToTranslate: str, translate = Depends(getTranslator)):
    return translate(textToTranslate)
