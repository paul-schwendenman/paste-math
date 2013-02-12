from google.appengine.ext import db
import random
import datetime
abc = "abcdefghijklmnopqrstuvwxyz"

def getUrlString():
    f = random.randrange
    return abc[f(26)] + abc[f(26)] + abc[f(26)] + abc[f(26)] +  abc[f(26)]

class Page(db.Model):
    url = db.StringProperty()
    title = db.StringProperty()
    grade = db.IntegerProperty()
    published = db.BooleanProperty()
    timestamp = db.DateTimeProperty()
    content = db.TextProperty()

class Todo(db.Model):
    open = db.BooleanProperty()
    title = db.StringProperty()
    content = db.TextProperty()

q = db.GqlQuery
d = db.delete