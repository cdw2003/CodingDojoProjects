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
		label{
			display: inline-block;
			margin: 15px;
		}
	</style>
	<body>
		<c:forEach items="${errors}" var="error">
			<h2><c:out value="${error.getDefaultMessage()}"/></h2>
		</c:forEach>
		<h4><a href = "/dashboard">Dashboard</a></h4>
		<form:form method="POST" action="/songs/new" modelAttribute="song">
    		<form:label path="name">Title
   			 	<form:errors path="name"/>
    			<form:input path="name"/>
    		</form:label>
    		<form:label path="artist">Artist
    			<form:errors path="artist"/>
    			<form:textarea path="artist"/>
    		</form:label>
   			<form:label path="rating">Rating(1-10)
   				 <form:select path="rating">
    				<form:option value = "1" />
    				<form:option value = "2" />
    				<form:option value = "3" />
    				<form:option value = "4" />
    				<form:option value = "5" />
    				<form:option value = "6" />
    				<form:option value = "7" />
    				<form:option value = "8" />
    				<form:option value = "9" />
    				<form:option value = "10" />
				 </form:select>
   				 <form:errors path="rating"></form:errors>
   			</form:label>
    		<input type="submit" value="Add Song"/>
		</form:form>
	</body>