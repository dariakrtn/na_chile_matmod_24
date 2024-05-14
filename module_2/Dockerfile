
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["streamlit", "run", "app/main.py", "--server.maxUploadSize 2048"]
EXPOSE 8501