FROM huggingface/transformers-gpu

WORKDIR /app

ENV LANG C.UTF-8

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]