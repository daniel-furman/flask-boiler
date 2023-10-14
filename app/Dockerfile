FROM python:3.12-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["python", "-u", "app.py"]