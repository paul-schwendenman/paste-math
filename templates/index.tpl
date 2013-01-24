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
  <td><a href="show/{{row[0]}}">show</a></td>
  </tr>
%end
</table>

%rebase templates/layout_user