FROM python:3.9-slim-buster
RUN pip install requests
WORKDIR /BTC-ETH-Converter
ADD main.py .
ENTRYPOINT ["python", "./main.py"]