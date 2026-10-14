FROM python:3.12-slim

WORKDIR /app

RUN useradd -m appuser
USER appuser
COPY app/ ./app/
EXPOSE 8080
CMD ["python", "app/app.py"]
