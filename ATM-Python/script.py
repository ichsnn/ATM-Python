import os  
import method
from atm import ATM

os.system('cls')

#MASUKKAN PIN
counter = 4
while counter>0 or False:
    print('--------------------------------------')
    print('     SELAMAT DATANG DI ATM PYTHON     ')
    print('--------------------------------------')    
    pin      = int(input('MASUKKAN PIN ANDA : '))
    print('--------------------------------------')   
    if method.rekening(pin) == False: 
        if counter > 0:       
            print('PIN SALAH! TERSISA ' + str(counter - 1) + ' PERCOBAAN LAGI')                    
            print()
            counter -=1 
        else:            
            print('MAAF COBA BEBERAPA SAAT LAGI...')             
    else: 
        counter = 0    
        print('PIN BENAR')
    os.system('pause')           
    os.system('cls')

print('----------------------------------')
print('     PILIH TRANSAKSI YANG ANDA    ')    
print('             BUTUHKAN             ')  
print('----------------------------------')  
print(' 1. PENARIKAN    INFO REKENING .7 ')
print(' 2. TRANSFER          UBAH PIN .5 ')
print(' 3. PEMBELIAN           KELUAR .6 ')  
print('----------------------------------')  
input_menu = int(input(" Masukkan Pilihan Anda: "))
print('----------------------------------')

os.system('pause')
os.system('cls')

if input_menu == 1:        
    print('MASUKKAN NOMINAL YANG AKAN DITARIK')
    withdraw = int(input('NOMINAL : RP. '))
    print('-----------------------------------')   
    print()    
    confirm = input('[Y/N] : ')        

elif input_menu == 2:        
    print('MASUKKAN NOMOR REKENING TUJUAN')    
    no_rek = int(('NO. REK : '))
    print('-----------------------------------')
    print()
    confirm = input('[Y/N] : ')

elif input_menu == 3:
    print('----------------------------------')
    print('            MOHON MAAF            ')
    print('   LAYANAN INI SEDANG DIPERBAIKI  ')
    print('----------------------------------')

os.system('pause')