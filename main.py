from lib import bottle
from lib.bottle import route, template, request, error, debug, static_file
from google.appengine.ext.webapp.util import run_wsgi_app
import sqlite3
 
@route('/')
def todo_list():
    conn = sqlite3.connect('math.db')
    c = conn.cursor()
    c.execute("SELECT id, url, data FROM paste WHERE status LIKE '1';")
    result = c.fetchall()
    c.close()

    output = template('templates/make_table', rows=result)
    return output

@route('/admin')
def admin_list():
    conn = sqlite3.connect('math.db')
    c = conn.cursor()
    c.execute("SELECT id, url, data FROM paste WHERE status LIKE '1';")
    result = c.fetchall()
    c.close()

    output = template('templates/make_table_with', rows=result)
    return output

@route('/all')
def todo_list_all():
    conn = sqlite3.connect('math.db')
    c = conn.cursor()
    c.execute("SELECT id, url, data, status FROM paste;")
    result = c.fetchall()
    c.close()

    output = template('templates/make_table', rows=result)
    return output


@route('/new', method='GET')
def new_item():
    return template('new_task.tpl')

@route('/new', method='POST')
def new_item():

    if request.POST.get('save','').strip():

        new = request.POST.get('data', '').strip()
        conn = sqlite3.connect('math.db')
        c = conn.cursor()

        c.execute("INSERT INTO paste (url,data,status) VALUES (?,?,?)", ('AAAAA', new,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p><p>Go back to admin: <a href="/admin">here</a></p>' % new_id

    else:
        return template('templates/new_task.tpl')

@route('/edit')
@route('/edit/')
def edit_table():
    conn = sqlite3.connect('math.db')
    c = conn.cursor()
    c.execute("SELECT id, url, data FROM paste WHERE status LIKE '1';")
    result = c.fetchall()
    c.close()

    output = template('templates/edit_table', rows=result)
    return output

@route('/edit/:no', method='GET')
@validate(no=int)
def edit_item(no):
    conn = sqlite3.connect('math.db')
    c = conn.cursor()
    c.execute("SELECT data FROM paste WHERE id LIKE ?", (str(no)))
    cur_data = c.fetchone()

    return template('templates/edit_task', old = cur_data, no = no)
    
@route('/edit/:no', method='POST')
@validate(no=int)
def edit_item(no):
    if request.POST.get('save','').strip():
        url = request.POST.get('url','').strip()
        status = request.POST.get('status','').strip()
        data = request.POST.get('data','').strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('math.db')
        c = conn.cursor()
        c.execute("UPDATE paste SET url = ?, status = ?, data = ? WHERE id LIKE ?", (url,status,data,no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p><p><a href="/show%s">View</a></p><p><a href="/admin">Admin</a></p>' %(no, no)

    else:
        conn = sqlite3.connect('math.db')
        c = conn.cursor()
        c.execute("SELECT data FROM paste WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()

        return template('templates/edit_task', old = cur_data, no = no)

@route('/item:item#[1-9]+#')
def show_item(item):

        conn = sqlite3.connect('math.db')
        c = conn.cursor()
        c.execute("SELECT data FROM paste WHERE id LIKE ?", (item))
        result = c.fetchall()
        c.close()

        if not result:
            return 'This item number does not exist!'
        else:
            return 'Task: %s' %result[0]

@route('/show:item#[1-9]+#')
def show_page(item):

        conn = sqlite3.connect('math.db')
        c = conn.cursor()
        c.execute("SELECT data FROM paste WHERE id LIKE ?", (item))
        result = c.fetchall()
        c.close()

        if not result:
            body =  'This item number does not exist!'
        else:
            body = '%s' % result[0]
        #return template('show', body = body)
        return wrapWebpageSimple(body)

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