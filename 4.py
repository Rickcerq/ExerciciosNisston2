class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
        self.saldo_atual = 0.0
        self.saldo_atualizado = 0.0

    def depositar(self):
        dinheiro_depositado = float(input('Quanto você deseja depositar?: '))
        self.saldo_atual = self.saldo + dinheiro_depositado
        return self.saldo_atual

    def sacar(self):
        dinheiro_sacado = float(input('Quanto você deseja sacar?: '))
        self.saldo_atualizado = self.saldo_atual - dinheiro_sacado
        return self.saldo_atualizado
    
    def mostrar_saldo(self):
        print('Seu saldo atual é de ' +str(self.saldo_atualizado) + ' R$')

c1 = ContaBancaria(1300.46, 'Henrique')
c1.depositar()
c1.sacar()
c1.mostrar_saldo()