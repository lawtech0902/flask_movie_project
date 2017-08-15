# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/8/13 下午9:26'
"""

from flask import Blueprint

admin = Blueprint("admin", __name__)

import app.admin.views