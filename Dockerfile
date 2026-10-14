FROM python:3.12-alpine

WORKDIR /app

RUN adduser -D -H -u 10001 appuser
USER appuser
COPY app/ ./app/
EXPOSE 8080
CMD ["python", "app/app.py"]
