<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<!DOCTYPE HTML>
<html>
	<head>
		<title>Lookify</title>
	</head>
	<body>
		<div id = "topnav">
			<h3>Top Ten Songs</h3>
			<h3><a href = "/dashboard">Dashboard</a></h3>
		</div>
		<div id = "topten">
			<c:forEach var="song" items="${songs}" varStatus = "loop">
         	  <h3><c:out value = "${song.rating}"/>-<a href="/songs/${song.id}"><c:out value="${song.name}"/>-<c:out value = "${song.artist}"/></a></h3>  	
      		</c:forEach>
		</div>
	</body>
</html>