from flask import current_app, flash, redirect, url_for
from flask import render_template
from sqlalchemy import desc

from app import db
from app.libs.enums import PendingStatus
from app.models.drift import Drift
from app.models.gift import Gift
from app.service.gift import GiftService
from app.view_models.gift import MyGifts
from . import web
from flask_login import login_required, current_user


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
        desc(Gift.create_time)).all()
    wishes_count = GiftService.get_wish_counts(gifts)
    view_model = MyGifts(gifts, wishes_count).package()
    return render_template('my_gifts.html', gifts=view_model)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):

    if current_user.can_save_to_list(isbn):

        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)

    else:
        flash('这本书已经添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加。')

    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    gift = Gift.query.filter_by(id=gid, launched=False).first()
    if not gift:
        flash('该书籍不存在，或已经交易，删除失败')
    drift = Drift.query.filter_by(gift_id=gid, pending=PendingStatus.waiting).first()
    if drift:
        flash('这个礼物正处于交易状态，请先前往鱼漂完成该交易')
    else:
        with db.auto_commit():
            current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
            gift.delete()
    return redirect(url_for('web.my_gifts'))



