def cek_pin(input_pin):
    if input_pin != 123456:        
        return False
    else: return True 

def pin_counter(pin, counter):
    if cek_pin(pin) == False: 
        if counter > 1:       
            print('PIN SALAH! TERSISA ' + str(counter-1) + ' PERCOBAAN LAGI')                                      
            return counter - 1
        else:            
            print('MAAF, COBA BEBERAPA SAAT LAGI...')                            
            return 0                                
    else: 
        print('PIN BENAR')        
        return -1 

def penarikan(confirm):
    pass    