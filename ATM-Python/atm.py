class ATM:

    def __init__(self, pin, saldo):        
        self.pin = pin
        self.saldo = saldo

    def info(self):
        print('Nomor Rekening : ' + str(self.rekening))  
        print('PIN            : ' + str(self.pin))
        