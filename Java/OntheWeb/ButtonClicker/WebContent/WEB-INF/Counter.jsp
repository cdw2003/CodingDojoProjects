<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
		<title>Button Clicker</title>
	</head>
	<body>
	    <form action ='/ButtonClicker/counter' name ="count" method="get">
	      <input type = "submit" value = "Click Me">
	    </form>
   		<p>You clicked this button <c:out value="${count}"/> times</p>
	</body>
</html>