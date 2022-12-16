import os
import pickle
from alimentO import alimento
from pacient import paciente
from pacient import verLetras

cafeManha = {}
try:
  arqCafeManha = open("cafeManha.dat", "rb")
  cafeManha = pickle.load(arqCafeManha)
  arqCafeManha.close()
except:
  arqcafeManha = open("cafeManha.dat", "wb")
  arqcafeManha.close()

almoco = {}
try:
  arqalmoco = open("almoco.dat", "rb")
  almoco = pickle.load(arqalmoco)
  arqalmoco.close()
except:
  arqalmoco = open("almoco.dat", "wb")
  arqalmoco.close()

lanche = {}
try:
  arqlanche = open("lanche.dat", "rb")
  lanche = pickle.load(arqlanche)
  arqlanche.close()
except:
  arqlanche = open("lanche.dat", "wb")
  arqlanche.close()

janta = {}
try:
  arqjanta = open("janta.dat", "rb")
  janta = pickle.load(arqjanta)
  arqjanta.close()
except:
  arqjanta = open("janta.dat", "wb")
  arqjanta.close()

def atualizarArquivoCafe():
  arqCafeManha = open("cafeManha.dat", "wb")
  pickle.dump(cafeManha, arqCafeManha)
  arqCafeManha.close()

def atualizarArquivoAlmoco():
  arqalmoco = open("almoco.dat", "wb")
  pickle.dump(almoco, arqalmoco)
  arqalmoco.close()

def atualizarArquivoLanche():
  arqlanche = open("lanche.dat", "wb")
  pickle.dump(lanche, arqlanche)
  arqlanche.close()

def atualizarArquivoJanta():
  arqjanta = open("janta.dat", "wb")
  pickle.dump(janta, arqjanta)
  arqjanta.close()

def analisarJanta():
  vdd = 'Inválido'
  while vdd == 'Inválido':
    janta = input('Qual a janta? ')
    janta = janta.strip()
    vdd = verLetras(janta)
    if vdd == 'Inválido':
      print()
      print(vdd)
      print()

  return vdd
  
def analisarLanche():
  vdd = 'Inválido'
  while vdd == 'Inválido':
    lanche = input('Qual o lanche? ')
    lanche = lanche.strip()
    vdd = verLetras(lanche)
    if vdd == 'Inválido':
      print()
      print(vdd)
      print()

  return vdd

def analisarAlmoco():
  vdd = 'Inválido'
  while vdd == 'Inválido':
    almoco = input('Qual o almoço? ')
    almoco = almoco.strip()
    vdd = verLetras(almoco)
    if vdd == 'Inválido':
      print()
      print(vdd)
      print()

  return vdd

def analisarCafe():
  vdd = 'Inválido'
  while vdd == 'Inválido':
    cafe = input('Qual o café da manhã? ')
    cafe = cafe.strip()
    vdd = verLetras(cafe)
    if vdd == 'Inválido':
      print()
      print(vdd)
      print()

  return vdd

#função para calcular a dieta de manutenção (manter o peso)
def calculoManu(dicionario):
  print('\nDieta de manutenção')

  for y in dicionario: #irá calcular os nutrientes de cada refeição para a dieta de manutenção, deixando as informações dos alimentos cadastrados no módulo alimento da forma que estavam
    print()
    print(y)
    print('\nAlimentos:\n')
    print()
    for i in dicionario[y]:
      for ali in alimento:
        if ali == i:
          if alimento[ali][1] == '100': #calcular de acordo com 100g
            print('Alimento: ' , alimento[ali][0] , '\nQuantidade: ' , alimento[ali][1] , 'g\nProteínas: ' , alimento[ali][2] , 'g\nGordura: ' , alimento[ali][3] , 'g\nCarboidrato: ' , alimento[ali][4] , 'g')
            print()
            
          elif alimento[ali][1] == '1': #calcular de acordo 1unid
            print('Alimento: ' , alimento[ali][0] , '\nQuantidade: ' , alimento[ali][1] , 'unid\nProteínas: ' , alimento[ali][2] , 'g\nGordura: ' , alimento[ali][3] , 'g\nCarboidrato: ' , alimento[ali][4] , 'g')
            print()

  input('Pressione ENTER')

