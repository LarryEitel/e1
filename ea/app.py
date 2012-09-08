#import wingdbstub
import os
from bottle import run, debug, Bottle
import bottle_mongo as bottle_mongo
import urls
# sys.path.append('C:\\Users\\Larry\\__prjs\\_ex\\_prjs\\ab')

# init app
app = Bottle(autojson=False)
app.install(bottle_mongo.MongoPlugin(uri="localhost", db="ex", json_mongo=True))

#------ Here is where we init all routes
app = urls.init(app)

if __name__ == "__main__":
    if os.environ.get("DEV"):
        print "Starting as DEV"
        debug(True)
        run(app=app, host="127.0.0.1", port=os.environ.get("PORT", 3000), reloader=True)
    else:
        run(app=app, host="127.0.0.1", port=os.environ.get("PORT", 3000))
