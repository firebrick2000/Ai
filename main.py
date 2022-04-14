import random
greetings = ["hello", "hi", "hola", "howdy", "greetings"]
responses = ["music is so relaxing", "i love playing games", "i like pets. dogs are my favorite"]
goodbyes = ["bye", "goodbye", "siya", "adios"]
keyword = ["pet", "games", "music",  ]
print(random.choice(greetings))
user = input("say something to start (or type bye to quit ) ")
user = user.lower()
while (user != "bye"):
  keyword_found = False
  
  for index in range(len(keyword)):
    if (keyword[index] in user):
      print("bot: " + responses[index])
      keyword_found = True

  if (keyword_found == False):
    new_keyword = input("i'm not sure how to respond. What keyword should i respond to? ")
    keyword.append(new_keyword)
    new_response = input("how should i respond to " +new_keyword+ "? ")
    responses.append(new_response)
  user = input("say something to start (or type bye to quit ")
  user = user.lower()
print(random.choice(goodbyes))