#função para calcular a dieta de superávit calórico (ganho de massa)
def calculoSuper(dicionario):
  print('\nDieta de superávit calórico')

  for y in dicionario: #irá calcular os nutrientes de cada refeição para a dieta de superávit calórico, multiplicando as informações dos alimentos cadastrados no módulo alimento por 2
    print()
    print(y) #y vai recebendo o valor da chave do dicionário
    print('\nAlimentos:\n')
    print()
    for i in dicionario[y]:
      for ali in alimento:
        if ali == i:
          if alimento[ali][1] == '100': #calcular de acordo com 100g
            print('Alimento: ' , alimento[ali][0], '\nQuantidade: ' , float(alimento[ali][1]) * 2 , 'g\nProteínas: ' , float(alimento[ali][2]) * 2 , 'g\nGordura: ' , float(alimento[ali][3]) * 2 , 'g\nCarboidrato: ' , float(alimento[ali][4]) * 2 , 'g')
            print()
            
          elif alimento[ali][1] == '1': #calcular de acordo com 1unid
            print('Alimento: ' , alimento[ali][0], '\nQuantidade: ' , float(alimento[ali][1]) * 2, 'unid\nProteínas: ' , float(alimento[ali][2]) * 2 , 'g\nGordura: ' , float(alimento[ali][3]) * 2 , 'g\nCarboidrato: ' , float(alimento[ali][4]) * 2 , 'g')
            print()

  input('Pressione ENTER')

#função para calcular a dieta de déficit calórico (perda de gordura)
def calculoDeficit(dicionario):
  print('\nDieta de défict calórico')

  for y in dicionario: #irá calcular os nutrientes de cada refeição para a dieta de déficit calórico, dividindo as informações dos alimentos cadastrados no módulo alimento por 2
    print(y) #y vai recebendo o valor da chave do dicionário
    print('\nAlimentos:\n')
    print()
    for i in dicionario[y]: #é um dicionário que ele recebeu de algum lugar
      for ali in alimento:
        if ali == i:
          if alimento[ali][1] == '100': #calcular de acordo com 100g
            print('Alimento: ' , alimento[ali][0], '\nQuantidade: ' , float(alimento[ali][1]) / 2 , 'g\nProteínas: ' , float(alimento[ali][2]) / 2 , 'g\nGordura: ' , float(alimento[ali][3]) / 2 , 'g\nCarboidrato: ' , float(alimento[ali][4]) / 2 , 'g')
            print()
            
          elif alimento[ali][1] == '1': #calcular de acordo com 1unid
            print('Alimento: ' , alimento[ali][0], '\nQuantidade: ' , float(alimento[ali][1]) / 2, 'unid\nProteínas: ' , float(alimento[ali][2]) / 2 , 'g\nGordura: ' , float(alimento[ali][3]) / 2 , 'g\nCarboidrato: ' , float(alimento[ali][4]) / 2 , 'g')
            print()

  input('Pressione ENTER')

#função para deletar janta:
def delJanta():
  for jant in janta: #exibindo o que tem na janta
    print()
    print(jant)
    print('\nAlimentos:\n')
    for i in janta[jant]: 
      print(i)

  delete = input('\nQual opção deseja apagar? ')
  
  if int(delete) <= len(janta) and int(delete) > 0:   
    print()
    encontrarChave = 'Opção ' + delete + ':' #inserindo em opção o número que o usuário digitar, de acordo com a quantidade de elementos que tem no dicionário e sendo maior que 0
    
    contador = 0
    vdd = False #validação
    
    for jant in janta: #olhando no dicionário onde está a opção que o usuário digitou
      contador = contador + 1 #sempre que achar uma chave, ele colocará no contador
      if jant == encontrarChave: #compara se a chave é a que queremos apagar, se for:
        vdd = True
        if vdd == True: #se ele encontrar, ele armazena a posição
          aux2 = str(contador) #aux2 armazena qual a 'posição' que o usuário escolheu estava
  
    confirmar = input('\nVocê deseja mesmo apagar?\n') 
    
    if confirmar.upper() == 'SIM' or confirmar.upper() == 'S': 
      del janta[encontrarChave] #deleta a opção/chave que ele escolheu
      print('Opção excluída com sucesso!')
    
      listaxu1 = []
      listaxu2 = []
      
      for jant in janta: #percorre o dicionário
        jant2 = jant #essa variável receberá a chave jant
        divisao = jant2.find(' ')
        aux3 = jant2[divisao:]
        divisao2 = aux3.find(':') 
        #essas 4 linhas acima servem para pegar o número que está junto com a opção
      
        if int(aux3[:divisao2]) >= int(aux2): #irá comparar se o número extraído da opção é igual ou maior que a posição que foi excluída
          aux2 = str(aux2) 
          novaPosic = int(aux3[:divisao2]) - 1
          novaChave = 'Opção ' + str(novaPosic) + ':'
