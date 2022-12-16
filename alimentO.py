import pickle
import os
from pacient import verLetras

alimento = {}
#dicionário vazio, que vai receber depois as informações

try:
   arqAlimento = open("alimento.dat", "rb") #rb = pede para abrir em modo leitura e binário
   alimento = pickle.load(arqAlimento) #o dicionário recebe aqui o que tem no arquivo alimento
   arqAlimento.close() #fecha o arquivoAlim
  
except:
   arqAlimento = open("alimento.dat", "wb") #wb = escrever em binário
   arqAlimento.close()

#o try tenta recuperar os arquivos e colocar de volta no dicionario, se ele falhar, o except entra em ação, então ele perde o que tinha antes no arquivo e cria outro novo, vazio

def analisarAlim():
  vdd = 'Inválido'
  while vdd == 'Inválido':
    alim = input('Qual o alimento? ')
    alim = alim.strip()
    vdd = verLetras(alim)
    if vdd == 'Inválido':
      print()
      print(vdd)
      print()

  return vdd
  
def verifNum(num):
  num = num.strip(' ')
  if len(num) == 0:
    return 'Inválido'
  elif ',' in num:
    num = num.replace(',','.')

  tuplaNum = ('0','1','2','3','4','5','6','7','8','9','.')
  listaux = []

  tam = len(num)
  if len(num) == 1 and num == '.':
    return 'Inválido'
  elif len(num) == tam and '.' in num[tam - 1]:
    return 'Inválido'
  elif len(num) == tam and '.' in num[0]:
    return 'Inválido'
    
  elif '.' in num:
    for i in range(len(num)): #vai rodando o tamanho
      if num[i] == '.':
        listaux = listaux + [num[i]] #vai adicionar os pontos, ou seja, armazenar os pontinhos aqui
          
    if len(listaux) != 1: #no caso, seria mais de um ponto, dando inválido
      return 'Inválido'
    elif float(num) <= 0: #seria números negativos
      return 'Inválido' 
      
  for i in range(len(num)):
    if num[i] in tuplaNum:
      listaux = listaux + ['t'] #seria "true", para caso tenha na tupla
    else:
      listaux = listaux + ['f'] #false
        
  if 'f' in listaux: #caso tenha encontrado algum que n seja um número
    return 'Inválido'
  else:
      return num  

def analisarCarb():
  vdd = 'Inválido'
  while vdd == 'Inválido':
    carboidrato = input('Qual a quantidade de carboidrato? ')
    vdd = verifNum(carboidrato)
    if vdd == 'Inválido':
      print()
      print(vdd)
      print()

  return vdd
      
def analisarGord():
  vdd = 'Inválido'
  while vdd == 'Inválido':
    gordura = input('Qual a quantidade de gordura? ')
    vdd = verifNum(gordura)
    if vdd == 'Inválido':
      print()
      print(vdd)
      print()

  return vdd

def analisarProt():
  vdd = 'Inválido'
  while vdd == 'Inválido':
    proteina = input('Qual a quantidade de proteína? ')
    vdd = verifNum(proteina)
    if vdd == 'Inválido':
      print()
      print(vdd)
      print()

  return vdd
    
def atualizarArquivo():
  arqalimento = open("alimento.dat", "wb") #apaga 
  pickle.dump(alimento, arqalimento) #adiciona outras informações do dicionário no arquivo. Mesmo que ele perca, ele recupera, pois há o dicionário
  arqalimento.close()
#essa função atualiza o arquivo quando se tem alguma alteração

def gramasUnidade(x):
  if alimento[x][0] == x: # o x recebe o que tinha dentro do aux do e usa nas comparações de if e elif 
        if alimento[x][1] == '100':
          print('Alimento: ' , alimento[x][0] , '\nQuantidade: ' , alimento[x][1] , 'g\nProteínas: ' , alimento[x][2] , 'g\nGordura: ' , alimento[x][3] , 'g\nCarboidrato: ' , alimento[x][4] , 'g')
          
        elif alimento[x][1] == '1':
          print('Alimento: ' , alimento[x][0] , '\nQuantidade: ' , alimento[x][1] , 'und\nProteínas: ' , alimento[x][2] , 'g\nGordura: ' , alimento[x][3] , 'g\nCarboidrato: ' , alimento[x][4] , 'g')

  input('Pressione ENTER')
  
def deletarAlimento():
  print()
  print('==============================================')
  print('============== Deletar alimento ==============')
  print('==============================================')
  alim = input('Qual alimento deseja deletar? ')
  print()
  alim = alim.strip()
  achou = False 
