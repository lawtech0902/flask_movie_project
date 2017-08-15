# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/8/13 下午9:27'
"""

from . import admin


@admin.route('/')
def index():
    return "<h1 style='color:red'>this is admin</h1>"
