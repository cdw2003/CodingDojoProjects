package com.cheryl.dojoninjas.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import com.cheryl.dojoninjas.models.Dojo;

@Repository
public interface DojoRepository extends CrudRepository <Dojo, Long>{
	public Dojo findOne(Long id);
}
