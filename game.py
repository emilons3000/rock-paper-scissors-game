import random
turns = ['rock', 'paper', 'scissors']
human_turns = []  #tuksi sarkasti kuriem append pievieno izveles
computer_turns = []


while(True):
    human_turn = input("Enter your turn or type exit:") #abi izvelas izveli
    computer_turn = random.choice(turns)

    if human_turn == 'exit':
        print('thank you for playing')
        break
        

    human_turns.append(human_turn) #saskaita izveles un pievieno tuksajam sarkastam
    computer_turns.append(computer_turn)




    

    print(f'Human:{human_turn} vs. Computer: {computer_turn}')
    if human_turn == computer_turn:
        print('Draw!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('Human wins!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('Human wins!')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('Human wins!')
    else:
        print('Computer wins')
