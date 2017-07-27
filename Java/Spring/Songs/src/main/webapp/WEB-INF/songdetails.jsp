<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<!DOCTYPE HTML>
<html>
	<head>
		<title>Lookify</title>
	</head>
	<style>
		#labels{
			display: inline-block;
			font-size: 20px;
			font-weight: bold;
		}
		#details{
			display: inline-block;
			margin-left: 25px;
			font-size: 18px;
			font-weight: light;
		}
	</style>
	<body>
		<h3><a href = "/dashboard">Dashboard</a></h3>
		<div id = "labels">
			<h2>Title:</h2>
			<h2>Artist:</h2>
			<h2>Rating (1-10):</h2>
		</div>
		<div id = "details">
			<h2><c:out value = "${song.name}"/></h2>
			<h2><c:out value = "${song.artist}"/></h2>
			<h2><c:out value = "${song.rating}"/></h2>
			<h2></h2>
		</div>
	</body>
</html>