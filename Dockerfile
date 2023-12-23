FROM python:3.8
WORKDIR /app
COPY read.py /app/read.py
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "read.py"]
