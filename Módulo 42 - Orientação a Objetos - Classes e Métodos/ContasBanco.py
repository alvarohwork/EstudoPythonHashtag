from datetime import datetime
import pytz


class ContaCorrente():
    '''
        ### DOCSTRING - USANDO PARA DOCUMENTAR A CLASSE
        Classe para gerenciamento da conta corrente

        Atributos:
            nome: (str) : Nome do cliente
            .....
            .....

    '''

    #Método estático que não usa nenhuma informação da classe.
    #O decorator é informativo para que fique claro que se trata de um método estatico.
    @staticmethod
    def _datahora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')


    def __init__(self, nome, cpf, agencia, conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.conta = conta
        self.transacoes = []
        
    def consulta_saldo(self):
        print('{} seu saldo é de: R${:,.2f}'.format(self.nome, self.saldo))

    def depositar(self, vr_deposito):
        self.saldo += vr_deposito
        self.transacoes.append((vr_deposito, self.saldo, 'Tipo Transação: Depósito', ContaCorrente._datahora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar(self, vr_saque):
        if self.saldo - vr_saque < self._limite_conta():
            print('Você não possui limite para sacar este valor.')
            self.consulta_saldo()
        else:    
            self.saldo -= vr_saque
            self.transacoes.append((vr_saque, self.saldo, 'Tipo Transação: Saque', ContaCorrente._datahora()))

    def consultar_historico(self):
        '''
            ## É POSSÍVEL CRIAR DOC STRING PARA OS MÉTODOS TAMBEM.
            
        '''
        print("=================================")
        print("==== HISTÓRICO DE TRANSAÇÕES ====")
        print("=================================")
        for transacao in self.transacoes:
            print (transacao)
            print("=" * 100)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((valor, self.saldo, f'Tipo Transação: Transferência para {conta_destino.nome}', ContaCorrente._datahora()))
        conta_destino.saldo += valor
        self.transacoes.append((valor, conta_destino.saldo, f'Tipo Transação: Transferência de {self.nome}', ContaCorrente._datahora()))



#### PROGRAMA ####
# Abertura da conta
print("===============================")
print("===== ABERTURA DAS CONTAS =====")
print("===============================")
conta_alvaro = ContaCorrente("Alvaro", "032.405.327-82", "1234", "05010274-2")
print("Olá {} sua conta foi aberta no CPF:{} e seu saldo é de R${:,.2f}".format(conta_alvaro.nome, conta_alvaro.cpf, conta_alvaro.saldo))
print("===============================")
conta_be = ContaCorrente("Bernardo", "197.804.690-99", "5497", "10125-2")
print("Olá {} sua conta foi aberta no CPF:{} e seu saldo é de R${:,.2f}".format(conta_be.nome, conta_be.cpf, conta_be.saldo))
print("===============================")
print("")

#Depositando $$$ na conta
print("===============================")
print("===== DEPOSITO NAS CONTAS =====")
print("===============================")
conta_alvaro.depositar(12000)
print('Olá {} seu depósito foi feito com sucesso e seu saldo atual é de R${:,.2f}'.format(conta_alvaro.nome, conta_alvaro.saldo))
print("===============================")
conta_be.depositar(55000)
print('Olá {} seu depósito foi feito com sucesso e seu saldo atual é de R${:,.2f}'.format(conta_be.nome, conta_be.saldo))
print("===============================")
print("")

#Sacando $$$ da conta
print("===============================")
print("=====   SAQUE NAS CONTAS  =====")
print("===============================")
conta_alvaro.sacar(2000)
print('Olá {} seu saque foi processado com sucesso e seu saldo atual é de R${:,.2f}'.format(conta_alvaro.nome, conta_alvaro.saldo))
print("===============================")
conta_be.sacar(2000)
print('Olá {} seu saque foi processado com sucesso e seu saldo atual é de R${:,.2f}'.format(conta_be.nome, conta_be.saldo))
print("===============================")
print("")

#Transferindo $$$ da conta
print("================================")
print("===== TRANSFERENCIA CONTAS =====")
print("================================")
conta_alvaro.transferir(2000, conta_be)
print('Olá {} sua transferência para {} no valor de {} foi processada com sucesso e seu saldo atual é de R${:,.2f}'.format(conta_alvaro.nome, conta_be.nome, 2000, conta_alvaro.saldo))
print("===============================")
print("")

#Consultando os saldos
print("================================")
print("=====  CONSULTA DE SALDOS  =====")
print("================================")
conta_alvaro.consulta_saldo()
print("================================")
conta_be.consulta_saldo()
print("================================")
print("")

conta_alvaro.consultar_historico()