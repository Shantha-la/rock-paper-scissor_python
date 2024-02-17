import random
print("*******************************************************")
print("*               **PAPER**ROCK**SCISSOR*              *")
print("*******************************************************")
print(" lets starts the game!!....")
point=0
ai=0
hs=0
cs=0
ma=0
while('True'):
  if(ma>5):
    print("######################")
    print("total match:",ma)
    print("human score:",hs)
    print("AI score:",cs)
    if(hs>cs):
      print("congrats you won")
    elif(cs>hs):
      print("AI won... better luck next time")
    else:
      print("match drawn")
      print("##############################")
      braek
  c=input(" choose paper->p  rock->r  scissor->s stop->stop: ")
  if(c=="p"):
    print("paper")
    point=10+random.randint(1,3)
    match point:
         case 11:
             ma=ma+1
             hs=hs+1
             cs=cs+1
             print("human: paper","AI: rock")
             print("match: ",ma," human score:",hs,"AI score:")
             print("human:win","AI :lost")
             print(" -----------------------------")
             
         case 12:
             ma=ma+1
             hs=hs+1
             cs=cs+1
             print("human:paper","AI: scissor")
             print("match: ",ma," human score:",hs,"AI score:")
             print("human :lost","AI :win")
             print(" -----------------------------")
             
         case 13:
             ma=ma+1
             hs=hs+1
             cs=cs+1
             print("human:paper","AI: paper")
             print("match: ",ma," human score:",hs,"AI score:")
             print("match draw")
             print(" -----------------------------")
             
  elif(c=="r"):
    print("rock")
    point=10+random.randint(1,3)
    match point:
         case 21:
             ma=ma+1
             hs=hs+1
             cs=cs+1
             print("human: rock","AI: scissor")
             print("match: ",ma," human score:",hs,"AI score:")
             print("human:win","AI :lost")
             print(" -----------------------------")
         case 22:
             ma=ma+1
             hs=hs+1
             cs=cs+1
             print("human:rock","AI: paper")
             print("match: ",ma," human score:",hs,"AI score:")
             print("human :lost","AI :win")
             print(" -----------------------------")
         case 23:
             ma=ma+1
             hs=hs+1
             cs=cs+1
             print("human:rock","AI: rock")
             print("match: ",ma," human score:",hs,"AI score:")
             print("match draw")
             print(" -----------------------------")
  elif(c=="s"):
    print("scissor")
    point=10+random.randint(1,3)
    match point:
         case 31:
             ma=ma+1
             hs=hs+1
             cs=cs+1
             print("human: scissor","AI: rock")
             print("match: ",ma," human score:",hs,"AI score:")
             print("human:win","AI :lost")
             print(" -----------------------------")
         case 32:
             ma=ma+1
             hs=hs+1
             cs=cs+1
             print("human:scissor","AI: paperp")
             print("match: ",ma," human score:",hs,"AI score:")
             print("human :lost","AI :win")
             print(" -----------------------------")
         case 33:
             ma=ma+1
             hs=hs+1
             cs=cs+1
             print("human:scissor","AI: scissor")
             print("match: ",ma," human score:",hs,"AI score:")
             print("match draw")
             print(" -----------------------------")
  elif(c=="stop"):
    break
print("program end")