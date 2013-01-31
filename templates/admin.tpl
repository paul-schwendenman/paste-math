<h1>Pages</h1>
<table border="1">
  <tr>
    <th>Url</th>
    <th>Title</th>
  </th>
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  <td><a href="edit/{{row[0]}}">edit</a></td>
  <td><a href="show/{{row[0]}}">show</a></td>
  <td><a href="view/{{row[0]}}">view</a></td>
  </tr>
%end
</table>
<div id="fixed">
	<a href="/new">New</a>
	<a href="{{users.create_logout_url("/")}}">sign out</a>
</div>
<p>
<ul>
<li><p>Edit</p>
<p>Edit the page</p></li>
<li><p>Show</p>
<p>Show the processed page</p></li>
<li><p>View</p>
<p>View the raw content of the page</p></li>
</ul>
</p>

<div id="todo">
<h1>Todo</h1>
<table border="1">
  <tr>
    <th>Title</th>
    <th>Status</th>
  </th>
%for row in todo:
  <tr>
    <td>{{row.title}}</td>
%if row.open:
    <td>Open</td>
%else:
    <td>Closed</td>
%end
  </tr>
%end
</table>

<p>Add a new task to the ToDo list:</p>
<form action="/todo" method="POST">
Title: <br>
<input type="text" name="title"><br>
Body: <br>
<textarea name="data" cols="25" rows="5">
</textarea>
<br />
<input type="submit" name="save" value="save">
</form>

</div>

%rebase templates/layout
