package com.cheryl.pets.models;

public class Dog extends Animal{

	public Dog() {
	}
	
	public Dog(String name, String breed, double weight) {
		this.setName(name);
		this.setBreed(breed);
		this.setWeight(weight);
	}
	
	@Override
	public String showAffection(){
		if(this.getWeight()>=30){
			return this.getName()+" curled up next to you.";
		}
		else if(this.getWeight()<30){
			return this.getName()+" hopped into your lap.";
		}
		return "You have a very unhappy dog.";
	}
}
