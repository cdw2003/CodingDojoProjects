package com.cheryl.songs.repositories;

import java.util.ArrayList;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import com.cheryl.songs.models.Song;

@Repository
public interface SongRepository extends CrudRepository <Song, Long>{
	
	public ArrayList<Song> findByArtistContaining(String artist);
	public Song findOne(Long id);
	public ArrayList<Song> OrderByRatingDesc();
}
