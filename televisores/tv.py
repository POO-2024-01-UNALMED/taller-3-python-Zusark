class TV: 
    _numTV=0

    def __init__(self,marca,estado):
        self._marca = marca
        self._estado = estado
        TV._numTV+=1
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._control = None

    def setMarca(self,marca):
        self._marca = marca
    def getMarca(self):
        return self._marca
    
    def setCanal(self,num):
        if (self._estado == True) and (num <=120 ) and ( num>=1 ):
            self._canal = num

    def getCanal(self):
        return self._canal
    
    def setPrecio(self,precio):
        self._precio = precio
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self,volumen):
        if self._estado == True and volumen>=0 and volumen <= 7:
            self._volumen = volumen
    def getVolumen(self):
        return self._volumen
    
    def setControl(self,control):
        self._control = control
    def getControl(self):
        return self._control
    
    def setNumTV(num):
        TV._numTV = num
    def getNumTV():
        return TV._numTV
    
    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False
    
    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if (self._estado == True)and(self._canal<120):
            self._canal +=1
    def canalDown(self):
        if (self._estado == True)and(self._canal>1):
            self._canal -=1
    def volumenUp(self):
        if (self._estado == True)and(self._volumen<7):
            self._volumen +=1
    def volumenDown(self):
        if (self._estado == True)and(self._volumen>0):
            self._volumen -=1