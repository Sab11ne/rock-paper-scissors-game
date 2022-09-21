human_turn = 'paper'
computer_turn = 'scissors'

if human_turn == 'rock' and computer_turn == 'scissors':
    print('human_wins!')
elif human_turn == 'paper' and computer_turn == 'rock':
    print('human_wins!')
elif human_turn == 'scissors' and computer_turn == 'paper':
    print('human_wins!')
elif human_turn == 'scissors' and computer_turn == 'rock':
    print('computer_wins!')
if human_turn == 'rock' and computer_turn == 'paper':
    print('computer_wins!')
if human_turn == 'paper' and computer_turn == 'scissors':
    print('computer_wins!')
if human_turn == 'rock' and computer_turn == 'rock':
    print('Draw!')
if human_turn == 'paper' and computer_turn == 'paper':
    print('Draw!')
if human_turn == 'scissors' and computer_turn == 'scissors':
    print('Draw!')
elif human_turn == computer_turn:
    print('Draw!')
