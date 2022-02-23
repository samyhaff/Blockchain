FROM python:3.9.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "app.py"]
