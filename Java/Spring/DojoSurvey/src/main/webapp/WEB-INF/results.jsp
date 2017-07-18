<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
    <head>
      <title>Dojo Survey</title>
      <style>
        #contentbox{
          margin: 25px;
          border: 1px solid black;
          padding: 20px;
          width: 500px;
        }
        #labels{
          display: inline-block;
          padding: 15px;
          vertical-align: top;
        }
        #responses{
          display: inline-block;
          padding: 15px;
          vertical-align: top;
        }
        h3{
          background-color: green;
          border: 1px solid black;
          padding: 15px;
          width: 510px;
          margin-left: 25px;
          color: white;
        }
        h4{
          text-decoration: underline;
        }
        a{
          border: 1px solid black;
          background-color: blue;
          color: white;
          text-decoration: none;
          padding: 5px;
        }
      </style>
      <body>
	  	<div id = "contentbox">
	    	<h4>Submitted Information:</h4>
	          <div id="labels">
	            <span>Name:</span><br>
	            <span>Dojo Location:</span><br>
	            <span>Favorite Language:</span><br>
	            <span>Comment:</span>
	          </div>
	          <div id="responses">
	            <span><c:out value="${name}"/></span><br>
	            <span><c:out value="${location}"/></span><br>
	            <span><c:out value="${language}"/></span><br>
	            <span><c:out value="${comment}"/></span>
	          </div>
	          <br><br>
	          <a href = "/">Go Back</a>
	  	</div>
      </body>
</html>