#criará uma nova chave menor que a anterior para a sequência ficar correta        
          listaxu1 = listaxu1 + [jant] #salva a opção de antes
          listaxu2 = listaxu2 + [novaChave] #salva a nova opção, ou seja, armazena a próx chave
          
      tamanho1 = len(listaxu1) 
      
      for pos in range(tamanho1): #percorre a lista e troca os valores das chaves. Caso ela esteja vazia, ele não entrará
        aux4 = listaxu2[pos]
        aux5 = listaxu1[pos]
      
        janta[aux4] = janta[aux5] #na nova chave (aux4) vai receber o que se tinha na aux5, em seguida apaga a chave aux5
        del janta[aux5]

    else:
      print('\nComando cancelado\n')

  else:
    print('\nEssa opção não existe.')
  
  input('Pressione ENTER')

  atualizarArquivoJanta()

#função para deletar lanche:
def delLanche():
  for lanch in lanche: #exibindo o que tem no lanche
    print()
    print(lanch)
    print('\nAlimentos:\n')
    for i in lanche[lanch]: 
      print(i)

  delete = input('\nQual opção deseja apagar? ')
  
  if int(delete) <= len(lanche) and int(delete) > 0: 
    print()
    encontrarChave = 'Opção ' + delete + ':' #inserindo a opção o número que o usuário digitar, de acordo com a quantidade de elementos que tem no dicionário e sendo maior que 0
    
    contador = 0
    vdd = False #validação
    
    for lanch in lanche: #olhando no dicionário onde está a opção que o usuário digitou
      contador = contador + 1 #sempre que achar uma chave, ele colocará no contador
      if lanch == encontrarChave: #compara se a chave é a que queremos apagar, se for:
        vdd = True
        if vdd == True: #se ele encontrar, ele armazena a posição
          aux2 = str(contador) #aux2 armazena qual a 'posição' que o usuário escolheu estava
  
    confirmar = input('\nVocê deseja mesmo apagar?\n') 
    
    if confirmar.upper() == 'SIM' or confirmar.upper() == 'S': 
      del lanche[encontrarChave] #deleta a opção/chave que ele escolheu
      print('Opção excluída com sucesso!')
    
      listaxu1 = []
      listaxu2 = []
      
      for lanch in lanche: #percorre o dicionário
        lanch2 = lanch #essa variável vai receber a chave lanch
        divisao = lanch2.find(' ')
        aux3 = lanch2[divisao:]
        divisao2 = aux3.find(':') 
      #essas quatro linhas servem para pagar o npumero que está junto com a opção
      
        if int(aux3[:divisao2]) >= int(aux2): #irá comparar se o número extraído da opção é igual ou maior que a posição que foi excluída
          aux2 = str(aux2) 
          novaPosic = int(aux3[:divisao2]) - 1
          novaChave = 'Opção ' + str(novaPosic) + ':'
          #criará uma nova chave menor que a anterior para a sequência ficar correta
        
          listaxu1 = listaxu1 + [lanch] #salva a opção de antes
          listaxu2 = listaxu2 + [novaChave] #salva a nova opção, ou seja, armazena a próx chave
          
      tamanho1 = len(listaxu1) 
      
      for pos in range(tamanho1): #percorre a lista e troca os valores das chaves. Caso esteja vazia, ele não vazia
        aux4 = listaxu2[pos]
        aux5 = listaxu1[pos]
      
        lanche[aux4] = lanche[aux5] #na nova chave (aux4) vai receber o que se tinha na aux5, em seguida apaga a chave aux5
        del lanche[aux5]

    else:
      print('\nComando cancelado\n')
      
  else:
    print('\nEssa opção não existe.')
  
  input('Pressione ENTER')

  atualizarArquivoLanche()

