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
  </tr>
%end
</table>
<div id="fixed">
	<a href="/new">New</a>
	<a href="{{users.create_logout_url("/")}}">sign out</a>
</div>
%rebase templates/layout_admin
