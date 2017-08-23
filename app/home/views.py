# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/8/13 下午9:26'
"""

from . import home
from flask import render_template, redirect, url_for, flash
from app.home.forms import RegisterForm
from app.models import User
from werkzeug.security import generate_password_hash
from app import db

import uuid


# 会员登录
@home.route('/login/')
def login():
    return render_template("home/login.html")


# 会员退出登录
@home.route('/logout/')
def logout():
    return redirect(url_for("home.login"))


# 会员注册
@home.route('/regist/', methods=["GET", "POST"])
def regist():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            pwd=generate_password_hash(data["pwd"]),
            uuid=uuid.uuid4().hex
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功！", "ok")
    return render_template("home/regist.html", form=form)


# 会员中心
@home.route('/user/')
def user():
    return render_template("home/user.html")


# 修改密码
@home.route('/pwd/')
def pwd():
    return render_template("home/pwd.html")


# 评论
@home.route('/comments/')
def comments():
    return render_template("home/comments.html")


# 登录日志
@home.route('/loginlog/')
def loginlog():
    return render_template("home/loginlog.html")


# 收藏电影
@home.route('/moviecol/')
def moviecol():
    return render_template("home/moviecol.html")


# 首页
@home.route('/')
def index():
    return render_template("home/index.html")


# 电影列表
@home.route('/animation/')
def animation():
    return render_template("home/animation.html")


# 电影搜索
@home.route('/search/')
def search():
    return render_template("home/search.html")


# 电影详情
@home.route('/play/')
def play():
    return render_template("home/play.html")
