# InvestmentApp
Pet project.

I created myself this simple app.

Console & gui investment app to manage data about stocks. Functions of the app: look, insert, delete & update data.

App uses python 3, postgresql 14, rabbitmq, tkinter, API (get), sqlalchemy.

Preparation steps:
1) Set API Token from https://www.alphavantage.co/ in api.py file.
2) Set db name, db user, db pwd in sql.py, sql_create.py & tk.py files.
Create table & sequence in postgresql db with sql_create.py file.
3) Set message broker connection details in rabbitmq.py & consumer.py files.