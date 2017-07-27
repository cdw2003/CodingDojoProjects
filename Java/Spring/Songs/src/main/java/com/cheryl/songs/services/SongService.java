package com.cheryl.songs.services;

import java.util.ArrayList;
import java.util.List;
import org.springframework.stereotype.Service;
import com.cheryl.songs.models.Song;
import com.cheryl.songs.repositories.SongRepository;

@Service
public class SongService {

	private final SongRepository songRepository;
	public SongService(SongRepository songRepository){
		this.songRepository = songRepository;
	}
	
	public List<Song> getallSongs(){
		return (List<Song>) songRepository.findAll();
	}
	
	public void create(Song song){
		songRepository.save(song);
	}
	
	public void update(Song song){
		songRepository.save(song);
	}
	
	public void destroy(long id) {
		songRepository.delete(id);
	}
	
	public List<Song> all(){
		return (List<Song>) songRepository.findAll();
	}
	
	public Song findById(Long id){
		return songRepository.findOne(id);
	}
	
	public ArrayList<Song> findByArtist(String artist){
		return (ArrayList<Song>) songRepository.findByArtistContaining(artist);
	}
	
	public ArrayList<Song> topTen(){
		ArrayList<Song> songs = (ArrayList<Song>) songRepository.OrderByRatingDesc();
		for(int i=0; i<songs.size(); i++){
			if(i > 10){
				songs.remove(i);
			}
		}
		return songs;
	}
}
