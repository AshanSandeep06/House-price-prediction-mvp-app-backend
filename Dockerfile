FROM python:3.9

WORKDIR /usr/src/app

# Instead of Copying all the files in the backend including such as venv
# We copy only requirements.txt file(e files walata Yana space eka wadi nisa
# uparimenma simple widihata Dockerfile eka thiygnna ona)
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .
COPY .env .
COPY routes ./routes
COPY models ./models
COPY ml_model ./ml_model
COPY controllers ./controllers

EXPOSE 8000

CMD ["python", "main.py"]