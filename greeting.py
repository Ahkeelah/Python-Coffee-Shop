import random

Barista = ['Levi', 'Armin', 'Erin']

LGreetings = ['Your order?','Order...','*staaaaaaare*',]

AGreetings = ['How can I be of service today','*Beeming Smile*, What a day to be alive, what would you like for us to whip up for you today']

EGreetings = ['Welcome, what will you have today?','Hello, what can I get for ya?','Welcome to Python cafe what will you be having today?']

Menu = ['[1]Black Coffee','[2]Cinnamon Roll','[3]Coffee Cake','[4]Ice Coffee','[5]Scone','[6]Python Cafe Expresso']


random.choice(Barista)

if random.choice(Barista) == Barista[0]:
  print(random.choice(LGreetings) + " *Agressivevly Holds up menu * " + "\n" + str(Menu))
elif random.choice(Barista) == Barista[1]:
    print(random.choice(AGreetings) + " Here's our menu " + "\n" + str(Menu))
else:
      print(random.choice(EGreetings) + " *Hands Menu* " + "\n" + str(Menu))

#CustomerGreetingCommands = CGC 
#CustomerGreetingReply = CGCR
#MenuDiologue = MD

print('[1]Wonderful day we are having, [2]I would like to order ...')

LCGCR1 = ['*unamused* What would you like to order?', '....I suppose', "Let's keep it professional"]
ACGCR1 = ['Oh yes, so glad to spend it here at Python Cafe *large grin*', "Couldn't be better. *large grin*" ]
ECGCR1 = ['Yes', 'Certainly']

CGC = input()

if CGC == 1 and Barista == 0:
  print(random.choice(LCGCR1))
elif Barista == 1:
    print(random.choice(ACGCR1))
else:
      print(random.choice(ECGCR1))



LMD = ["Can you ask for something we have?", "*Scribbles in Book*", "Paiteinly waits"]
AMD =["Will that be all", "Oh we do not have that currently, perhaps I can ask our manager to stock it"]
EMD =["Okay..", "That is not on the menu"]


if CGC == 2:
  while True: 
      print("Go on")
      order = input()
      match order:
        case 1:
          print(str(Menu[0]))
        case 2:
          print(str(Menu[1]))
        case 3:
          print(str(Menu[2]))
        case 4:
          print(str(Menu[3]))
        case 5:
          print(str(Menu[4]))
        case 6:
          print(str(Menu[5]))
        case _:
          print("Sorry we don't have that item")

  
     
      
