package com.cheryl.ninjagold.controllers;

import javax.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import java.util.*;

@Controller
@RequestMapping("/")
public class NinjaGoldController {
	ArrayList<String> results = new ArrayList<String>();

	@RequestMapping("")
	public String index(HttpSession session){
		session.getAttribute("gold");
		
		if(session.getAttribute("gold") == null){
			session.setAttribute("gold", 0);
		}
		return "index.jsp";
	}
	
	@SuppressWarnings("unchecked")
	@RequestMapping("/process_money")
	public String points(@RequestParam(value="building") String building, HttpSession session){
		session.setAttribute("building", building);
		Random rand = new Random();
		int gold = 0;
		
		if(session.getAttribute("results") == null){
			session.setAttribute("results", results);
		}
		else{
			results = (ArrayList<String>) session.getAttribute("results");
		}
		
		switch(building){
			case "farm": gold = rand.nextInt(10) + 10;
				results.add("Earned " + gold + " golds from the farm." + "\n");
				break;
				
			case "cave": gold = rand.nextInt(5) + 5;
				results.add("Earned " + gold + " golds from the cave." + "\n");
				break;	
				
			case "house": gold = rand.nextInt(2) + 3;
				results.add("Earned " + gold + " golds from the house." + "\n");
				break;
				
			case "casino": gold = rand.nextInt(50) - 50;
				if(gold > 0){
					results.add("Earned " + gold + " golds from the casino." + "\n");
				}
				else{
					results.add("You went to the casino and lost " + gold + " golds." + "\n");
				}
				break;
			}
			
		session.setAttribute("gold", (Integer) session.getAttribute("gold") + gold);
		session.setAttribute("results", results);
		return "redirect:/";
	}
	
	@RequestMapping("/reset")
	public String clearSession(HttpSession session){ 
		session.invalidate();
		results.clear();
		return "redirect:/";
	}
}
