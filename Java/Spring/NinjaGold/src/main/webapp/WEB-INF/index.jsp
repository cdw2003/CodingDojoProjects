<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
  <head>
    <style>
      #header{
        margin: 20px;
      }
      #GoldTally span{
        display: inline-block;
        font-weight: bold;
        vertical-align: top;
      }
      #GoldTally p{
        display: inline-block;
        border: 1px solid black;
        padding: 5px;
        margin-left: 10px;
        width: 100px;
        height: 25px;
        vertical-align: top;
      }
      #boxes form{
        display: inline-block;
        border: 1px solid black;
        background-color: #D3D3D3;
        padding: 25px;
        width: 200px;
        margin: 15px;
      }
      #boxes form h3{
        text-align: center;
        margin-bottom: 5px;
        color: blue;
      }
      #boxes form p{
        text-align: center;
        margin-top: 0px;
        font-size: 14px;
      }
      .button{
        margin-top: 50px;
        position: relative;
        left: 60px;
      }
      .textbox{
        width: 1125px;
        height: 150px;
      }
      #activity_box{
        height: 250px;
        width: 1110px;
        border: 1px solid black;
        margin-left: 15px;
        margin-bottom: 10px;
        overflow: auto;
      }
      #activity_box h4{
        font-weight: bold;
        font-size: 20px;
        margin-left: 20px;
      }
      #activity_box p{
        margin-left: 20px;
      }
    </style>
  </head>
  <body>
    <div id = "header">
      <div id="GoldTally">
        <span>Your Gold:</span>
        <p><c:out value="${gold}"/></p>
      </div>
      <div id = "boxes">
        <form action="/process_money" method="post">
          <h3>Farm</h3><br>
          <p>(earns 10-20 golds)</p>
          <input type = "hidden" name="building" value="farm">
          <input class = "button" type="submit" value="Find Gold!">
        </form>
        <form action="/process_money" method="post">
          <h3>Cave</h3><br>
          <p>(earns 5-10 golds)</p>
          <input type = "hidden" name="building" value="cave">
          <input class = "button" type="submit" value="Find Gold!">
        </form>
        <form action="/process_money" method="post">
          <h3>House</h3><br>
          <p>(earns 2-5 golds)</p>
          <input type = "hidden" name="building" value="house">
          <input class="button" type="submit" value="Find Gold!">
        </form>
        <form action="/process_money" method="post">
          <h3>Casino</h3><br>
          <p>(earns/takes 0-50 golds)</p>
          <input type = "hidden" name="building" value="casino">
          <input class="button" type="submit" value="Find Gold!">
        </form>
      </div>
      <div id = "activity_box">
        <h4>Activities:</h4>
        	<c:forEach items="${results}" var="value">
        		<c:if test="${value.substring(0,6) == 'Earned'}">
    				<p style = "color: green;"><c:out value="${value}"/></p>
    			</c:if>
    			<c:if test="${value.substring(0,3) == 'You'}">
    				<p style = "color: red;"><c:out value="${value}"/></p>
    			</c:if>
    		</c:forEach>	
      </div>
      <form action="/reset" method ="post">
        <input class = "reset" type = "submit" value = "Start Over">
      </form>
    </div>
  </body>
</html>