# -*- coding: utf-8 -*-
import os
from controllers.api import common
from controllers import home

root_api = '/api/v1/'

def init(app):
    # leave as first route. For serving static files
    app.route('/<filename:re:.*\.(css|js|ico|html)>',   callback = common.static)

    # common / shared core controllers
    app.get(root_api    + '<model>/find<q:re:.*>',      callback = common.find)
    app.get(root_api    + '<model>/<id>',               callback = common.get)
    app.put(root_api    + '<model>/<id>',               callback = common.put)
    app.delete(root_api + '<model>/<id>',               callback = common.remove)
    app.post(root_api   + '<model>',                    callback = common.post)

    app.get('/', callback = home.get)
    return app