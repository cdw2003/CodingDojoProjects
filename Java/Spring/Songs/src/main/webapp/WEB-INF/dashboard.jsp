<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE HTML>
<html>
	<head>
		<Title>Lookify</Title>
	</head>
	<style>
		#links h3, form{
			display: inline-block;
			padding: 15px;
		}
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
			<h3><a href = "/songs/new">Add New</a></h3>
			<h3><a href = "/songs/top">Top Songs</a></h3>
			<form action = "/search" method = "post">
				<input type="text" name="artist"></input>
				<input type="submit" value="Search Artists"></input>
			</form>
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