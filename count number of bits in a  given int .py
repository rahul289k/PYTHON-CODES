def count_bits(x):
    num = 0
    while x:
        # and operatot with even num always gives zero and with odd gives 1 i.e bits
        num += x & 1

        # right shifing the num by 1 each time

        x >>= 1
        
    return num
print(count_bits(15))


