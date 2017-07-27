package com.cheryl.dojoninjas.controllers;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import com.cheryl.dojoninjas.models.Dojo;
import com.cheryl.dojoninjas.models.Ninja;
import com.cheryl.dojoninjas.services.DojoService;
import com.cheryl.dojoninjas.services.NinjaService;

@Controller
@RequestMapping("/")
public class DojoNinjaController {
	
	private DojoService dojoService;
	private NinjaService ninjaService;
	
	public DojoNinjaController(DojoService dojoService, NinjaService ninjaService){
		this.dojoService = dojoService;
		this.ninjaService = ninjaService;
	}

	@RequestMapping("")
	public String index(@ModelAttribute("dojo") Dojo dojo){
		return "dojo.jsp";
	}
	
	@PostMapping("/dojo/new")
	public String create(@Valid @ModelAttribute("dojo") Dojo dojo, BindingResult result, RedirectAttributes flash){
		if(result.hasErrors()){
			flash.addFlashAttribute("errors", result.getAllErrors());
			return "redirect:/";
		}else{
			dojoService.create(dojo);
			return "redirect:/ninja/new";
		}
	}
	
	@RequestMapping("/ninja/new")
	public String newNinja(@ModelAttribute("ninja") Ninja ninja, Model model){
		model.addAttribute("dojos", dojoService.all());
		return "ninja.jsp";
	}
	
	@PostMapping("/ninja/new")
	public String createNinja(@Valid @ModelAttribute("ninja") Ninja ninja, BindingResult result, RedirectAttributes flash){
		if(result.hasErrors()){
			flash.addFlashAttribute("errors", result.getAllErrors());
			return "redirect:/ninja/new";
		}else{
			String id = (String) result.getFieldValue("dojo.id");
			ninjaService.create(ninja);
			return "redirect:/dojo/" + id;
		}
	}
	
	@RequestMapping("/dojo/{id}")
	public String findById(@PathVariable("id") Long id, Model model) {
	    model.addAttribute("dojo", dojoService.findById(id));
	    return "location.jsp";
	}
}
