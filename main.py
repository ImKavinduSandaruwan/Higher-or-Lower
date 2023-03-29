#Coded by Kavindu sandaruwan.
import random
from game_data import data
from art import logo, vs
from replit import clear

#Checking user win or not using a function
def check_answer(guess,account_a_followers,account_b_followers):
  if account_a_followers > account_b_followers:
    if guess == "a":
      return True
    else:
      return False
  elif account_b_followers > account_a_followers:
    if guess == "b":
      return True
    else:
      return False

#creating a function for formatting data
def format(account):
  """formatting account data printable"""
  account_name = account["name"]
  account_discr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_discr}, from {account_country}"


score = 0
is_continue_game = True
account_b = random.choice(data)

#repeting game
while is_continue_game:
  print(logo)
  #Generating random account
  account_a = account_b
  account_b = random.choice(data)
  #if account a and b are same it will generate another account for b
  if account_a == account_b:
    account_b = random.choice(data)
  
  #printing formated data
  print(f"Compare A: {format(account_a)}")
  print(vs)
  print(f"Compare B: {format(account_b)}")
  
  #Taking user input
  guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
  
  #Checking win or not
  account_a_followers = account_a["follower_count"]
  account_b_followers = account_b["follower_count"]
  
  is_correct = check_answer(guess,account_a_followers,account_b_followers)
  clear()
  #Give score if its correct
  if is_correct:
    score += 1
    print(f"You're correct. Current score {score}.")
  else:
    is_continue_game = False
    print(f"Sorry you're wrong. Final score {score}.")
