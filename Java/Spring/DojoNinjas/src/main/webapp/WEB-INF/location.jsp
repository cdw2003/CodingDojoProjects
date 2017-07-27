<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE HTML>
<html>
	<head>
		<Title>Dojo Ninjas</Title>
	</head>
	<body>
		<table>
			<tr>
				<th>First Name</th>
				<th>Last Name</th>
				<th>Age</th>
			</tr>
			<c:forEach var="ninja" items="${dojo.ninjas}" varStatus = "loop">
			<tr>
	         	<td><c:out value="${ninja.firstName}"/></td>
	         	<td><c:out value = "${ninja.lastName}"/></td>
	         	<td><c:out value = "${ninja.age}"/></td>   
	         </tr>
      		</c:forEach>
		</table>
	</body>
</html>