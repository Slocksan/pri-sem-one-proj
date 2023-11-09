import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

stringToTranslate = st.text_input("Введите ваш текст")

if (st.button("Перевести")):
    input_ids = tokenizer.encode(stringToTranslate, return_tensors="pt")

    outputs = model.generate(input_ids)

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    st.write("Перевод: " + decoded)