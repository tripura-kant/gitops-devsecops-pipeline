FROM python:3.x-slim
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
RUN adduser -D -H -u 10001 appuser
COPY --chown=appuser:appuser app/ ./app/
USER 10001
EXPOSE 8080
CMD ["python", "app/app.py"]