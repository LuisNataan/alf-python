FROM python

RUN pip3 install flask && pip3 install pandas && pip3 install mysql

COPY Serasa/ Serasa/
COPY app.py app.py

CMD [ "python -m flask run --port=3306" ]
