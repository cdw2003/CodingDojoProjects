package com.cheryl.dojoninjas.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import com.cheryl.dojoninjas.models.Ninja;

@Repository
public interface NinjaRepository extends CrudRepository <Ninja, Long>{
	public Ninja findOne(Long id);
}
