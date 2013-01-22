%#template for the form for a new task
<p>Add a new task to the ToDo list:</p>
<form action="/new" method="POST">
<textarea name="data" cols="80" rows="30">
</textarea>
<br />
<input type="submit" name="save" value="save">
</form>