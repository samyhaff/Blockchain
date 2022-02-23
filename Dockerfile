FROM python:3.9.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl", "-Sf" "localhost:80" ]
ENTRYPOINT ["python", "app.py"]
