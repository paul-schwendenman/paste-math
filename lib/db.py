from google.appengine.ext import db
import random
abc = "abcdefghijklmnopqrstuvwxyz"

def getUrlString():
    f = random.randrange
    return abc[f(26)] + abc[f(26)] + abc[f(26)] + abc[f(26)] +  abc[f(26)]

class Page(db.Model):
    url = db.StringProperty()
    title = db.StringProperty()
    content = db.TextProperty()

q = db.GqlQuery
d = db.delete