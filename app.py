from flask import Flask, render_template, request, redirect, url_for, Response, make_response, send_file
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///license.db'
# db = SQLAlchemy(app)


# class License(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     license = db.Column(db.String(100))
@app.route('/',methods=['GET', 'POST'])
def root():
    return redirect('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/sample/<name>')
def Download_File(name):
    PATH= name + '.zip'
    return send_file(PATH,as_attachment=True)



@app.route('/buy', methods=['GET', 'POST'])
def buy():
    return render_template('buy.html')

@app.route('/how_to_buy', methods=['GET', 'POST'])
def how_to_buy():
    return render_template('how_to_buy.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)