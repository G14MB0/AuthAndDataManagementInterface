FROM python:3.12.2 

WORKDIR /usr/src/app 

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python main.py
