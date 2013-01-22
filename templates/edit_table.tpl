%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
  <tr>
  <td><a href="edit/{{row[0]}}">{{row[0]}}</a></td>
  %for col in row[1:]:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>