#digitou o alimento, logo ver se esse alimento existe em alimento, para comida em alimento, a chave é 'comida', se nessa chave a primeira posição for igual ao que ele digitou, a chave vai receber alim e o achou = verdade. Se ele tiver realmente achado, ele chama o gramasUnidade(aux) -> função
  
  if alim in alimento:
    for comida in alimento:
      if alimento[comida][0] == alim:
        aux = alim #a variável recebe alim
        achou = True

    if achou == True:
      gramasUnidade(aux)
      
      deletar = input('\nDeseja realmente deletar? ')
      deletar = deletar.strip()
      
      if deletar.upper() == 'SIM' or deletar.upper() == 'S':
        del alimento[aux]
        print('\nAlimento excluído com sucesso!')

        atualizarArquivo()

  else:
    print('\nAlimento não cadastrado')
  
  input('Pressione ENTER')

# função para pesquisar o alimento
  
def pesquisarAlimento():
  print()
  print('==============================================')
  print('============= Pesquisar alimento =============')
  print('==============================================')
  alim = input('Qual alimento deseja ver? ')
  alim = alim.strip()

  if alim in alimento: #vai pegar o que digitou acima e percorrer o dicionário
    for comida in alimento: #comida está assumindo os valores da chave alimento
      
      if comida == alim:
        gramasUnidade(alim) #se a chave for igual a comida digitada, ele irá colocar nessa função que ela irá enviar para a função gramasUnidade 
        
  else:
    print('\nAlimento não cadastrado')

# mesma coisa que o anterior, mas neste caso irá salvar 100g de alimento e não 1 unidade:
    
def alimento100g():
  os.system('clear')
  print('==============================================')
  print('=============== ALIMENTO 100g ================')
  print('==============================================')
  print()
  
  alim = analisarAlim()
  if alim in alimento:
    print('\nAlimento já cadastrado')
  else:
    proteina = analisarProt()
    gordura = analisarGord()
    carboidratos = analisarCarb()
    alimento[alim] = [alim, '100' , proteina, gordura, carboidratos] #armazenam em uma lista, cuja chave é o alim, essa lista vai para os dicionários, que por sua vez será salvo nos arquivos

    input('Pressione ENTER')

#função de cadastrar o alimento pela unidade
    
def alimentoUnidade():
  os.system('clear')
  print('==============================================')
  print('============== ALIMENTO UNIDADE ==============')
  print('==============================================')
  print()
  
  alim = analisarAlim()
  if alim in alimento:
    print('\nAlimento já cadastrado')
  else:
    proteina = analisarProt()
    gordura = analisarGord()
    carboidratos = analisarCarb()
    alimento[alim] = [alim, '1' , proteina, gordura, carboidratos]

    input('Pressione ENTER')

def telaCadastrarALimento():
  os.system('clear')

# tela do cadastro  
  print('==============================================')
  print('============= CADASTRAR ALIMENTO =============')
  print('==============================================')
  print()
  print('\t1 - Cadastrar por unidade')
  print('\t2 - Cadastrar por 100g')
  print('\t0 - Voltar ao menu principal')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')

  return esc
  
# quando seleciona no while do módulo 1, vem para essa função de cadastro
  
def cadastrarAlimento():
  esc = telaCadastrarALimento()

  while esc != '0':
    if esc == '1':
      alimentoUnidade() #aqui cadastra por unidade
      atualizarArquivo() 
     
    elif esc == '2':
      alimento100g() 
      alimentoUnidade() 
      atualizarArquivo()
      # após sair da função alimento100g, ele irá chamar a função que atualiza o arquivo para armazenar lá
    else:
      print('Seleção inválida') 
      
    esc = telaCadastrarALimento()
      
# essa é a tela principal desse módulo:
    
def menuAlimento():
  os.system('clear')
  print('==============================================')
  print('=============== MENU ALIMENTO ================')
  print('==============================================')
  print()
  print('\t1 - Cadastrar alimento')
  print('\t2 - Pesquisar alimento')
  print('\t3 - Deletar alimento')
  print('\t0 - Voltar ao menu principal')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  return esc

# Módulo principal do alimento:
def moduloAlimento():
  os.system('clear')
  esc = menuAlimento()

  while esc != '0':
    if esc == '1':
      cadastrarAlimento()
      
    elif esc == '2':
      pesquisarAlimento()
          
    elif esc == '3':
      deletarAlimento()  

    else:
      print('Seleção inválida') 
    print()

    esc = menuAlimento()