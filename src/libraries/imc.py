class Imc:
    imc = 0
    composicion_corporal = ''

    def __init__(self, peso, altura, fecha):
        self.fecha = fecha
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        self.imc = round(self.peso / (self.altura * self.altura),1)

    def mostrar_imc(self):
        return self.imc

    def mostrar_fecha(self):
        return self.fecha

    def mostrar_composicion_corporal(self):
        return self.composicion_corporal

    def evaluar_composicion_corporal(self):
        if self.imc < 18.5:
            self.composicion_corporal = 'Peso Inferior a Normal'
        elif 18.5 <= self.imc <= 24.9:
            self.composicion_corporal = 'Normal'
        elif 25.0 <= self.imc <= 29.9:
            self.composicion_corporal = 'Peso superior al Normal'
        elif self.imc <= 30:
            self.composicion_corporal = 'Obesidad'

