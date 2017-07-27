<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>

<!DOCTYPE HTML>
<html>
	<head>
		<Title>License</Title>
	</head>
	<body>
		<c:forEach items="${errors}" var="error" varStatus="loop">
			<c:out value="${error.getDefaultMessage()}"/>
		</c:forEach>
		<h2>New License</h2>
		<form:form method="POST" action="/license/new" modelAttribute="license">
			<form:label path="person">Person:
   				 <form:select path="person">
   				 	<c:forEach items="${persons}" var="person">		
    				<form:option value="${person.id}">${person.firstName} ${person.lastName}</form:option>
    				</c:forEach>
				 </form:select><br>
   				 <form:errors path="person"></form:errors>
   			</form:label>
			<form:label path="state">State:
   			 	<form:errors path="state"/>
    			<form:input path="state"/><br>
    		</form:label>
    		<form:label path="expiration_date">Expiration Date:
   			 	<form:errors path="expiration_date"/>
    			<form:input path="expiration_date" type="date"/><br>
    		</form:label>
			<input type="submit" value="Create"/>
		</form:form>
	</body>
</html>