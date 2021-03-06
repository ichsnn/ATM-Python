import os  
import method

os.system('cls')

#MASUKKAN PIN
counter = 4
while counter>0:
    print('--------------------------------------')
    print('     SELAMAT DATANG DI ATM PYTHON     ')
    print('--------------------------------------')    
    pin      = int(input('MASUKKAN PIN ANDA : '))
    print()   
    method.cek_pin(pin)    
    counter = method.pin_counter(pin, counter)
    print('--------------------------------------')    
    os.system('pause')
    os.system('cls')

if counter == -1:
    exit_menu = False
    while exit_menu == False:  
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
            confirm = input('[Y/N] : ')        

        elif input_menu == 2:        
            print('MASUKKAN NOMOR REKENING TUJUAN')    
            no_rek = int(input('NO. REK : '))
            print('-----------------------------------')    
            confirm = input('[Y/N] : ')

        elif input_menu == 3:
            print('----------------------------------')
            print('            MOHON MAAF            ')
            print('   LAYANAN INI SEDANG DIPERBAIKI  ')
            print('----------------------------------')  

        elif input_menu == 6:
            print('TERIMAKASIH SUDAH MENGGUNAKAN ATM PYTHON')
            exit_menu = True
            print()
            os.system('pause')            

        os.system('cls')                    