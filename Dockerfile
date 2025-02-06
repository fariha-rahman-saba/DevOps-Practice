FROM python:3.9

WORKDIR /app

COPY main.py /app/main.py

RUN pip install requests

CMD ["python", "main.py"]