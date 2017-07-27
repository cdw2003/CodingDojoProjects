package com.cheryl.licenses.repositories;

import java.util.ArrayList;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import com.cheryl.licenses.models.License;

@Repository
public interface LicenseRepository extends CrudRepository <License, Long> {
	public License findOne(Long id);
	ArrayList<License> findByPersonIdContaining(long id);
}
