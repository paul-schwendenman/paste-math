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

%rebase templates/layout
