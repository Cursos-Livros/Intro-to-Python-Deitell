# player 1 = Tom and player 2 = Jim

player1_name1 = ord('T')
player1_name2 = ord('o')
player1_name3 = ord('m')

player2_name1 = ord('J')
player2_name2 = ord('i')
player2_name3 = ord('m')

player1_result_character_set= player1_name1 + player1_name2 + player1_name3
player2_result_character_set= player2_name1 + player2_name2 + player2_name3

print("Player name to character set integer: ", player1_result_character_set)
print("Player name to character set integer: ", player2_result_character_set)

if(player1_result_character_set > player2_result_character_set):
    print(f"Player 1 wins!")
else:
    print(f"Player 2 wins!")