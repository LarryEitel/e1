# -*- coding: utf-8 -*-
# import wingdbstub
#from lib.bottle import request, default_app
from pymongo import Connection

def get():
    # app = default_app.pop()
    # print app.plugins
    # query = request.query.__dict__
    # app.mongodb
    # #print mongodb
    db     = Connection('localhost', 27017)['ex']
    return [a for a in db.contacts.find()]
