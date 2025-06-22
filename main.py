import time

def takeSecond(t,numOfBreaks=1):
    time.sleep(t)
    for i in range(numOfBreaks):
        print('')

def clearTerm():
    for i in range(15):
        print('\n\n')

def userIn(options):
    ans = 1
    for i in options:
        print(str(ans) + ') '+ str(i))
        ans +=1

    x = input()
    return x

def intro():
    clearTerm()
    print(' Hello welcome to the Python Coffee shop!')
    print('You will be presented with options type that option to proceed')
    takeSecond(1,2)

def testMain():
    intro()
    options = ['a bundle of foo','a bag of eggs','an option','exit']
    while True:
        print('please select one of the following options: \n')
        ans = userIn(options)
        try: 
            ans = int(ans) - 1
            ans = options[ans]
        except:
            print('Uh made a typeO try again!')
            takeSecond(0.5)
            continue 
        #don't think I need this atm
        #print('user picked ans '+ options[(int(ans)-1)])
        print('\nI see you have selected: '+ ans)
        if (ans == 'exit'):
            print('Goodbye!')
            break
        takeSecond(2)


testMain()