#função para deletar o almoço:
def delAlmoco():
  for almoc in almoco: #Exibindo o que tem no almoço
    print()
    print(almoc)
    print('\nAlimentos:\n')
    for i in almoco[almoc]: 
      print(i)

  delete = input('\nQual opção deseja apagar? ') 

  if int(delete) <= len(almoco) and int(delete) > 0:   
    print()
    encontrarChave = 'Opção ' + delete + ':' #inserindo em opção o número que o usuário digitar, de acordo com a quantidade de elementos que tem no dicionário e sendo maior que 0
    
    contador = 0
    vdd = False #validação
    
    for almoc in almoco: #olhando no dicionário onde está a opção que o usuário digitou
      contador = contador + 1 #sempre que achar uma chave, ele colocará no contador
      if almoc == encontrarChave: #compara se a chave é a que queremos apagar, se for:
        vdd = True
        if vdd == True: #se ele encontrar, ele armazena a posição
          aux2 = str(contador) #aux2 armazena qual a 'posição' que o usuário escolheu estava
  
    confirmar = input('\nVocê deseja mesmo apagar?\n') 
    
    if confirmar.upper() == 'SIM' or confirmar.upper() == 'S': 
      del almoco[encontrarChave] #deleta a opção/chave que ele digitou
      print('Opção excluída com sucesso!')
      
      listaxu1 = []
      listaxu2 = []
      
      for almoc in almoco: #percorrer o dicionário
        almoc2 = almoc #essa variável vai receber a chave almoc
        divisao = almoc2.find(' ')
        aux3 = almoc2[divisao:]
        divisao2 = aux3.find(':') 
      #essas 4 linhas acima servem para pegar o número que está junto com a opção
        
        if int(aux3[:divisao2]) >= int(aux2): #irá comparar se o número extraído da opção é igual ou maior que a posição que foi excluiída
          aux2 = str(aux2) 
          novaPosic = int(aux3[:divisao2]) - 1
          novaChave = 'Opção ' + str(novaPosic) + ':'
        #criará uma nova chave menor que a anterior para a sequência ficar correta
          listaxu1 = listaxu1 + [almoc] #salva a opção de antes
          listaxu2 = listaxu2 + [novaChave] #salva a nova opção, ou seja, armazena a próx chave
          
      tamanho1 = len(listaxu1) 
      
      for pos in range(tamanho1): #percorre a lista e troca os valores das chaves. Caso esteja vazia, ele não entrará
        aux4 = listaxu2[pos]
        aux5 = listaxu1[pos]
      
        almoco[aux4] = almoco[aux5] #na nova chave (aux4) vai receber o que se tinha na aux5, em seguida apaga a chave aux5
        del almoco[aux5]

    else:
      print('\nComando cancelado\n')
            
  else:
    print('\nEssa opção não existe.')
    
  input('Pressione ENTER')

  atualizarArquivoAlmoco()

#função para deletar café da manhã:
def delCafe():
  for cafe in cafeManha: #Exibindo o que tem no café da manhã
    print()
    print(cafe)
    print('\nAlimentos:\n')
    for i in cafeManha[cafe]: 
      print(i)

  delete = input('\nQual opção deseja apagar? ') #Perguntando ao usuário qual opção ele deseja apagar

  if int(delete) <= len(cafeManha) and int(delete) > 0:
    print()
    encontrarChave = 'Opção ' + delete + ':' #Inserindo em opção o número que o usuário digitar, de acordo com a quantidade de elementos que tem no dicionário e sendo maior qu 0
    
    contador = 0
    vdd = False # Validação
    
    for cafe in cafeManha: # Olhando no dicionário onde está a opção que o usuário digitou.
      contador = contador + 1 #sempre que achar uma chave, ele colocará no contador
      if cafe == encontrarChave: # Compara se a chave é a que queremos apagar, se for:
        vdd = True
        if vdd == True: # Se ele encontrar, ele armazena a posição
          aux2 = str(contador) # Aux2 armazena qual a "posição" que o usuário escolheu estava.
    
    confirmar = input('\nVocê deseja mesmo apagar?\n') # Pergunta se o usuário deseja mesmo apagar a posição.
    
    if confirmar.upper() == 'SIM' or confirmar.upper() == 'S': # Se ele quiser apagar mesmo, digita Sim ou apenas S
      del cafeManha[encontrarChave] # Deleta a opção/chave que ele escolheu.
      print('Opção excluída com sucesso!')
    
      listaxu1 = []
      listaxu2 = []
      
      for cafe in cafeManha: # Percorrer o dicionário
        cafe2 = cafe #essa variável vai receber a chave cafe
        divisao = cafe2.find(' ')
        aux3 = cafe2[divisao:]
        divisao2 = aux3.find(':') 
        # Essas quatro linhas servem para pegar o número que está junto com a opção.
        if int(aux3[:divisao2]) >= int(aux2): # Irá comparar se o número extraido da opção é igual ou maior que a posição que foi excluída. 
          aux2 = str(aux2) #
          novaPosic = int(aux3[:divisao2]) - 1
          novaChave = 'Opção ' + str(novaPosic) + ':'
     # Criará uma nova chave menor que a anterior para a sequência ficar correta.
          
          listaxu1 = listaxu1 + [cafe] #salva a opção de antes
          listaxu2 = listaxu2 + [novaChave] #salva a nova opção, ou seja, armazena a próx chave
          
      tamanho1 = len(listaxu1) 
      
      for pos in range(tamanho1): # Percorre a lista e troca os valores das chaves. Caso esteja vazia, ele não vai entrar 
        aux4 = listaxu2[pos]
        aux5 = listaxu1[pos]
      
        cafeManha[aux4] = cafeManha[aux5] #na nova chave (aux4) vai receber o que se tinha na aux5, em seguida apaga a chave aux5
        del cafeManha[aux5]

    else:
      print('\nComando cancelado\n')
      
  else:
    print('\nEssa opção não existe.')

  input('Pressione ENTER')
  # Este trabalho foi feito com muito amor e carinho
  # By: Dayanne, Manu
  # Participação especial nos comentários: Italo Maurício

  atualizarArquivoCafe()

