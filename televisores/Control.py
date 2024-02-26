import TV
class Control:
    _tv = None
    def turnOn(self):
        self._tv.turnOn(self)
    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()
    
    def setCanal(self):
        self._tv.setCanal()
    def setVolumen(self):
        self._tv.setVolumen()
    
    def enlazar(self, tv):
        if isinstance(tv, TV):
            self._tv = tv
            tv.setControl(self)
    
    def setTv(self, tv):
        self.enlazar(tv)

    def getTv(self):
        return self._tv