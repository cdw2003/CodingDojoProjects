<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
	<head>
	    <title>Counter</title>
	</head>
	<body>
		<h1>You have visited <a href="/">your server</a> <c:out value="${count}"/> times.</h1>
		<a href="/">Test another visit?</a>
		<a href="/reset">Reset</a>
		<a href="/plustwo">Count by Two</a>
	</body>
</html>