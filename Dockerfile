FROM  python:3.8.16-alpine3.18
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY flask_service  flask_service
COPY fastapi_service fastapi_service
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT [ "python","./flask_service/main.py" ]
