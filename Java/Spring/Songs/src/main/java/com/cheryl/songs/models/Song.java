package com.cheryl.songs.models;

import java.util.Date;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.PrePersist;
import javax.persistence.PreUpdate;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import org.springframework.format.annotation.DateTimeFormat;

@Entity
public class Song {
	@Id
	@GeneratedValue
	private Long id;
	
	@Column
	@Size(min=5, message = "Name must be at least 5 characters.")
	private String name;
	
	@Column
	@Size(min=5, message = "Artist name must be at least 5 characters.")
	private String artist;
	
	@Column
	@NotNull
	private int rating;
	
	@Column
	@DateTimeFormat(pattern = "MM/dd/yyyy  HH:mm:ss")
	private Date created_at;
	
	@Column
	@DateTimeFormat(pattern = "MM/dd/yyyy  HH:mm:ss")
	private Date updated_at;
	
	@PrePersist
    protected void onCreate(){
            this.created_at = new Date();
    }
	
    @PreUpdate
    protected void onUpdate(){
            this.updated_at = new Date();
	}
    
    public Song(){}
    
    public Song(String name, String artist, int rating, Date created_at, Date updated_at){
    	this.name = name;
    	this.artist = artist;
    	this.rating = rating;
    	this.created_at = created_at;
    	this.updated_at = updated_at;
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

	public String getArtist() {
		return artist;
	}

	public void setArtist(String artist) {
		this.artist = artist;
	}

	public int getRating() {
		return rating;
	}

	public void setRating(int rating) {
		this.rating = rating;
	}

	public Date getCreated_at() {
		return created_at;
	}

	public void setCreated_at(Date created_at) {
		this.created_at = created_at;
	}

	public Date getUpdated_at() {
		return updated_at;
	}

	public void setUpdated_at(Date updated_at) {
		this.updated_at = updated_at;
	}
}
