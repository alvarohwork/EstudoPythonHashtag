# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#classes
class TV:
    #É possível criar um atributo da classe que define a caracteristica da classe inteira.
    #Pode ser modificado, mas é algo perigoso pq todos os objetos instanciados vão herdar essa modificação.
    cor = 'preta'

    def __init__(self, tamanho):
        #Estes atributos são chamados de atributos de instância porque podem ser modificados diretamente pelos
        #objetos instanciados no seu programa.
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    # É possível colcoar parâmetros nos métodos para serem enviados pelos objetos instanciados
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal



#Instanciando os objetos a partir da classe TV. A partir daí temos um objeto com as caracteristicas da classe.
tv_sala = TV(tamanho=55)
tv_quarto = TV(tamanho=40)
print(tv_sala.tamanho)
print(tv_quarto.tamanho)

#Os atributos determinados na classe podem ser acessados nos objetos instanciados, pois eles herdaram estas 
#características.
print(tv_sala.volume)
#Mudando a caracterisca de cor da tv_sala
tv_sala.volume = 20
print(tv_sala.cor)

#Passando o parâmetro novo_canal do método mudar_canal() instanciado no objeto tv_sala.
tv_sala.mudar_canal(novo_canal="Globo")
print(tv_sala.canal)
print(tv_quarto.canal)

#Modificando um atributo de CLASSE no caso a cor
print(tv_sala.cor)
print(tv_quarto.cor)
TV.cor = "AMARELO"
print(tv_quarto.cor)
print(tv_sala.cor)

