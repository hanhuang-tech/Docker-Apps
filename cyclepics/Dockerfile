FROM alpine:3.5
RUN apk add --update py2-pip
COPY app.py .
COPY templates templates
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
EXPOSE 2000
CMD ["python", "app.py"]
