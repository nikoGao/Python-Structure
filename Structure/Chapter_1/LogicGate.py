class Connector:
    def __init__(self, fromtube, totube):
        self.fromtube = fromtube
        self.totube = totube

        totube.setNextPin(self)

    def getFrom(self):
        return self.fromtube

    def getTo(self):
        return self.totube

class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class Binary(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if not self.pinA:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if not self.pinB:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if not self.pinA:
            self.pinA = source
        else:
            if not self.pinB:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class Unary(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        if not self.pin:
            return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(Binary):
    def __init__(self, n):
        Binary.__init__(self, n)


    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(Binary):
    def __init__(self, n):
        Binary.__init__(self, n)


    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NorGate(OrGate):

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


class NandGate(AndGate):
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

class NotGate(Unary):
    def __init__(self,n):
        Unary.__init__(self, n)


    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1

def main():
    g1 = NandGate('G1')
    print (g1.getOutput())

main()