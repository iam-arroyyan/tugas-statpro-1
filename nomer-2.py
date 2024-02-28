#input pertama memasukan angka bil bulat
x = int(input('Masukan angka bulat (0 = berhenti): '))

#perulangan while jika x lebih besar dari 0 maka akan terjadi looping jika x samadengan 0 program akan berhenti
while x > 0:
    if (x % 2 == 0): #conditional statement x mod 2 adalah 0 akan bernilai genap jika salah akan bernilai ganjil
        print(x,'adalah bilangan genap')
        x = int(input('Masukan angka bulat (0 = berhenti): ')) #input setelah while jika nilai x masih lebih besar dari 0
    else:
        if(x % 3 == 0): #jika x angka ganjil mod 3 adalah 0 maka x bisa dibagi dengan 3  
            print(x,'adalah bilangan ganjil dapat dibagi 3')
        else:
            print(x,'adalah bilangan ganjil tidak dapat dibagi 3')
        x = int(input('Masukan angka bulat (0 = berhenti): '))
