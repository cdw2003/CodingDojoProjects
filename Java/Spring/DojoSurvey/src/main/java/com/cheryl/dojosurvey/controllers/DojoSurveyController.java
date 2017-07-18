package com.cheryl.dojosurvey.controllers;

import javax.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;  
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping("/")
public class DojoSurveyController {
	@RequestMapping("")
	public String index(){
		return "index.jsp";
	}
	
	@RequestMapping(path="/process", method=RequestMethod.POST)
	public String process(@RequestParam(value="name") String name, @RequestParam(value="location") String location, @RequestParam(value="language") String language, @RequestParam(value="comment", defaultValue = "") String comment, HttpSession session){
		session.setAttribute("name", name);
		session.setAttribute("location", location);
		session.setAttribute("language", language);
		session.setAttribute("comment", comment);
		return "redirect:/result";
    }
	
	@RequestMapping("/result")
	public String results(){
		return "results.jsp";
	}
}
