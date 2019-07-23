# Buatlah script pengulangan angka. 
# Jika angkanya kelipatan 3 dan angkanya bukan 3 tulis “INITIGA”. 
# Jika kelipatan 7 dan bukan angka 7 tulis “INITUJUH”.

numbers = 0

while numbers < 100:
    numbers = numbers + 1
    if((numbers%3==0) and (numbers!=3)):
        print('INITIGA')
    elif((numbers%7==0) and (numbers!=7)):
        print('INITUJUH')
    else:
        print(numbers)
        
# Nadhifa Sofia with Python
