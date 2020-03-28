# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6

bit_or =  a | b
bit_and = a & b
bit_xor = a ^ b
bit_no = ~ a
bit_right = a >> 2
bit_left = a << 2
print("Результат побитового OR: ", bin(bit_or))
print("Результат побитового AND: ", bin(bit_and))
print("Результат побитового XOR: ", bin(bit_xor))
print("Результат побитового NO: ", bin(bit_no))
print("Результат побитового >>: ", bin(bit_right))
print("Результат побитового <<: ", bin(bit_left))






