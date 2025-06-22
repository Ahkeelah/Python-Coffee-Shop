import random

Barista = ['Levi', 'Armin', 'Erin']

LGreetings = ['Your order?','Order...','*staaaaaaare*',]

AGreetings = ['How can I be of service today','*Beeming Smile*, What a day to be alive, what would you like for us to whip up for you today']

EGreetings = ['Welcome, what will you have today?','Hello, what can I get for ya?','Welcome to Python cafe what will you be having today?']


random.choice(Barista)


if Barista == 0:
  print(random.choice(LGreetings))
elif Barista == 1:
    print(random.choice(AGreetings))
else:
      print(random.choice(EGreetings))

#CustomerGreetingCommands = CGC
#CustomerGreetingReply = CGCR

print('[1]Wonderful day we are having, [2]I would like to order ...')

LCGCR1 = ['*unamused* What would you like to order?', '....I suppose', "Let's keep it professional"]
ACGCR = ['Oh yes, so glad to spend it here at Python Cafe *large grin*', "Couldn't be better. *large grin*" ]
ECGCR = []

CGC = input()

if CGC == 1 and Barista == 0:
  print(random.choice(LGreetings))
elif Barista == 1:
    print(random.choice(AGreetings))
else:
      print(random.choice(EGreetings))


Menu = ['Black Coffee','Cinnamon Roll','Coffee Cake','Ice Coffee','Scone','Python Cafe Expresso']

