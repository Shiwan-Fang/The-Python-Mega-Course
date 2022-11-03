from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/height_collector' #连上数据库height_collector
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data" #在数据库height_collector建立一个table，表头设置如下
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True) #email是唯一的unique，所以不能两次输入同一个email
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        if db.session.query(Data).filter(Data.email_==email).count() == 0: #防止输入相同的email
            data=Data(email,height) #先将数据变成class Data的格式，然后再加到数据库里，然后确认commit，如果没有这一行直接add会出错
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height,1)
            count=db.session.query(Data.height_).count()
            send_email(email,height,average_height,count)
            return render_template("success.html")
    return render_template('index.html', text="Seems like we've got something from that email adress already!")


if __name__ =='__main__': 
#if the script has been executed not been imported, we will execute the lines below
    app.debug=True
    app.run(port=5000)

