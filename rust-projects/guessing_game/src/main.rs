use std::io; // the io library comes from the standard library
use rand::Rng; 
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!"); 
    // macro that prints a string to the screen
   
    println!("Please input your guess.");
    let mut guess = String::new();
    // in rust, variables are immutable by default, 
    // and therefore the value will not change when fed in
    
    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");
    println!("You guessed: {guess}");
}


