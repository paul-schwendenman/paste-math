<h1>Pages</h1>

%if len(rows)>0:
<table border="1">
  <tr>
    <th>Url</th>
    <th>Title</th>
    <th>Published</th>
%if not grade:
    <th>Grade</th>
%end
    <th colspan="3"></th>
  </th>
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  <td><a href="/edit/{{row[0]}}">edit</a></td>
  <td><a href="/show/{{row[0]}}">show</a></td>
  <td><a href="/view/{{row[0]}}">view</a></td>
  </tr>
%end
</table>
%else:
<p>No pages currently exist</p>
%end
<div id="fixed">
%if grade:
	<a href="/">Home</a>
%end
	<a href="/new">New</a>
	<a href="{{users.create_logout_url("/")}}">sign out</a>
</div>
<!--
<p>
<ul>
<li><p>Edit</p>
<p>Edit the page</p></li>
<li><p>Show</p>
<p>Show the processed page</p></li>
<li><p>View</p>
<p>View the raw content of the page</p></li>
</ul>
</p>
-->
%if not grade:
<div id="grades">
%for each_grade in (7, 8, 9, 10, 11, 12):
<div id="grade{{each_grade}}">
<h2><a href="/grade/{{each_grade}}">Grade {{each_grade}}</a></h2>
% grade_page = [item for item in rows if item[-1] == each_grade]
%if len(grade_page)>0:
<table border="1">
  <tr>
    <th>Url</th>
    <th>Title</th>
    <th>Published</th>
    <th colspan="3"></th>
  </th>
%for row in grade_page:
  <tr>
  %for col in row[:-1]:
    <td>{{col}}</td>
  %end
  <td><a href="/edit/{{row[0]}}">edit</a></td>
  <td><a href="/show/{{row[0]}}">show</a></td>
  </tr>
%end
</table>
%else:
<p>No pages exist</p>
%end
</div>
%end
</div>
%end
%if todo:
%include templates/todo todo=todo,solo=False,message=None
%end

%rebase templates/layout
