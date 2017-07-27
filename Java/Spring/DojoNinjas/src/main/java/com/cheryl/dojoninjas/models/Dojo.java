package com.cheryl.dojoninjas.models;

import java.util.Date;
import java.util.List;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.PrePersist;
import javax.persistence.PreUpdate;
import javax.persistence.Table;
import org.springframework.format.annotation.DateTimeFormat;

@Entity
@Table(name="dojos", schema = "dojoninjas")
public class Dojo {

	@Id
    @GeneratedValue
    private Long id;
	
	@Column
    private String name;
	
	@Column
	@DateTimeFormat(pattern = "MM/dd/yyyy  HH:mm:ss")
    private Date createdAt;
	
	@Column
	@DateTimeFormat(pattern = "MM/dd/yyyy  HH:mm:ss")
    private Date updatedAt;
	
	@PrePersist
    protected void onCreate(){
            this.createdAt = new Date();
    }
	
	@PreUpdate
    protected void onUpdate(){
            this.updatedAt = new Date();
	}
	
    @OneToMany(mappedBy="dojo", fetch = FetchType.LAZY)
    private List<Ninja> ninjas;
    
    public Dojo() {
    }
    
    public Dojo(String name) {
        this.name = name;
        this.createdAt = new Date();
        this.updatedAt = new Date();        
    }
	
    public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Date getCreatedAt() {
		return createdAt;
	}

	public void setCreatedAt(Date createdAt) {
		this.createdAt = createdAt;
	}

	public Date getUpdatedAt() {
		return updatedAt;
	}

	public void setUpdatedAt(Date updatedAt) {
		this.updatedAt = updatedAt;
	}

	public List<Ninja> getNinjas() {
		return ninjas;
	}

	public void setNinjas(List<Ninja> ninjas) {
		this.ninjas = ninjas;
	}
}
