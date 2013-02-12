<!DOCTYPE html>
<html>
<head>
<title>paste-math</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<link rel="icon" href="/icon.ico" />
<link rel="stylesheet" href="/static/main.css" type="text/css" />

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    showProcessingMessages: false,
    tex2jax: { inlineMath: [['$','$'],['\\(','\\)']] }
  });
</script>
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/javascript" src="/static/live_preview.js"></script>
</head>
<body>
<div id="body">
<div id="content">
<form action="/new" method="POST">
Title: <br>
<input type="text" name="title"><br>
Body: <br>
<textarea name="data" id="data" cols="80" rows="20" style="margin-top:5px">
</textarea><br>
<br/><br/>
<button type="button" onclick="Preview.Update()">preview</button>

<input type="submit" name="save" value="save" alt="Save as draft"/>
<input type="submit" name="publish" value="publish" alt="Publish"/>
</form>
<br/><br/>
Preview:
<div class="preview">
<h2 class="title"></h2>
<div id="preview"></div>
<div id="buffer" style="visibility:hidden; position:absolute; top:0; left: 0;"><div>
</div>

<script>
Preview.Init();
</script>
</div>
</div>
</body>
</html>
