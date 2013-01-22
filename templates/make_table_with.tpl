%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
  <tr>
  <td><a href="show{{row[0]}}">view</a></td>
  <td><a href="edit/{{row[0]}}">edit</a></td>
  %for col in row[:]:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>

<p>
Make a new page: <a href="/new">here</a>
</p>