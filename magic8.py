import random

#Assigning values to the variables we will use for the Magic 8-ball generator#
name = "Pricey"
question = "Does she love me?"
answer = ""

#Writing code to generate a random number which the Magic 8-Ball will use to provide one of our selected responses#
random_number = random.randint(1, 11) #This will generate a random number between 1 (inclusive) and 11 (inclusive) and stores the result within a variable#
print(random_number)

#Contol Flow#
if random_number == 1:
  answer += "Yes - Definitely"
elif random_number == 2:
  answer += "It is decidedly so"
elif random_number == 3:
  answer += "Without a doubt"
elif random_number == 4:
  answer += "Reply hazy, try again"
elif random_number == 5:
  answer += "Ask again later"
elif random_number == 6:
  answer += "Better not tell you now"
elif random_number == 7:
  answer += "My sources say no"
elif random_number == 8:
  answer += "Outlook not so good"
elif random_number == 9:
  answer += "Very doubtful"
elif random_number == 10:
  answer += "Extra Response 10"
elif random_number == 11:
  answer += "Extra Response 12"
else:
  answer += "Error"

if question == "":
  print("Where's the flipping question lad?") #Task 14#
elif name == "":
  print(question) #task 13#
  print("Magic 8-Ball's answer:", answer)
else: 
  print(name, "asks:", question)
  print("Magic 8-Ball's answer:", answer)