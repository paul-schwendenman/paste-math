from lib import bottle
from lib.bottle import route, template, request, error, debug, static_file
from google.appengine.ext.webapp.util import run_wsgi_app
from lib.db import Database
from lib.html import convertList

d = Database()

@route('/')
def index():
    result = d.list()
    output = template('templates/index', rows=result)
    return output

@route('/admin')
def admin():
    result = d.list()
    output = template('templates/admin', rows=result)
    return output

@route('/show/:name')
def show(name):
    title, lst = d.load(name)
    content = convertList(lst)
    return template('templates/show_page.tpl', title=title, body=content)

@route('/new', method='GET')
def new():
    return template('templates/new_page.tpl')

@route('/new', method='POST')
def new_post():
    if request.POST.get('save','').strip():
        title = request.POST.get('title', '').strip()
        data = request.POST.get('data', '').strip()

        d.new(title, data)
        return '<p>The new task was inserted into the database, the ID is %s</p><p>Go back to admin: <a href="/admin">here</a></p>'

@route('/edit/:name', method='GET')
def edit(name):
    title, data = d.load(name)
    content = "".join(data)
    return template('templates/edit_page.tpl', name=name, body=content, url=name, title=title)

@route('/edit/:name', method='POST')
def edit_post(name):
    if request.POST.get('save','').strip():
        title = request.POST.get('title', '').strip()
        data = request.POST.get('data', '').strip()
        url = request.POST.get('url', '').strip()

        lst = data.split('\n')
        
        d.save(url, title, lst)

        return '<p>The item number %s was successfully updated</p><p><a href="/show%s">View</a></p><p><a href="/admin">Admin</a></p>' 

@route('/help')
def help():
    static_file('help.html', root='.')

@route('/static/<filename>')
def css(filename):
    static_file(filename, root='.')

@route('/help')
def help():
    static_file('help.html', root='.')

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