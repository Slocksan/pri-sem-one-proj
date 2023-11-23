import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

@st.cache
def load_tokenizer():
    return AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

@st.cache
def load_model():
    return AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

stringToTranslate = st.text_input("Введите ваш текст (на русском)")

st.image('fbzr.jpg')

if (st.button("Перевести")):
    input_ids = load_tokenizer().encode(stringToTranslate, return_tensors="pt")

    outputs = load_model().generate(input_ids)

    decoded = load_tokenizer().decode(outputs[0], skip_special_tokens=True)

    with open('queryis.txt', 'a', encoding='utf-8') as f:
        f.write(stringToTranslate +" --- " + decoded + '\n')

    st.write("Перевод: " + decoded)