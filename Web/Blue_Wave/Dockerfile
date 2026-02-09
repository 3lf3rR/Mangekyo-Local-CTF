FROM python:3.11-slim
WORKDIR ssti
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 
ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=4002
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 4002
CMD ["flask", "run"]
