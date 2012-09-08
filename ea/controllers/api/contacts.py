# -*- coding: utf-8 -*-
import json
from bottle import request, HTTPResponse
from pymongo import Connection
from bson import ObjectId
from ea.models.contact import *
import datetime
db = Connection('localhost', 27017)['ex']

def remove(id):
    """ Test:
    import requests as R
    _id = '5046168225587124cc9712b2'
    host='http://localhost:3000/api/v1/cnt/%s' % _id
    data='{"fnam": "fred"}'
    headers = {'content-type': 'application/json'}
    print R.put(host, data=data, headers=headers)
    """

    return db.contacts.remove({"_id":ObjectId(id)})

def put(id):
    """ Test:
    import requests as R
    _id = '5046168225587124cc9712b2'
    host='http://localhost:3000/api/v1/cnt/%s' % _id
    data='{"fnam": "fred"}'
    headers = {'content-type': 'application/json'}
    print R.put(host, data=data, headers=headers)
    """
    print request.json
    print ObjectId(id)
    js            = request.json
    
    unam          = 'lwe2'
    now           = datetime.datetime.utcnow()

    try:
        Contact(**js).validate()
    except TypeException, se:
        return HTTPResponse(output='error', status=400, header={'error':se})
    c             = Cnt(**js)
    c.onUpdate()
    js = c.to_python()
    js["log.mOn"] = now
    js["log.mBy"] = unam
    #print {"$set": js}
    db.contacts.update({"_id":ObjectId(id)}, {"$set": js})
    return {"_id":ObjectId(id)}

def post():
    """ Test:
    import requests as R
    host='http://localhost:3000/api/v1/cnt'
    data='{"fnam": "apóstol", "unam": "lwe"}'
    headers = {'content-type': 'application/json'}
    print R.post(host, data=data, headers=headers)
    """
    # print request.json
    # data = request.body.readline().strip("'")
    # js = json.loads(data)
    js = request.json

    unam = js['unam']

    c      = Cnt(**js)
    c.onUpdate()
    now    = datetime.datetime.utcnow()
    log    = Log(
        oBy = unam, oOn = now,
        cBy = unam, cOn = now,
        mBy = unam, mOn = now,
        )
    c.log = log
    id = db.contacts.insert(c.to_python())
    return {'id':id}

def goto(id):
    # http://localhost:3000/api/v1/cnt/<obId string>
    return db.contacts.find_one({"_id": ObjectId(id)})

