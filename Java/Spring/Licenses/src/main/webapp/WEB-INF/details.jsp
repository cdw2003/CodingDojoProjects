<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>

<!DOCTYPE HTML>
<html>
	<head>
		<title>License</title>
	</head>
	<body>
		<h2><c:out value = "${person.firstName}"/> <c:out value = "${person.lastName}"/></h2><br>
		<p>License Number: <c:out value = "${person.license.getNumber()}"/></p><br>
		<p>State: <c:out value = "${person.license.getState()}"/></p><br>
		<p>Expiration Date: <fmt:formatDate pattern="MM-dd-yyyy" value = "${person.license.getExpiration_date()}"/></p>
	</body>
</html>