eggs = 53
box = 6

# Calcula a quantidade de caixas necessárias o numero de ovos sobrando e o numero de ovos na ultima caixa
total_boxes = eggs // box
eggs_last_box = eggs % box

# Total de caixas necessárias
if eggs_last_box > 0:
    total_boxes += 1

print(f"{eggs} eggs require {total_boxes} boxes.")

# Se há caixa incompleta, mostra detalhes
if eggs_last_box > 0:
    print(f"Last box has {eggs_last_box} eggs.")
    print(f"Need {box - eggs_last_box} more eggs to fill it.")
else:
    print("All boxes are full.")
