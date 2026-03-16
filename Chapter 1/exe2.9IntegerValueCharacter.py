var_t = ord('T')
var_o = ord('o')
var_m = ord('m')
total_char_tom = var_t + var_o + var_m

print(f'Tom name total: {total_char_tom} ')

var_j = ord('J')
var_i = ord('i')
total_char_jim = var_j + var_i + var_m

print(f'Jim name total: {total_char_jim} ')

if(total_char_tom > total_char_jim):
    print('Tom Starts')
else:
    print('Jim Starts')
