<html>
<head>
<title>paste-bin</title>
</head>
<body>
<p>Add a new task to the ToDo list:</p>
<form action="/new" method="POST">
Title: <br>
<input type="text" name="title"><br>
Body: <br>
<textarea name="data" cols="80" rows="30">
</textarea>
<br />
<input type="submit" name="save" value="save">
</form>
</body>
</html>
