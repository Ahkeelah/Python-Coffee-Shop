import time
import random

Barista = ['Levi', 'Armin', 'Erin']

LGreetings = ['Your order?','Order...','*staaaaaaare*',]

AGreetings = ['How can I be of service today','*Beeming Smile*, What a day to be alive, what would you like for us to whip up for you today']

EGreetings = ['Welcome, what will you have today?','Hello, what can I get for ya?','Welcome to Python cafe what will you be having today?']

Menu = ['[1]Black Coffee','[2]Cinnamon Roll','[3]Coffee Cake','[4]Ice Coffee','[5]Scone','[6]Python Cafe Expresso']

playerOrder = []

def randomConvo():
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



options = ['Black Coffee','Cinnamon Roll','Coffee Cake','Ice Coffee','Scone','Python Cafe Expresso','exit']

def takeSecond(t,numOfBreaks=1):
    time.sleep(t)
    for i in range(numOfBreaks):
        print('')

def clearTerm():
    for i in range(15):
        print('\n\n')

def userIn(options):
    while True:
        print('please select one of the following options: \n')

        ans = 1
        for i in options:
            print(str(ans) + ') '+ str(i))
            ans +=1

        x = input()
        try: 
            ans = int(x) -1
            ans = options[ans]
        except: 
            print('uh-oh you made a typo, try again!')
            takeSecond(0.5)
            continue
        break
    print('\nI see you have selected: '+ ans)
    return ans

def displayMenu():
    print('..................................')
    print('|  this is a picture of the menu  |')
    print('...................................')

def stateOrder():
    print('okay so you ordered: ')
    print(str(playerOrder))

def LeviOrder():
  print(random.choice(LGreetings) + " *Agressivevly Holds up menu * " + "\n" + str(Menu))
  displayMenu()
  ans = userIn(options)
  if (ans == 'Black Coffee'):
      print('black coffee or whatever')
      playerOrder.append('Black Coffee')
  if (ans == 'exit'):
      end()
  stateOrder()



def order():
  random.choice(Barista)

  if random.choice(Barista) == Barista[0]:
    LeviOrder()
  elif random.choice(Barista) == Barista[1]:
    print(random.choice(AGreetings) + " Here's our menu " + "\n" + str(Menu))
    LeviOrder()
  else:
    print(random.choice(EGreetings) + " *Hands Menu* " + "\n" + str(Menu))
    LeviOrder()        



def intro():
    clearTerm()
    print(' Hello welcome to the Python Coffee shop!')
    print('You will be presented with options type that option to proceed')
    takeSecond(1,2)
    while True:
        ans = userIn(options)
        if (ans == 'exit'): 
            end()
            break
        if (ans == 'Black Coffee'): 
            print('A clean way to start the day')
            takeSecond(6,6)
        if (ans == 'a bag of eggs'): 
            print('smelly stuff')
            takeSecond(0.5,1)
            

def end():
    print('Goodbye!')
    exit

def testMain():
    intro()
    options = ['a bundle of foo','a bag of eggs','an option','exit']
    while True:
        print('please select one of the following options: \n')
        ans = userIn(options)

        if (ans == 'exit'):
            print('Goodbye!')
            break
        takeSecond(2)

def runGame():
    #intro()
    order()
    #randomConvo()

runGame()


      
