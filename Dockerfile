FROM python:3.11.6-slim

COPY ./requirements.txt /requirements.txt
COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN pip install -r /requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "./app/streamlit_app.py", "--server.port=8501", "--server.address=localhost"]