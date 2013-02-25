<div id="todo">
<h1><a href="/todo">Todo</a></h1>

%if message:
{{!message}}
%end

%if solo:
<table border="1">
  <tr>
    <th>Title</th>
    <th>Status</th>
    <th>Creator</th>
  </th>
%for row in todo:
  <tr>
    <td>{{row.title}}</td>
%if row.open:
    <td>Open</td>
%else:
    <td>Closed</td>
%end
    <td>{{row.creator.nickname()}}</td>
  </tr>
%end
</table>
<div id="fixed">
	<a href="/">Home</a>
</div>
%end

<p>Add a new task to the todo list:</p>
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

%if solo:
%rebase templates/layout
%end
