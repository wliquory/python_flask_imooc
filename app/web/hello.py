#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import current_app
from flask import flash
from flask import render_template

from . import web


@web.route('/hello_normal')
def hello_world():

    # status code 200, 404, 301...
    # content-type http headers
    # content-type text/html
    # Response
    return 'Hello World!'


@web.route('/hello_html')
def hello():

    # status code 200, 404, 301...
    # content-type http headers
    # content-type text/html
    # Response
    headers = {
        'content-type': 'text/plain'
    }

    # response = make_response('<html></html>', 404)
    # response.headers = headers
    # return response
    return '<html></html>', 404, headers


@web.route('/test_render')
def test_render():

    r = {
        "name": "yzLan",
        "age": 28
    }

    return render_template("test.html", data=r)

# app.add_url_rule('/hello', view_func=hello_world)
@web.route('/test')
def test():
    r = {
        'name': None,
        'age': 18
    }
    # data['age']
    r1 = {

    }
    flash('hello,qiyue', category='error')
    flash('hello, jiuyue', category='warning')
    # 模板 html
    return render_template('test.html', data=r, data1=r1)


@web.route('/test1')
def test1():
    print(id(current_app))
    from flask import request
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print('-----------------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('-----------------')
    return ''
