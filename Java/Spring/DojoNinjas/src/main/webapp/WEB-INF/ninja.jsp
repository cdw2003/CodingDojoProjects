<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>

<!DOCTYPE HTML>
<html>
	<head>
		<Title>Dojo Ninjas</Title>
	</head>
	<body>
		<c:forEach items="${errors}" var="error" varStatus="loop">
			<c:out value="${error.getDefaultMessage()}"/>
		</c:forEach>
		<h2>New Ninja</h2>
		<form:form method="POST" action="/ninja/new" modelAttribute="ninja">
			<form:label path="dojo">Dojo:
   				 <form:select path="dojo">
   				 	<c:forEach items="${dojos}" var="dojo">		
    				<form:option value="${dojo.id}">${dojo.name}</form:option>
    				</c:forEach>
				 </form:select><br>
   				 <form:errors path="dojo"></form:errors>
   			</form:label>
			<form:label path="firstName">First Name:
   			 	<form:errors path="firstName"/>
    			<form:input path="firstName"/><br>
    		</form:label>
    		<form:label path="lastName">Last Name:
   			 	<form:errors path="lastName"/>
    			<form:input path="lastName"/><br>
    		</form:label>
    		<form:label path="age">Age:
   			 	<form:errors path="age"/>
    			<form:input path="age"/><br>
    		</form:label>
			<input type="submit" value="Create"/>
		</form:form>
	</body>
</html>