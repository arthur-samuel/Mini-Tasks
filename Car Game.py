command = ""
while command != 'quit':
    command = input('> ').lower()

    if command == "start":
        print('Car start, ready to go ....')
    elif command == 'stop':
        print('Car stopped....')
    elif command == 'help':
        print('''
        start - starts the game
        stop - stops the car
        quit - quits the game
        
        ''')
    else:
        print('Invalid')