#tela para ver café:
def telaVerCafe():
  os.system('clear')
  print()
  print('==============================================')
  print('================== Ver café  =================')
  print('==============================================')
  print()
  print('\t1 - Manutenção')
  print('\t2 - Superávit calórico')
  print('\t3 - Déficit calórico')
  print('\t0 - Voltar ao menu café')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  print()

  return esc

#função para ver café:
def verCafe():
  esc = telaVerCafe()
  
  while esc != '0':
    if esc == '1':
      calculoManu(cafeManha)
    elif esc == '2':
      calculoSuper(cafeManha)
    elif esc == '3':
      calculoDeficit(cafeManha)
    else:
      print('Escolha inváida')
    esc = telaVerCafe()
#o while chama as funções calculoManu, calculoSuper e calculoDeficit. Eles vão receber o parâmetro café, para saber que é o dicionário que está sendo usado e fazer os cálculos posteriormente

#tela ver almoço:
def telaVerAlmoco():
  os.system('clear')
  print()
  print('==============================================')
  print('================ Ver almoço  =================')
  print('==============================================')
  print()
  print('\t1 - Manutenção')
  print('\t2 - Superávit calórico')
  print('\t3 - Déficit calórico')
  print('\t0 - Voltar ao menu almoço')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')

  return esc

#função para ver o almoço:
def verAlmoco():
  esc = telaVerAlmoco()
  
  while esc != '0':
    if esc == '1':
      calculoManu(almoco) #aquele dicionário vão recebendo esses
    elif esc == '2':
      calculoSuper(almoco)
    elif esc == '3':
      calculoDeficit(almoco)
    else:
       print('Seleção inválida') 
    print()
    
    esc = telaVerAlmoco()
#o while chama as funções calculoManu, calculoSuper e calculoDeficit. Eles vão receber o parâmetro almoço, para saber que é o dicionário que está sendo usado e fazer os cálculos posteriormente
    
#tela para ver lanche:
def telaVerLanche():
  os.system('clear')
  print()
  print('==============================================')
  print('================ Ver lanche  =================')
  print('==============================================')
  print('\t1 - Manutenção')
  print('\t2 - Superávit calórico')
  print('\t3 - Déficit calórico')
  print('\t0 - Voltar ao menu lanche')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  
  return esc

#função para ver lanche:
def verLanche():
  esc = telaVerLanche()

  while esc != '0':
    if esc == '1':
      calculoManu(lanche)
    elif esc == '2':
      calculoSuper(lanche)
    elif esc == '3':
      calculoDeficit(lanche)
    else:
       print('Seleção inválida') 
    print()
    
    esc = telaVerLanche()
#o while chama as funções calculoManu, calculoSuper e calculoDeficit. Eles vão receber o parâmetro lanche, para saber que é o dicionário que está sendo usado e fazer os cálculos posteriormente
    
#tela ver janta:
def telaVerJanta():
  os.system('clear')
  print()
  print('==============================================')
  print('================== Ver janta  ================')
  print('==============================================')
  print()
  print('\t1 - Manutenção')
  print('\t2 - Superávit calórico')
  print('\t3 - Déficit calórico')
  print('\t0 - Voltar ao menu janta')
  print('==============================================')
  esc = input('Selecione sua opção: ')

  return esc

#função para ver janta:
def verJanta():
  esc = telaVerJanta()

  while esc != '0':
    if esc == '1':
      calculoManu(janta)
    elif esc == '2':
      calculoSuper(janta)
    elif esc == '3':
      calculoDeficit(janta)
    else:
      print('Seleção inválida') 
    print()
      
    esc = telaVerJanta()
    
