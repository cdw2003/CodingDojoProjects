package com.cheryl.licenses.services;

import java.util.List;
import org.springframework.stereotype.Service;
import com.cheryl.licenses.models.Person;
import com.cheryl.licenses.repositories.PersonRepository;

@Service
public class PersonService {
	private final PersonRepository personRepository;
	
	public PersonService(PersonRepository personRepository){
		this.personRepository = personRepository;
	}
	
	public void create(Person person){
		personRepository.save(person);
	}
	
	public List<Person> all(){
		return (List<Person>) personRepository.findAll();
	}
	
	public Person findById(Long id){
		return personRepository.findOne(id);
	}
}