#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.search_util import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel
from . import web


@web.route('/book/search')
def search():
    """
    :param q:普通关键字 或 isbn
    :param page:
    :return:
    """

    form = SearchForm(request.args)
    if not form.validate():
        return jsonify(form.errors)

    q = form.q.data.strip()
    page = form.page.data
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
        result = BookViewModel.package_single(result, q)
    else:
        result = YuShuBook.search_by_keyword(q, page)
        result = BookViewModel.package_single(result, q)

    return jsonify(result)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
