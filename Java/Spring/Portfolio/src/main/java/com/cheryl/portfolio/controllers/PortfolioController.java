package com.cheryl.portfolio.controllers;

import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.stereotype.Controller;

@SpringBootApplication
@Controller
@RequestMapping("/")
public class PortfolioController {
	
    public String index() {
        return "forward:/index.html";
	}
	
	@RequestMapping("/myProjects")
    public String projects() {
        return "forward:/projects.html";
	}
	
	@RequestMapping("/aboutMe")
    public String about() {
        return "forward:/about.html";
	}
}


