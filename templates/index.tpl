%if len(rows)>0:
<table border="1">
  <tr>
    <th>Url</th>
    <th>Title</th>
  </tr>
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  <td><a href="/show/{{row[0]}}">show</a></td>
  </tr>
%end
</table>
%else:
<p>No pages currently exist</p>
%end

<div id="fixed">
%if users.get_current_user():
	<a href="{{users.create_logout_url("/")}}">sign out</a>
%else:
	<a href="{{users.create_login_url("/")}}">sign in</a>
%end
</div>

%rebase templates/layout