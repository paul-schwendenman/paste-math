<html>
<head>
<title>paste-bin</title>
</head>
<body>
<p>Add a new task to the ToDo list:</p>
<form action="/edit/{{name}}" method="POST">
Title: <br>
<input type="text" name="title" value="{{title}}"><br>
Body: <br>
<textarea name="data" cols="80" rows="30">
{{body}}
</textarea>
<br />
URL: <br>
<input type="text" name="url" value="{{url}}"><br>

<input type="submit" name="save" value="save">
</form>
</body>
</html>
