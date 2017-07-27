<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>

<!DOCTYPE HTML>
<html>
	<head>
		<Title>Dojo Ninjas</Title>
	</head>
	<body>
		<h2>New Dojo</h2>
		<form:form method="POST" action="/dojo/new" modelAttribute="dojo">
			<form:label path="name">Name
   			 	<form:errors path="name"/>
    			<form:input path="name"/><br>
    		</form:label>
			<input type="submit" value="Create"/>
		</form:form>	
	</body>
</html>