marbles = 22
friends = 4

total_marbles = marbles // friends
remainder_marbles = marbles % friends

if remainder_marbles > 0:
    print(f"Não é possível dividir as marbles igualmente em 4 pois cada amigo ficará com {total_marbles} e ainda restaram {remainder_marbles}.")
else:
    print(f"É possível as marbles igualmente entre {friends} sendo {total_marbles} para cada amigo e não restando nenhuma.")