#o while chama as funções calculoManu, calculoSuper e calculoDeficit. Eles vão receber o parâmetro janta, para saber que é o dicionário que está sendo usado e fazer os cálculos posteriormente

  
#função para sugerir janta:
def sugJanta():
  os.system('clear')
  print()
  print('==============================================')
  print('=============== Sugestão Janta  ==============')
  print('==============================================')

  jant = analisarJanta()
  listJanta = [] #lista vazia

  while jant != '0':
    listJanta = listJanta + [jant] #adiciona aqui na lista
    jant = input('\nMais algum alimento para a sua sugestão? Caso queira encerrar, digite 0.\n')

  #ver se o alimento está cadastrado:
  listaxu = []
  for i in range(len(listJanta)): #percorre a lista janta salva
    if listJanta[i] not in alimento: #se o que estiver na lista janta não estiver cadastrado no dicionário, ele será adicionado na lista aux
      listaxu = listaxu + [listJanta[i]]
      
  if len(listaxu) != 0:
    for i in range(len(listaxu)):
      print('\n' , listaxu[i] , 'esse alimento ainda não foi cadastrado no Menu Alimento.')
    print('\nPor favor, dê outra sugestão, ou cadastre o alimento no Menu Alimento para cadastrar uma nova refeição.')
  else:
#surgiu uma questão de como faríamos para saber qual seria o número da opção que iriamos cadastrar, para resolver isso, primeiro lemos quantas chaves tem na nossa dicionário, em seguida somamos essa opção com '1', pois assim saberemos qual será a opção seguinte, depois mudamos para string,  após isso, juntamos na variavel 'novaChave'
    
    tamanho = len(janta)
    proximaChave = tamanho + 1
    proximaChave = str(proximaChave)
    chave = 'Opção ' + proximaChave + ':'

    janta[chave] = listJanta #aqui adiciona no dicionário
    
  input('Digite ENTER')
  
  atualizarArquivoJanta()

#função para sugerir lanche:
def sugLanche():
  os.system('clear')
  print()
  print('==============================================')
  print('============= Sugestão Lanche  ===============')
  print('==============================================')

  lanch = analisarLanche()
  listLanche = []

  while lanch != '0':
    listLanche = listLanche + [lanch] #adiciona aqui na lista
    lanch = input('\nMais algum alimento para a sua sugestão? Caso queira encerrar, digite 0.\n')

  #ver se o alimento está cadastrado:
  listaxu = []
  for i in range(len(listLanche)): #percorre a lista salva
    if listLanche[i] not in alimento: #se o que estiver na lista lanche não estiver cadastrado no dicionário, ele será adicionado na lista aux
      listaxu = listaxu + [listLanche[i]]
      
  if len(listaxu) != 0:
    for i in range(len(listaxu)):
      print('\n' , listaxu[i] , ' ainda não foi cadastrado no Menu Alimento.')
    print('\nPor favor, dê outra sugestão, ou cadastre o alimento no Menu Alimento para cadastrar uma nova refeição.')
  else:
#surgiu uma questão de como faríamos para saber qual seria o número da opção que iriamos cadastrar, para resolver isso, primeiro lemos quantas chaves tem na nossa dicionário, em seguida somamos essa opção com '1', pois assim saberemos qual será a opção seguinte, depois mudamos para string,  após isso, juntamos na variavel 'novaChave'

    tamanho = len(lanche)
    proximaChave = tamanho + 1
    proximaChave = str(proximaChave)
    novaChave  = 'Opção ' + proximaChave + ':'
    
    lanche[novaChave] = listLanche #aqui adiciona no dicionário

  input('Digite ENTER')
  
  atualizarArquivoLanche()


#Função que é para sugerir almoço
def sugAlmoco():
  os.system('clear')
  print()
  print('==============================================')
  print('============= Sugestão Almoço  ===============')
  print('==============================================')

  almoc = analisarAlmoco()
  listAlmoco = []  #lista vazia

  while almoc != '0':
    listAlmoco = listAlmoco + [almoc] #adiciona aqui na lista 
    almoc = input('\nMais algum alimento para a sua sugestão? Caso queira encerrar, digite 0.\n')

  #ver se o alimento está cadastrado
  listaxu = []
  for i in range(len(listAlmoco)): #percorre a lista almoço salva
    if listAlmoco[i] not in alimento: #se o que estiver na lista almoço não estiver cadastrado no dicionário, ele será adicionado na lista aux
      listaxu = listaxu + [listAlmoco[i]]

  if len(listaxu) != 0:
    for i in range(len(listaxu)):
      print('\n' , listaxu[i] , 'esse alimento ainda não foi cadastrado no Menu Alimento.')
    print('\nPor favor, dê outra sugestão, ou cadastre o alimento no Menu Alimento para cadastrar uma nova refeição.')
  else:
