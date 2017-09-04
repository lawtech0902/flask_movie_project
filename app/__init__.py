# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/8/13 下午9:24'
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask.ext.redis import FlaskRedis

import pymysql
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = '18037ef7318e4f79bc7b8f38eceba15a'
app.config["REDIS_URL"] = "redis://localhost:6379/0"
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")
app.debug = True
db = SQLAlchemy(app)
rd = FlaskRedis(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


# 404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
