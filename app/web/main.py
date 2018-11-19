from flask import render_template

from app.service.gift import GiftService
from . import web


__author__ = '七月'


@web.route('/')
def index():
    gift_list = GiftService.recent()
    return render_template('index.html', recent=gift_list)


@web.route('/personal')
def personal_center():
    pass
