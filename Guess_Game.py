#!/usr/bin/evn python
# -*- coding: utf-8 -*-

secret = 4

while True != secret:
  guess = int(raw_input("Guess the secret number (between 1 and 30): "))

  if guess == secret:
      print "You guessed it - congratulations! It is number 4 :)"
      break
  else:
      print "Sorry, your guess is not correct... Secret number is not " +str(guess)
