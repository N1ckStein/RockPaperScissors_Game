import random




while True:
    

    def play():
            
        user = input("Welcome. The rules are simple: rock > scissors, scissors > paper, paper > rock. Select your weapon! 'r' = rock, 'p' = paper, 's' = scissors. Type quit to exit\n")
        user = user.lower()
        
        computer = random.choice(['r', 'p', 's'])
        
        if user == 'quit':
            print('goodbye')
            return 'goodbye'

        elif user == computer:
            print('Its a tie...how boring')

        elif user == 'r' and computer == 's' or user == 's' and computer == 'p' or user == 'p' and computer == 'r':
            print("You chose {} and the computer chose {}. You Won...This time.".format(user,computer))
            
        else:
            print("You chose {} and the computer has chosen {}. Ur trash, kid. Hold that L".format(user,computer))
            

    game = play()
    if game == 'goodbye':
        break

    
            
        
            

    

    

