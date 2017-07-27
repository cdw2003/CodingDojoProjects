package com.cheryl.dojoninjas.services;

import java.util.List;

import org.springframework.stereotype.Service;
import com.cheryl.dojoninjas.models.Dojo;
import com.cheryl.dojoninjas.repositories.DojoRepository;

@Service
public class DojoService {
private final DojoRepository dojoRepository;
	
	public DojoService(DojoRepository dojoRepository){
		this.dojoRepository = dojoRepository;
	}
	
	public void create(Dojo dojo){
		dojoRepository.save(dojo);
	}
	
	public List<Dojo> all(){
		return (List<Dojo>) dojoRepository.findAll();
	}
	
	public Dojo findById(Long id){
		return dojoRepository.findOne(id);
	}
}
