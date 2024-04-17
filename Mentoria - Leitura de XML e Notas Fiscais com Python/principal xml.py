import xmltodict

with open('NFs Finais/nota15997.xml', 'rb') as arquivo:

    documento = xmltodict.parse(arquivo)

EnderecoTomador = documento['NFe']['Discriminacao']
print(EnderecoTomador)
dadosdiscri = list(EnderecoTomador.items())
print(dadosdiscri)
#for item in EnderecoTomador:
#    print(EnderecoTomador[item])

#print (documento['NFe']['EnderecoTomador']['Logradouro'])
##print(documento['NFe']['RazaoSocialTomador'])



