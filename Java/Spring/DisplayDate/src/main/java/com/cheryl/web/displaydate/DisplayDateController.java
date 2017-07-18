package com.cheryl.web.displaydate;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import java.text.*;


@SpringBootApplication
@Controller
@RequestMapping("/")
public class DisplayDateController {
	@RequestMapping("")
	 public String index() {
	     return "index.jsp";
	}   
	
	@RequestMapping("/date")
	 public String getDate(Model model) {
		SimpleDateFormat dateformat = new SimpleDateFormat("EEEE, 'the' dd 'of' MMMM, yyyy");
		java.util.Date currDate = new java.util.Date();
		String date = dateformat.format(currDate);
		model.addAttribute("date", date);
	    return "date.jsp";
	}   
	
	@RequestMapping("/time")
	 public String getTime(Model model) {
		SimpleDateFormat timeformat = new SimpleDateFormat("h:m a");
		java.util.Date currTime = new java.util.Date();
		String time = timeformat.format(currTime);
		model.addAttribute("time", time);
	    return "time.jsp";
	}   	     
}
