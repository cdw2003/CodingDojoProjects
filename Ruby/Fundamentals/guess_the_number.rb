def guess_number guess
  number = 25
  case guess
  when guess = number
    puts "You got it"
  when guess > number
    puts "Guess was too high"
  else
    puts "Guess was too low"
  end
end
guess_number 25
guess_number 20
guess_number 35
