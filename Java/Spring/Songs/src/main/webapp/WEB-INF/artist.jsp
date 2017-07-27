<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<!DOCTYPE HTML>
<html>
	<head>
		<title>Lookify</title>
	</head>
	<style>
		table{
			margin-left: 25px;
		}
		td, th {
    		border: 1px solid #dddddd;
   			text-align: left;
    		padding: 8px;
		}
		tr:nth-child(even) {
    		background-color: #dddddd;
		}
	</style>
	<body>
		<div id = "links">
			<h3>Songs by artist: <c:out value = "${artist}"/></h3>
			<form action = "/search" method = "post">
				<input type="text" name = "artist"></input>
				<input type="submit" value="New Search"/>
			</form>
			<h3><a href = "/dashboard">Dashboard</a></h3>
		</div>
		<div id = "table">
			<table>
				<tr>
					<th>Name</th>
					<th>Artist</th>
					<th>Rating</th>
					<th>Actions</th>
				</tr>
				<c:forEach var="song" items="${songs}" varStatus = "loop">
				<tr>
	         	  <td><a href="/songs/${song.id}"><c:out value="${song.name}"/></a></td>
	         	  <td><c:out value = "${song.artist}"/></td>
	         	  <td><c:out value = "${song.rating}"/></td>   
	         	  <td><a href = "songs/delete/${song.id}">Delete</a></td>     	
	         	</tr>
	      		</c:forEach>
			</table>
		</div>
	</body>
</html>