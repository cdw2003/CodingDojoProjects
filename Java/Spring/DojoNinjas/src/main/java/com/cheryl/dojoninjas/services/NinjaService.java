package com.cheryl.dojoninjas.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.cheryl.dojoninjas.models.Ninja;
import com.cheryl.dojoninjas.repositories.NinjaRepository;



@Service
public class NinjaService {
private final NinjaRepository ninjaRepository;
	
	public NinjaService(NinjaRepository ninjaRepository){
		this.ninjaRepository = ninjaRepository;
	}
	
	public void create(Ninja ninja){
		ninjaRepository.save(ninja);
	}
	
	public List<Ninja> all(){
		return (List<Ninja>) ninjaRepository.findAll();
	}
	
	public Ninja findByDojoId(Long id){
		return ninjaRepository.findOne(id);
	}
}