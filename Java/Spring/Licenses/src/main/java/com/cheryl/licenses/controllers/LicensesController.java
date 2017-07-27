package com.cheryl.licenses.controllers;

import java.text.SimpleDateFormat;
import java.util.Date;

import javax.validation.Valid;

import org.springframework.beans.propertyeditors.CustomDateEditor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.InitBinder;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import com.cheryl.licenses.services.LicenseService;
import com.cheryl.licenses.services.PersonService;
import com.cheryl.licenses.models.Person;
import com.cheryl.licenses.models.License;

@Controller
@RequestMapping("/")
public class LicensesController {

	private PersonService personService;
	private LicenseService licenseService;

	public LicensesController(PersonService personService, LicenseService licenseService){
		this.personService = personService;
		this.licenseService = licenseService;
	}
	
	@RequestMapping("")
	public String index(@ModelAttribute("person") Person person){
		return "person.jsp";
	}
	
	@PostMapping("/person/new")
	public String create(@Valid @ModelAttribute("person") Person person, BindingResult result, RedirectAttributes flash){
		if(result.hasErrors()){
			flash.addFlashAttribute("errors", result.getAllErrors());
			return "redirect:/";
		}else{
			personService.create(person);
			return "redirect:/license/new";
		}
	}
	@InitBinder
	public void initBinder(WebDataBinder binder) {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyy-MM-dd");
        binder.registerCustomEditor(Date.class, new CustomDateEditor(dateFormat, true));
    }
	
	@RequestMapping("/license/new")
	public String newLicense(@ModelAttribute("license") License license, Model model){
		model.addAttribute("persons", personService.all());
		return "license.jsp";
	}
	
	@PostMapping("/license/new")
	public String createLicense(@Valid @ModelAttribute("license") License license, BindingResult result, RedirectAttributes flash){
		if(result.hasErrors()){
			flash.addFlashAttribute("errors", result.getAllErrors());
			return "redirect:/license/new";
		}else{
			String id = (String) result.getFieldValue("person.id");
			String number = String.format("%06d", Integer.parseInt(id));
			license.setNumber(number);
			licenseService.create(license);
			return "redirect:/person/" + id;
		}
	}
	
	@RequestMapping("/person/{id}")
	public String findById(@PathVariable("id") Long id, Model model) {
	    model.addAttribute("person", personService.findById(id));
	    return "details.jsp";
	}
}
