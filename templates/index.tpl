<html>
<head>
<title>paste-math</title>
</head>
<body>

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


</body>
</html>