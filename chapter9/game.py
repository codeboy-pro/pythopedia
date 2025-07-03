import random

def game():
  print("You are playing the game")
  # Fetch the highscore  
  score=random.randint(1,62)
  
  with open("1.txt") as f:
    hiscore=f.read()
    if(hiscore!=""):
      hiscore=int(hiscore)
    else:
      hiscore=0
  print(f"Your score is:{score}")
  if(score>hiscore):
    #write the hiscore to the file
    with open("1.txt","w") as f:
      f.write(str(score))


  return score
game()