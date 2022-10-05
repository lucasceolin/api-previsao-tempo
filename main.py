import requests
import json
import sqlite3
import datetime

opcao = int(input('Realizar consulta por: [1]-Cidade,UF ou [2]-Cidade?'))
if opcao == 1:
    cidade_uf = input('Informe a cidade e o estado [Padrão: Cidade, UF ]: ')
    requisicao = requests.get('https://api.hgbrasil.com/weather?key=4efea24f&city_name={}'.format(cidade_uf))
    localidade = json.loads(requisicao.text)
    #print(localidade)
    datahora = datetime.datetime.now()
    temperatura = local['results']['temp']
    data =  local['results']['date']
    hora = local['results']['time']
    descricaotempo = localidade['results']['description']
    dianoite = localidade['results']['currently']
    umidade = localidade['results']['humidity']
    velocidadevento = localidade['results']['wind_speedy']
    nascesol = localidade['results']['sunrise']
    porsol = localidade['results']['sunset']
    condicaotempoa = localidade['results']['condition_slug']

    print('Temperatura atual em graus celsius: {}'.format(temperatura))
    print('Data: {}'.format(data)+' Hora: {}'.format(hora))
    print('Descrição do tempo atual: {}'.format(descricaotempo))
    print('Dia ou noite: {}'.format(dianoite))
    print('Umidade: {}'.format(umidade))
    print('Velocidade do vento: {}'.format(velocidadevento))
    print('Nascer do sol: {}'.format(nascesol)+' Pôr do sol: {}'.format(porsol))
    print('Condição de tempo atual: {}'.format(condicaotempo))

    condicoessemana = json.loads(requisicao.text)
    #condicoessemana = list(requisicao.json())
    forecast = [condicoessemana['results']['forecast']]
    for p in forecast:
        print(p[0],p[1],p[2],p[3],p[4],p[5],p[6])
        #print('Temperaturas máximas semanal:')
        maximo = p[0]['max'],p[1]['max'],p[2]['max'],p[3]['max'],p[4]['max'],p[5]['max'],p[6]['max']
        #print(maximo)
        #print('Temperaturas mínimas semanal:')
        minimo = p[0]['min'],p[1]['min'],p[2]['min'],p[3]['min'],p[4]['min'],p[5]['min'],p[6]['min']
        #print(minimo)

    somamaximo = 0
    somaminimo = 0

    for p in forecast:
       somamaximo = sum(maximo)
       #print(f'Soma das temperaturas máximas da semana: {somamaximo}')

    for p in forecast:
        somaminimo = sum(minimo)
        #print(f'Soma das temperaturas máximas da semana: {somaminimo}')
    
    mediamaximo = somamaximo/7
    mediaminimo = somaminimo/7
    print(f'Média da temperatura máxima da semana: {media_maximo}')
    print(f'Média da temperatura mínima da semana: {media_minimo}')
  
elif opcao == 2:
    cidade = input('Informe a cidade: ')
    requisicao = requests.get('https://api.hgbrasil.com/weather?key=4efea24f&city_name={}'.format(cidade))
    localidade = json.loads(requisicao.text)
    #print(localidade)
    datahora = datetime.datetime.now()
    temperatura = localidade['results']['temp']
    data =  localidade['results']['date']
    hora = localidade['results']['time']
    descricaotempo = localidade['results']['description']
    dianoite = localidade['results']['currently']
    umidade = localidade['results']['humidity']
    velocidadevento = localidade['results']['wind_speedy']
    nascesol = localidade['results']['sunrise']
    porsol = localidade['results']['sunset']
    condicaotempo = localidade['results']['condition_slug']

    print('Temperatura atual em graus celsius: {}'.format(temperatura))
    print('Data: {}'.format(data)+' Hora: {}'.format(hora))
    print('Descrição do tempo atual: {}'.format(descricaotempo))
    print('Dia ou noite: {}'.format(dianoite))
    print('Umidade: {}'.format(umidade))
    print('Velocidade do vento: {}'.format(velocidadevento))
    print('Nascer do sol: {}'.format(nascesol)+' Pôr do sol: {}'.format(porsol))
    print('Condição de tempo atual: {}'.format(condicaotempo))

    condicoes_semanais = json.loads(requisicao.text)
    #condicoes_semanais = list(requisicao.json())
    forecast = [condicoessemanais['results']['forecast']]
    for p in forecast:
        print(p[0],p[1],p[2],p[3],p[4],p[5],p[6])
        #print('Temperaturas máximas da semana:')
        maximo = p[0]['max'],p[1]['max'],p[2]['max'],p[3]['max'],p[4]['max'],p[5]['max'],p[6]['max']
        #print(maximo)
        #print('Temperaturas mínimas da semana:')
        minimo = p[0]['min'],p[1]['min'],p[2]['min'],p[3]['min'],p[4]['min'],p[5]['min'],p[6]['min']
        #print(minimo)

    somamaximo = 0
    somaminimo = 0

    for p in forecast:
       somamaximo = sum(maximo)
       #print(f'Soma das temperaturas máximas da semana: {soma_maximo}')

    for p in forecast:
        somaminimo = sum(minimo)
        #print(f'Soma das temperaturas máximas da semana: {soma_minimo}')
    
    mediamaximo = soma_maximo/7
    mediaminimo = soma_minimo/7
    print(f'Média da temperatura máxima da semana: {media_maximo}')
    print(f'Média da temperatura mínima da semana: {media_minimo}')
