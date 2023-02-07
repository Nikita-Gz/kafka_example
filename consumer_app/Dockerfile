FROM python
COPY . /app
WORKDIR /app

RUN pip install kafka-python
RUN pip install requests

CMD ["python", "-u", "main.py"]
