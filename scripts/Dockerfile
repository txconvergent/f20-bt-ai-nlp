FROM nikolaik/python-nodejs
WORKDIR /app
COPY . /app
RUN pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.8.0-py3-none-any.whl
RUN pip install -r requirements.txt
EXPOSE 8000
RUN uvicorn fastApi:app --reload