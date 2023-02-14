import sqlite3
from bottle import route, run, template, request

@route('/')
def list():
    # this will connect and prepare the database to be used.
    conn = sqlite3.connect('simple-database.db')
    c = conn.cursor()
    c.execute("SELECT id, title, content FROM item")
    result = c.fetchall()
    c.close()
    return template('index', rows=result)


@ route('/new', method='GET')
def new_item():
    if request.GET.save:
        # fetching title and content from the inputfields in the index.tpl file.
        new_title = request.GET.title.strip()
        new_content = request.GET.content.strip()
        # this will connect and prepare the database to be used.
        conn = sqlite3.connect('simple-database.db')
        c = conn.cursor()
        # storing the new data/item and assign an id it.
        c.execute("INSERT INTO item (title, content) VALUES (?,?)",
                  (new_title, new_content))
        new_id = c.lastrowid

        conn.commit()
        c.close()
        # This returns a message after submission, in other cases continue.
        return '<p>Item %s has been created<br> <a href="/">Back</a></p>' % new_id
    else:
        return template('new_item.tpl')


# this route uses the Bottle's dynamic routing wildcard filtering behavior.
@ route('/edit/<no:int>', method='GET')
def edit_item(no):
    # fetching id, title and content from the inputfields in the edit_item.tpl file.
    if request.GET.save:
        edit_title = request.GET.title.strip()
        edit_content = request.GET.content.strip()
        # this will connect and prepare the database to be used.
        conn = sqlite3.connect('simple-database.db')
        c = conn.cursor()
        # updates and stores the new data where the old data once was.
        c.execute(
            "UPDATE item SET title = ?, content = ? WHERE id LIKE ?", (edit_title, edit_content, no))
        conn.commit()
        c.close()
        # This returns a message after submission, in other cases continue.
        return '<p>Item %s has been updated <br> <a href="/">Back</a></p>' % no
    else:
        # this will connect and prepare the database to be used.
        conn = sqlite3.connect('simple-database.db')
        c = conn.cursor()
        # fetch id to be shown in edit_item.tpl file.
        c.execute(
            "SELECT id, content FROM item WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()
        return template('edit_item', old=cur_data, no=no)

# this route uses the Bottle's dynamic routing wildcard filtering behavior.
@ route('/delete/<no:int>', method='GET')
def delete_item(no):
    # fetching id, title and content from the inputfields in the edit_item.tpl file.
    if request.GET.delete:
        no = request.GET.delete_id.strip()
        # this will connect and prepare the database to be used.
        conn = sqlite3.connect('simple-database.db')
        c = conn.cursor()
        c.execute(
            "DELETE FROM item WHERE id LIKE ?", (no))
        conn.commit()
        # This returns a message with a back button.
        return '<p>Item %s has been deleted <br><a href="/">Back</a></p>' % no


@route('/item/<item:re:[0-9]+>')
def show_item(item):
    # this will connect and prepare the database to be used.
    conn = sqlite3.connect('simple-database.db')
    c = conn.cursor()
    c.execute(
        "SELECT title, content, id FROM item WHERE id LIKE ?", (item,))
    result = c.fetchall()
    c.close()
    # error handling
    if not result:
        return 'This item does not exist'
    else:
        # This returns a message with item data and a back button.
        return '<h1> Title: %s </h1> <br> <h2>Content: %s </h2> <br> <a href="/edit/%s">Edit</a> <br> <a href="/">Back</a>' % result[0]



run(reloader=True, debug=True)
