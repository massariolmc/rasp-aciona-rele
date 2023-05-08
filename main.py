import RPi.GPIO as gpio
import time


class AcionaRele():
    def __init__(self):
        #Desabilita os warnings
        gpio.setwarnings(False)
        gpio.cleanup()
        self.define_pins()

    def define_pins(self):
        self.pins = {
                'pin11' : 11
            }
        self.define_setup(**self.pins)

    def define_setup(self,**kwargs):
        gpio.setmode(gpio.BOARD)
        for nome_pins,valor_pins in kwargs.items():
            gpio.setup(valor_pins,gpio.OUT)

    def ativa(self):
        for k,v in self.pins.items():
            #Desativa o rele
            gpio.output(v,gpio.LOW)
            time.sleep(1)
            #Aciona o rele
            gpio.output(v,gpio.HIGH)
            time.sleep(3)

if __name__ == '__main__':
    exe = AcionaRele()
    try:
       while True:
           exe.ativa()
    except Exception as e:
        print(e)
    finally:
        #Desfaz as configurações dos pinos
        gpio.cleanup()

