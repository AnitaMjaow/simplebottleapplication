<h1><a href="https://bottlepy.org/">Bottle</a> is a Python Web Framework which is fast, simple and lightweight WSGI micro web-framework for Python. It is distributed as a single file module and has no dependencies other than the Python Standard Library.</h1>
<h2>Edit item with the id {{no}}</h2>

<form action="/edit/{{no}}" method="get">
  <p>Title: </p><input type="text" name="title" value="{{old[0]}}" size="100" maxlength="100">
  <p>Content: </p><input type="text" name="content" value="{{old[1]}}" size="100" maxlength="100">
  <br>
  <input type="submit" name="save" value="save">
</form>

<form action="/delete/{{no}}" method="get">
  <input type="text" name="delete_id" value="{{no}}">
  <input type="submit" name="delete" value="delete">
</form>

