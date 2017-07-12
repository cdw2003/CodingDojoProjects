package com.cheryl.web;

import java.io.IOException;
import java.util.*;
import java.text.*;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

public class Word extends HttpServlet {
	private static final long serialVersionUID = 1L;
   
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session = request.getSession();
		String count = (String) session.getAttribute("count");
		String word = (String) session.getAttribute("word");
		String time = (String) session.getAttribute("time");
		Integer num=0;

		if(count != null){
			num = Integer.parseInt(count);
			num += 1;
			count = num.toString();
			session.setAttribute("count", count);
		}else{
			session.setAttribute("count", "0");
		}
		
		String letters = "abcdefghijklmnopqrstuvwzyz";
	      ArrayList<Character> random = new ArrayList<Character>();
	      Random rand = new Random();
	      for(int i = 0; i < 15; i++){
	        int randomNum = rand.nextInt(26);
	        random.add(letters.charAt(randomNum));
	      }
	      word = "";
	      for (Character c : random) {
	        word += c;
	      }
	      session.setAttribute("word", word);
	      
	     Date date = new Date();
	     SimpleDateFormat ft = new SimpleDateFormat ("MMMM d, y - h:m:s a");
	     time = ft.format(date).toString();
	     session.setAttribute("time", time);
	     
		RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/Word.jsp");
		view.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}
}
