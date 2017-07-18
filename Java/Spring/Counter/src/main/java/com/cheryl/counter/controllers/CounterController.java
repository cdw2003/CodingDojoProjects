package com.cheryl.counter.controllers;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class CounterController {
	@RequestMapping("")
	public String index(HttpSession session){
		Integer count = (Integer) session.getAttribute("count");
		
		if(session.getAttribute("count") == null){
			session.setAttribute("count",1);
			
		}else{
			session.setAttribute("count", count + 1);
			}

		return "index.jsp";
		}
		
	@RequestMapping("/counter")
	public String plusOne(){
		return "counter.jsp";
	}
	
	@RequestMapping("/plustwo")
	public String plusTwo(HttpSession session){
		Integer count = (Integer) session.getAttribute("count");
		
		if(session.getAttribute("count") == null){
			session.setAttribute("count",1);
			
		}else{
			session.setAttribute("count", count + 2);
			}

		return "counter2.jsp";
	}
	
	@RequestMapping("/reset")
	public String clearSession(HttpSession session){ 
		session.invalidate();
		return "redirect:/counter";
	}
}