#surgiu uma questão de como faríamos para saber qual seria o número da opção que iriamos cadastrar, para resolver isso, primeiro lemos quantas chaves tem na nossa dicionário, em seguida somamos essa opção com '1', pois assim saberemos qual será a opção seguinte, depois mudamos para string,  após isso, juntamos na variável 'novaChave'
    
    tamanho = len(almoco)
    proximaChave = tamanho + 1
    proximaChave = str(proximaChave)
    novaChave = 'Opção ' + proximaChave + ':'

    almoco[novaChave] = listAlmoco #aqui adiciona no dicionário
    
  input('Digite ENTER')
  atualizarArquivoAlmoco()

#Função que é para sugerir café da manhã
def sugCafe():
  print()
  print('==============================================')
  print('=========== Sugestão Café da manhã ===========')
  print('==============================================')

  cafe = analisarCafe()
  listCafe = [] #lista vazia
  
  while cafe != 'n':
    listCafe = listCafe + [cafe]  #adiciona aqui na lista
    cafe = analisarCafe()

  #ver se o alimento está cadastrado
  listaxu = []
  for i in range(len(listCafe)): #percorre a lista café salva
    if listCafe[i] not in alimento: #se o que estiver na lista café não estiver cadastrado no dicionário, ele será adicionado na lista aux
      listaxu = listaxu + [listCafe[i]]

  if len(listaxu) != 0:
    for i in range(len(listaxu)):
      print('\n' , listaxu[i] , 'esse alimento ainda não foi cadastrado no Menu Alimento.')
    print('\nPor favor, dê outra sugestão, ou cadastre o alimento no Menu Alimento para cadastrar uma nova refeição.')
  else:
#surgiu uma questão de como faríamos para saber qual seria o número da opção que iriamos cadastrar, para resolver isso, primeiro lemos quantas chaves tem na nossa dicionário, em seguida somamos essa opção com '1', pois assim saberemos qual será a opção seguinte, depois mudamos para string,  após isso, juntamos na variavel 'novaChave'
  
    tamanho = len(cafeManha)
    proximaChave = tamanho + 1
    proximaChave = str(proximaChave)
    novaChave = 'Opção ' + proximaChave + ':'    
    cafeManha[novaChave] = listCafe #posteriormente adiciona no dicionário

  input('Digite ENTER')
  
  atualizarArquivoCafe() 
  
#tela de café:
def telaChamarCafe():
  os.system('clear')
  print()
  print('==============================================')
  print('================ Café da manhã ===============')
  print('==============================================')
  print()
  print('\t1 - Ver café da manhã')
  print('\t2 - Sugerir um café da manhã')
  print('\t3 - Deletar uma opção de café da manhã')
  print('\t0 - Voltar ao menu refeição')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  print()

  return esc

#essa função será chamada para ver as opções do café:
def chamarCafe():
  esc = telaChamarCafe()

  while esc != '0':
    if esc == '1':
      verCafe()
    elif esc == '2':
      sugCafe()
    elif esc == '3':
      delCafe()
    else:
      print('Escolha inválida')
    esc = telaChamarCafe()
#o while chama outras funções, a tela, verCafe, sugCafe, delCafe...

#Tela de almoço:
def telaChamarAlmoco():
  os.system('clear')
  print()
  print('==============================================')
  print('=================== Almoço ===================')
  print('==============================================')
  print()
  print('\t1 - Ver almoço')
  print('\t2 - Sugerir um almoço')
  print('\t3 - Deletar uma opção de almoço')
  print('\t0 - Voltar ao menu refeição')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  print()

  return esc

#essa função será chamada para ver as opções do almoço:
def chamarAlmoco():
  esc = telaChamarAlmoco()
  
  while esc != '0':
    if esc == '1':
      verAlmoco()
    elif esc == '2':
      sugAlmoco()
    elif esc == '3':
      delAlmoco()
    else:
      print('Escolha inváida')
    esc = telaChamarAlmoco()
#o while chama outras funções, a tela, verAlmoco, sugAlmoco, delAlmoco...
    
#Tela do lanche:
def telaChamarLanche():
  os.system('clear')
  print()
  print('==============================================')
  print('=================== Lanche ===================')
  print('==============================================')
  print()
  print('\t1 - Ver lanche')
  print('\t2 - Sugerir um lanche')
  print('\t3 - Deletar uma opção de lanche')
  print('\t0 - Voltar ao menu refeição')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  print()

  return esc

#essa função será chamada para ver as opções do lanche
def chamarLanche():
  esc = telaChamarLanche()
  
  while esc != '0':
    if esc == '1':
      verLanche()
    elif esc == '2':
      sugLanche()
    elif esc == '3':
      delLanche()
    else:
      print('Escolha inválida')
    esc = telaChamarLanche()
