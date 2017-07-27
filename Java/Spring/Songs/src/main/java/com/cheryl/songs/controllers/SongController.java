package com.cheryl.songs.controllers;

import javax.validation.Valid;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import com.cheryl.songs.services.SongService;
import com.cheryl.songs.models.Song;

@Controller
@RequestMapping("/")
public class SongController {

	private final SongService songService;
	public SongController(SongService songService){
		this.songService = songService;
	}
	
	@RequestMapping("")
	public String index(){
		return "index.jsp";
	}
	
	@RequestMapping("/dashboard")
	public String dashboard(Model model){
		model.addAttribute("songs", songService.all());
		return "dashboard.jsp";
	}
	
	@RequestMapping("/songs/{id}")
	public String songs(@PathVariable("id") long id, Model model){
		model.addAttribute("song", songService.findById(id));
		return "songdetails.jsp";
	}
	
	@RequestMapping("songs/new")
	public String newSong(Model model){
		model.addAttribute("song", new Song());
		return "newsong.jsp";
	}
	
	@PostMapping("songs/new")
	public String create(@Valid @ModelAttribute("song") Song song, BindingResult result, RedirectAttributes flash){
		if(result.hasErrors()){
			flash.addFlashAttribute("errors", result.getAllErrors());
		}else{
			songService.create(song);
		}
		return "redirect:/dashboard";
	}
	
	@RequestMapping("/songs/delete/{id}")
	public String destroy(@PathVariable("id") Long id){
		songService.destroy(id);
		return "redirect:/dashboard";
	}
	
	@PostMapping("/search")
	public String search(@RequestParam(value="artist") String artist, Model model){
		model.addAttribute("songs", songService.findByArtist(artist));
		return "artist.jsp";
	}
	
	@RequestMapping("/songs/top")
	public String topTen(Model model){
		model.addAttribute("songs", songService.topTen());
		return "topsongs.jsp";
	}
}
