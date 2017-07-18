<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
	<head>
	    <title>Counter</title>
	</head>
	<body>
		<h1>Your count went up by two and is now <c:out value="${count}"/></h1>
		<a href="/">Test another visit?</a>
		<a href="/reset">Reset</a>
	</body>
</html>