#o while chama outras funções, a tela, verLanche, sugLanche, delLanche...

#tela para ver as opções de janta
def telaChamarJanta():
  os.system('clear')
  print()
  print('==============================================')
  print('=================== Janta ====================')
  print('==============================================')
  print()
  print('\t1 - Ver janta')
  print('\t2 - Sugerir uma janta')
  print('\t3 - Deletar uma opção de janta')
  print('\t0 - Voltar ao menu refeição')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  print()
  return esc

#essa função será chamada para ver as opções da janta
def chamarJanta():
  esc = telaChamarJanta()
 
  while esc != '0':
    if esc == '1':
      verJanta()
    elif esc == '2':
      sugJanta()
    elif esc == '3':
      delJanta()
    else:
      print('Escolha inváida')
    esc = telaChamarJanta()
#o while chama outras funções, a tela, verJanta, sugJanta, delJanta...

def menuCardapio():
  os.system('clear')
  print('==============================================')
  print('================= CARDÁPIO ===================')
  print('==============================================')
  print()
  print('\t1 - Café da manhã')
  print('\t2 - Almoço')
  print('\t3 - Lanche')
  print('\t4 - Janta')
  print('\t0 - Voltar ao menu principal')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  print()
  return esc

def escPorCardapio():
  os.system('clear')
  esc = menuCardapio()

  while esc != '0':
    if esc == '1':
      chamarCafe()
      
    elif esc == '2':
      chamarAlmoco()
          
    elif esc == '3':
      chamarLanche()
      
    elif esc == '4':
      chamarJanta()
      
    else:
      print('Seleção inválida') 
    print()

    esc = menuCardapio()

def refeicaoPorPac(dicionario):
  nome = input('Digite o nome do paciente: ')

  vdd = False
  
  for pac in paciente:
    nome2 = paciente[pac][0]
    if nome.upper() == nome2.upper():
      vdd = True
      
      finalidade = paciente[pac][4]

      if finalidade == 'Manutenção':
        calculoManu(dicionario)
    
      elif finalidade == 'Superávit calórico':
        calculoSuper(dicionario)
    
      else:
        calculoDeficit(dicionario)

  if vdd == False:
      print('\nPaciente não cadastrado.')
      

def menuEscPaciente():
  os.system('clear')
  print('==============================================')
  print('============= CARDÁPIO PACIENTE ==============')
  print('==============================================')
  print()
  print('\t1 - Café da manhã')
  print('\t2 - Almoço')
  print('\t3 - Lanche')
  print('\t4 - Janta')
  print('\t0 - Voltar ao menu principal')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  print()
  return esc

def escPorPaciente():
  os.system('clear')
  esc = menuEscPaciente()

  while esc != '0':
    if esc == '1':
      refeicaoPorPac(cafeManha)
      
    elif esc == '2':
      refeicaoPorPac(almoco)
          
    elif esc == '3':
      refeicaoPorPac(lanche)
      
    elif esc == '4':
      refeicaoPorPac(janta)
      
    else:
      print('Seleção inválida') 
    print()

    esc = menuEscPaciente()


def telaSugerirCard():
  os.system('clear')
  print('==============================================')
  print('============= SUGERIR CARDÁPIO ===============')
  print('==============================================')
  print()
  print('\t1 - Café da manhã')
  print('\t2 - Almoço')
  print('\t3 - Lanche')
  print('\t4 - Janta')
  print('\t0 - Voltar ao menu principal')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  print()
  return esc

def escSugerirCard():
  os.system('clear')
  esc = telaSugerirCard()

  while esc != '0':
    if esc == '1':
      sugCafe()
      
    elif esc == '2':
      sugAlmoco()

    elif esc == '3':
      sugLanche()

    elif esc == '4':
      sugJanta()
      
    else:
      print('Seleção inválida') 
    print()

    esc = telaSugerirCard()

  
def menuRefeic():
  os.system('clear')
  print('==============================================')
  print('=============== MENU REFEIÇÃO ================')
  print('==============================================')
  print()
  print('\t1 - Ver cardápio por paciente')
  print('\t2 - Ver todos os cardápios')
  print('\t3 - Sugerir cardápio')
  print('\t0 - Voltar ao menu principal')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  print()
  return esc
  
def moduloRefeic():
  os.system('clear')
  esc = menuRefeic()

  while esc != '0':
    if esc == '1':
      escPorPaciente()
      
    elif esc == '2':
      escPorCardapio()

    elif esc == '3':
      escSugerirCard()
      
    else:
      print('Seleção inválida') 
    print()

    esc = menuRefeic()