<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
	<head>
		<title>The Code</title>
	</head>
	<body>
		<h2 style = "color: red;">${errors}</h2>
		<h3>What is the code?</h3>
		 <form action="/code" method="post">
          <input class='textbox' type='text' name="code">
          <input class = "button" type="submit" value="Try Code">
         </form>
	</body>
</html>