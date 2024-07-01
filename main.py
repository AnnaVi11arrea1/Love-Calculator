print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?") 

# combine both names
combined_names = name1 + name2
# change to lowercase to make finding letters easier
lower_names = combined_names.lower()

# count the number of times each letter occurs in the word "true"
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
# Make this first digit for the score:
first_digit = t + r + u + e 

# count the number of times each letter occurs in the word "true"
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e") 
# Make this second digit for the score:
second_digit = l + o + v + e 

# concatenate digits, convert to integer.
score = int(str(first_digit) + str(second_digit))

# conditions for the score
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score < 50):
  print(f"Your score is {score}, you are alright together.")
else: 
  print(f"Your score is {score}.")