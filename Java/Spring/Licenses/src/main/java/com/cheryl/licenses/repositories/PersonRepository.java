package com.cheryl.licenses.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import com.cheryl.licenses.models.Person;

@Repository
public interface PersonRepository extends CrudRepository <Person, Long> {
	public Person findOne(Long id);
}
