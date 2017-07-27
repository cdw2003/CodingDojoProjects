package com.cheryl.licenses.services;

import java.util.List;
import org.springframework.stereotype.Service;
import com.cheryl.licenses.repositories.LicenseRepository;
import com.cheryl.licenses.models.License;

@Service
public class LicenseService {
	private final LicenseRepository licenseRepository;
	
	public LicenseService(LicenseRepository licenseRepository){
		this.licenseRepository = licenseRepository;
	}
	
	public void create(License license){
		licenseRepository.save(license);
	}
	
	public List<License> all(){
		return (List<License>) licenseRepository.findAll();
	}
	
	public License findByPersonId(Long id){
		return licenseRepository.findOne(id);
	}
}
