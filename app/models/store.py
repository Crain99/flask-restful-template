#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    store_id = db.Column(db.String(10))
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name, store_id):
        self.name = name
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'store_id': self.store_id, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
