import time
options = ['a bundle of foo','a bag of eggs','an option','exit']

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

def gameSelector(options,prompt,destinations):
    def selectorLoop():
        prompt()
        ans = userIn(options)
        destination()
    return selectorLoop

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
        if (ans == 'a bag of eggs'): 
            print('smelly stuff')
            takeSecond(0.5,1)

#intro = gameSelector(options,intro)

def end():
    print('Goodbye!')
    exit


def testMain():
    intro()
    options = ['a bundle of foo','a bag of eggs','an option','exit']
    while True:
        print('please select one of the following options: \n')
        ans = userIn(options)

        #don't think I need this atm
        #print('user picked ans '+ options[(int(ans)-1)])
        if (ans == 'exit'):
            print('Goodbye!')
            break
        takeSecond(2)

def runGame():
    intro()
    end()
#testMain()
runGame()
