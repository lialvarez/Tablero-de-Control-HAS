import datetime
from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import random

class BoxManager(QObject):
    ''' Representa un administrador de eventos de caja, emite 
        una señal cuando llego una caja nueva '''

    inboundBox = pyqtSignal(list)
    outboundBox = pyqtSignal(int)

    def __init__(self):
        # Inicializa el boxManager como un objeto
        QObject.__init__(self)
        self.boxList = []
        self.n = 0  # Numero de cajas prodcidas. Para generar el ID


    def receiveBox(self):
        ''' Recibir una caja '''
        self.inboundBox.emit(self.boxList)

    def crearCaja(self):
        # Este lo hago solo para simular un creador de cajas
        self.n = self.n + 1
        peso = random.randint(30,51)
        t_ingreso = datetime.datetime.now()
        tapado = random.choice([True, False])
        llenado = random.choice([True, False])

        box = Box(self.n, t_ingreso)
        box.set_peso(peso)
        box.llenada = llenado
        box.tapada = tapado
        self.boxList.append(box)
        self.receiveBox()
        




class Box():
    def __init__(self, code, t_ingreso):
        # Variable tipo int que identifica la caja. Necesaria para construir la caja
        self.code = code
        # Variables que indican la hora exacta en que ingreso la caja a la linea
        self.t_ingreso = t_ingreso
        self.tapada = False
        self.llenada = False

    def set_t_llenado(self, t_llenado):
        self.t_llenado = t_llenado - self.t_ingreso

    def set_t_tapado(self, t_tapado):
        self.t_tapado = t_tapado - self.t_ingreso

    def set_t_paletizado(self, t_paletizado):
        self.t_paletizado = t_paletizado - self.t_ingreso

    def set_t_completo(self, t_completo):
        self.t_completo = t_completo - self.t_ingreso

    def set_peso(self, peso):
        self.peso = peso


def main():
    box1 = Box(1, datetime.datetime.now())
    sleep(2)
    box1.set_t_llenado(datetime.datetime.now())
    sleep(3)
    box1.set_t_tapado(datetime.datetime.now())
    box1.set_peso(34)
    print(box1.t_ingreso.strftime('%Y-%m-%d %H:%M:%S'))
    print(box1.t_llenado.seconds)
    print(box1.t_tapado.seconds)
    print(box1.peso)

if __name__ == '__main__':
    main()
    
