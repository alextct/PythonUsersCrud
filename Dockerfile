FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install flask \
    pip install python-decouple \
    pip install pymysql \
    pip install requests
EXPOSE 5001
VOLUME /app/logs
CMD python3 rest_app.py