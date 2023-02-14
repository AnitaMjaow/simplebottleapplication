<h1>CRUD (CREATE READ UPDATE DELETE) applications can be created with different programming languages and frameworks.</h1>
<h2>This basic example is created with Python's framework <a href="https://bottlepy.org/docs/dev/tutorial_app.html">Bottle</a>, please follow the instructions over there.</h2>
<h3>This is a great CRUD + Python + database base-template to play around, learn and experiment with in your local environment. <i>Feel free to use or modify</i>.</h3>

<p>Minor changes has been made on Bottle's example for easier audit.</p>

<h3><a href="/new">Create new item</a></h3>
<table border>
  <tr>
  %for id,title,content in rows:
    <td><h5><a href="/item/{{id}}">{{title}}</a></h5><p>{{content}}</p></td>
  %end
  </tr>
</table>


<footer>
<a href="https://www.catfeewebdev.se/">www.catfeewebdev.se</a><br><a href="https://www.catfeewebdev.se/"><img src="https://usercontent.one/wp/www.catfeewebdev.se/wp-content/uploads/2022/02/catfeeroundlogo-300x300.png?media=1644628358" width="100",height="100"></a></p>
</footer>
<style>
tr {
  display: flex;
  flex-direction: column;
}
footer{
  text-align: center;
}
</style>