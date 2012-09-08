# -*- coding: utf-8 -*-
#import wingdbstub
import os, json
from bottle import request, abort,  static_file
from pymongo import Connection
from bson import ObjectId
import datetime

from ea.models import common, contact

# either use bottle plugin or this connection
db = Connection('localhost', 27017)['ex']

# this allows the model parameter to map to the corresponding collection Model which is required for a few of these functions
models = {'contacts': contact.Contact, 'companys': contact.Company, 'persons': contact.Person, 'users':contact.User}

server_root = None
def static(filename):
    global server_root
    if not server_root:
        # server_root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'public')
        server_root = 'public'
    return static_file(filename, root=server_root)
def get(model, id):
    # http://localhost:3000/api/v1/contacts/50463aa32558713cecaeb26b
    col = models[model].meta['collection']
    return db[col].find_one({"_id": ObjectId(id)})
def find(model, q):
    # http://localhost:3000/api/v1/contacts/find/?sort=[{"fnam":"-1"}]&fields=["fnam"]&find={"fnam":"apóstol"}&limit=1&skip=0
    #print request.params.__dict__
    g = request.GET
    if 1:
        if 'find'   in g: print g['find']
        if 'fields' in g: print g['fields']
        if 'sort'   in g: print g['sort']
        if 'skip'   in g: print g['skip']
        if 'limit'  in g: print g['limit']

    find     = json.loads(g['find'])      if 'find' in g else {}
    fields   = json.loads(g['fields'])    if 'fields' in g else None

    sort_raw = json.loads(g['sort'])      if 'sort' in g else None
    # mongo wants sorts like: [("fld1", <order>), ("fld2", <order>)]
    sorts    = []
    if sort_raw:
        flds = sort_raw
        for fld in flds:
            sorts = [(k,int(v)) for k,v in fld.iteritems()]

    skip       = int(json.loads(g['skip']))   if 'skip' in g else -1
    limit      = int(json.loads(g['limit']))  if 'limit' in g else 0
    skip_limit = skip > -1 and limit

    # build and return find
    col = models[model].meta['collection']
    if find:
        if fields:
            cursor = db[col].find(find,fields=fields)
        else:
            cursor = db[col].find(find)
    else:
        cursor = db[col].find(find)
    if sorts: cursor = cursor.sort(sorts)
    if skip_limit: return cursor[skip:limit]
    return cursor
def remove(model, id):
    """ Test:
    import requests as R
    _id = '5046168225587124cc9712b2'
    host='http://localhost:3000/api/v1/contacts/%s' % _id
    data='{"fnam": "fred"}'
    headers = {'content-type': 'application/json'}
    print R.put(host, data=data, headers=headers)
    """

    col = models[model].meta['collection']
    return db[col].remove({"_id":ObjectId(id)})
def put(model, id):
    """ Test:
    import requests as R
    _id = '5046168225587124cc9712b2'
    host='http://localhost:3000/api/v1/contacts/%s' % _id
    data='{"fnam": "fred"}'
    headers = {'content-type': 'application/json'}
    print R.put(host, data=data, headers=headers)
    """
    js            = request.json

    unam          = 'lwe2'
    uoid          = ObjectId("50468de92558713d84b03fd7")
    now           = datetime.datetime.utcnow()

    try:
        models[model](**js).validate()
    except TypeException, se:
        return HTTPResponse(output='error', status=400, header={'error':se})
    m             = models[model](**js)
    js = m.to_python()
    js["log.mOn"] = now
    js["log.mBy"] = uoid

    col = models[model].meta['collection']
    db[col].update({"_id":ObjectId(id)}, {"$set": js})

    # Need to run m.onUpdate to handle any changes affecting fields handled in onUpdate
    js = db[col].find_one({"_id":ObjectId(id)})
    m  = models[model](**js)
    m.onUpdate()
    js = m.to_python()
    db[col].update({"_id":ObjectId(id)}, {"$set": js})
    return {"_id":ObjectId(id)}
def post(model):
    """ Test:
    import requests as R
    host='http://localhost:3000/api/v1/contacts'
    data='{"fnam": "apóstol", "unam": "lwe"}'
    headers = {'content-type': 'application/json'}
    print R.post(host, data=data, headers=headers)
    """

    # Need to grab user to pass in ObjectId to log who added
    uoid = ObjectId("50468de92558713d84b03fd7")

    m    = models[model](**request.json)
    m.onUpdate()
    now    = datetime.datetime.utcnow()
    log    = common.Log(
        oBy = uoid, oOn = now,
        cBy = uoid, cOn = now,
        mBy = uoid, mOn = now,
        )
    m.log = log
    col   = models[model].meta['collection']
    id    = db[col].insert(m.to_python())
    return {'id':id}
