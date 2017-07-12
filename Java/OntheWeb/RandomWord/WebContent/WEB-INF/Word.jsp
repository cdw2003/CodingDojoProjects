<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
		<title>Random Word Generator</title>
	</head>
	<style>
	*{
		font-family: sans-serif;
		text-align: center;
	}
	.container{
		width: 500px;
		margin: auto;
	}
	</style>
	<body>
		<div class=container>
			<fieldset>
				<h3>You generated a word <c:out value="${count}"/> times</h3>
				<div id = "random">
					<c:out value="${word}"/>
				</div>
				<form action ='/RandomWord/word' name ="count" method="get">
			      <input type = "submit" value = "Generate">
			    </form>
		   		<h3>The last time you generated a word was:</h3>
		   		<div id = "time">
		   			<c:out value="${time}"/>
				</div>
			</fieldset>
		</div>
	</body>
</html>