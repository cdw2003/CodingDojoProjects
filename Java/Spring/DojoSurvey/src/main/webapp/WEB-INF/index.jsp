<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
  <head>
    <title>Dojo Survey</title>
  </head>
  <style>
	  #header{
	    margin: 25px;
	    border: 1px solid black;
	    padding: 20px;
	    width: 600px;
	    margin-left: 300px;
	  }
	  h2{
	    color: blue;
	  }
	  textarea {
	      width: 75%;
	      height: 150px;
	      padding: 12px 20px;
	      border: 2px solid #ccc;
	      border-radius: 4px;
	      background-color: #f8f8f8;
	  }
  </style>
  <body>
    <div id = "header">
      <div id="form">
        <form action="/process" method="POST">
            Your Name: <input class='textbox' type='text' name="name"><br><br>
            Dojo Location: <select class='dropdown' name="location">
              <option value = "DC">Washington, DC</option>
              <option value = "LA">Los Angeles</option>
              <option value = "Dallas">Dallas</option>
              <option value = "Chicago">Chicago</option>
              <option value = "Seattle">Seattle</option>
              <option value = "SF">Silicon Valley</option>
              <option value = "Tulsa">Tulsa</option>
            </select><br><br>
            Favorite Language: <select class='dropdown' name="language">
              <option value = "Python">Python</option>
              <option value = "Java">Java</option>
              <option value = "Ruby">Ruby on Rails</option>
              <option value = "MEAN">MEAN</option>
              <option value = "Swift">iOS Swift</option>
              <option value = "C#">C#</option>
            </select><br><br>
            Comment(optional): <textarea class='textbox' name = "comment">
            </textarea><br><br>
            <input type='submit' value='Submit'>
        </form>
      </div>
    </div>
  </body>
</html>