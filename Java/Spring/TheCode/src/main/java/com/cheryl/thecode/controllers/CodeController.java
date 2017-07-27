package com.cheryl.thecode.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping("/")
public class CodeController {

	@RequestMapping("")
    public String index() {
        return "index.jsp";
    }
    
    @RequestMapping("/code")
    public String process(@RequestParam(value = "code") String code, RedirectAttributes redirectAttributes){
    	String bushido = "bushido";
    	
    	if(code.equals(bushido)){
    		return "code.jsp";
    	}
    	else{
    		redirectAttributes.addFlashAttribute("errors", "You must train harder!");
            return "redirect:/";
    	}
    }
}
    
