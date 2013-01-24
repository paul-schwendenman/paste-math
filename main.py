from lib import bottle
from lib.bottle import route, template, request, error, debug, static_file
from google.appengine.ext.webapp.util import run_wsgi_app
import lib.db
from lib.html import addLineBreaks


@route('/')
def index():
    #q = lib.db.q("SELECT url, title FROM Page")
    q = lib.db.Page.all()
    result = [[p.url, p.title] for p in q.run()]
    output = template('templates/index', rows=result)
    return output

@route('/admin')
def admin():
    #result = lib.db.q("SELECT * FROM Page")
    q = lib.db.Page.all()
    result = [[p.url, p.title] for p in q.run()]
    output = template('templates/admin', rows=result)
    return output

@route('/show/:name')
def show(name):
    q = lib.db.Page.gql("WHERE url = :1", name)
    p = q.get()
    title = p.title
    content = addLineBreaks(p.content)
    return template('templates/show_page.tpl', title=title, body=content)
    #content = convertList(lst)

@route('/new', method='GET')
def new():
    return template('templates/new_page.tpl')

@route('/new', method='POST')
def new_post():
    if request.POST.get('save','').strip():
        title = request.POST.get('title', '').strip()
        data = request.POST.get('data', '').strip()
        url = lib.db.getUrlString()
        lib.db.Page(title=title, content=data, url=url).put()

        message =  '<p>The new task was inserted into the database, \
            the ID is %s</p><p><a href="/edit/%s">Edit</a></p><p><a \
            href="/show/%s">Show</a></p>' % (url, url, url)

        return template('templates/submit.tpl', body=message, data=addLineBreaks(data), title=title)


@route('/edit/:name', method='GET')
def edit(name):
    q = lib.db.Page.gql("WHERE url = :1", name)
    p = q.get()
    title = p.title
    content = p.content
    #lib.db.d(p)
    return template('templates/edit_page.tpl', name=name, body=content, url=name, title=title)

@route('/edit/:name', method='POST')
def edit_post(name):
    if request.POST.get('save','').strip():
        title = request.POST.get('title', '').strip()
        data = request.POST.get('data', '').strip()
        url = request.POST.get('url', '').strip()

        q = lib.db.Page.gql("WHERE url = :1", name)
        p = q.get()
        lib.db.d(p)

        if url == name:
            message = '<p>The ID %s was successfully updated</p><p><a href="/edit/%s">Edit</a></p><p><a href="/show/%s">Show</a></p>' % (url, url, url)
            #lib.db.q('UPDATE Page SET url = ?, data = ? WHERE url = :1', url)
        else:
            message =  '<p>The new task was inserted into the database, the ID is %s</p><p><a href="/edit/%s">Edit</a></p><p><a href="/show/%s">Show</a></p>' % (url, url, url) 
            #lib.db.Page(title=title, content=data, url=url).put()

        lib.db.Page(title=title, content=data, url=url).put()

        return template('templates/submit.tpl', body=message, data=addLineBreaks(data), title=title)

@route('/help')
def help():
    static_file('help.html', root='.')

@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='static')

@route('/json:json#[1-9]+#')
def show_json(json):

    conn = sqlite3.connect('math.db')
    c = conn.cursor()
    c.execute("SELECT data FROM paste WHERE id LIKE ?", (json))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task':'This item number does not exist!'}
    else:
        return {'Task': result[0]}
 
def main():
    debug(True)
    run_wsgi_app(bottle.default_app())
 
@error(403)
def Error403(code):
    return 'Get your codes right dude, you caused some error!'
 
@error(404)
def Error404(code):
    return 'Stop cowboy, what are you trying to find?'
 
if __name__=="__main__":
    main()