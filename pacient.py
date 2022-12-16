import os
import pickle

paciente = {}

try:
   arqPaciente = open("paciente.dat", "rb")
   paciente = pickle.load(arqPaciente)
   arqPaciente.close()
except:
   arqPaciente = open("paciente.dat", "wb")
   arqPaciente.close()
  
def atualizarArquivo():
  arqPaciente = open("paciente.dat", "wb")
  pickle.dump(paciente, arqPaciente)
  arqPaciente.close()

def escolhaDieta():
  aux = 'Inválido'
  while aux == 'Inválido':
    finalidade = input('Qual a finalidade da dieta? Manutenção (1), Superávit calórico(2) ou déficit calórico(3)?\n')
    finalidade = finalidade.strip()
    if finalidade == '1' or finalidade == '2'or finalidade == '3':
      aux = 'Válido'
      if finalidade == '1':
        finalidade = 'Manutenção'
      elif finalidade == '2':
        finalidade = 'Superávit calórico'
      else:
        finalidade = 'Déficit calórico'

      return finalidade
      
    else:
      print('\nEscolha inválida\n')
      aux = 'Inválido'
      
def verLetras(palavra): #função para permitir ingresso apenas de letras
  palavra = palavra.strip()
  
  if palavra.isalpha():
    return palavra
  else:
    return 'Inválido'

def analisarNome():
  vdd = 'Inválido'
  while vdd == 'Inválido':
    nome = input('Qual o nome do paciente? ')
    nome = nome.strip()
    vdd = verLetras(nome)
    if vdd == 'Inválido':
      print()
      print(vdd)
      print()

  return vdd
  
def analisarAltura():
  vdd = 'Inválido'
  while vdd == 'Inválido':
    altura = input('Qual a altura do paciente? ')
    vdd = verifAltVal(altura)
    if vdd == 'Inválido':
      print()
      print(vdd)
      print()

  return vdd
  
def verifIdade(num):
  num = num.strip(' ')
  if len(num) == 0:
    return 'Inválido'
  elif ',' in num:
    num = num.replace(',','.')

  tuplaNum = ('0','1','2','3','4','5','6','7','8','9','.')
  listaux = []
  
  if len(num) == 1 and num == '.':
    return 'Inválido'
  elif len(num) == 2 and num[1] == '.':
    return 'Inválido'
  elif len(num) == 3 and num[2] == '.':
    return 'Inválido'  
  elif len(num) == 2 and num[0] == '.':
    return 'Inválido'
  elif len(num) == 3 and num[0] == '.':
    return 'Inválido'   
    
  elif '.' in num:
    for i in range(len(num)):
      if num[i] == '.':
        listaux = listaux + [num[i]]
          
    if len(listaux) != 1:
      return 'Inválido'
    elif float(num) <= 0:
      return 'Inválido'
      
  for i in range(len(num)):
    if num[i] in tuplaNum:
      listaux = listaux + ['t']
    else:
      listaux = listaux + ['f']
        
  if 'f' in listaux:
    return 'Inválido'
  else:
    if float(num) <= 110:
      return num  
    else:
      return 'Inválido' 

def analisarIdade():
  vdd = 'Inválido'
  while vdd == 'Inválido':
    idade = input('Qual a idade do paciente? ')
    vdd = verifIdade(idade)
    if vdd == 'Inválido':
      print()
      print(vdd)
      print()

  return vdd
def verifPeso(num):
  num = num.strip(' ')
  if len(num) == 0:
    return 'Inválido'
  elif ',' in num:
    num = num.replace(',','.')

  tuplaNum = ('0','1','2','3','4','5','6','7','8','9','.')
  listaux = []
  
  if len(num) == 1 and num == '.':
    return 'Inválido'
  elif len(num) == 2 and num[1] == '.':
    return 'Inválido'
  elif len(num) == 3 and num[2] == '.':
    return 'Inválido'  
  elif len(num) == 4 and num[3] == '.':
    return 'Inválido'
  elif len(num) == 2 and num[0] == '.':
    return 'Inválido'
  elif len(num) == 3 and num[0] == '.':
    return 'Inválido'   
  elif len(num) == 4 and num[0] == '.':
    return 'Inválido'

  elif '.' in num:
    for i in range(len(num)):
      if num[i] == '.':
        listaux = listaux + [num[i]]
          
    if len(listaux) != 1: #porque seriam mais de 1 ponto armazenado
      return 'Inválido'
    elif float(num) <= 0:
      return 'Inválido'
      
  for i in range(len(num)):
    if num[i] in tuplaNum: #num[i] = 'se nessa posição'
      listaux = listaux + ['t']
    else:
      listaux = listaux + ['f']
        
  if 'f' in listaux:
    return 'Inválido'
  else:
    if float(num) <= 300:
      return num  
    else:
      return 'Inválido' 
  
def analisarPeso():
  vdd = 'Inválido'
  while vdd == 'Inválido':
    peso = input('Qual o peso do paciente? ')
    vdd = verifPeso(peso)
    if vdd == 'Inválido':
      print()
      print(vdd)
      print()

  return vdd
def menuPaciente():
  os.system('clear')
  print('==============================================')
  print('=============== MENU PACIENTE ================')
  print('==============================================')
  print()
  print('\t1 - Cadastrar paciente')
  print('\t2 - Editar paciente')
  print('\t3 - Pesquisar paciente')
  print('\t4 - Deletar paciente')
  print('\t0 - Voltar ao menu principal')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  return esc

def imc(alt,pes):
  pes = float(pes)
  alt = float(alt)
  imc = pes / (alt * alt)
  
  return imc

#função para verificação do email que foi cadastrado
def verificarEmail():
  vdd = False
  vdd2 = False
  email = input('Qual o seu email? ')
  
  while vdd2 == False:
    if email in paciente: #se o email já estiver no dicionário, ele afirma que já está cadastrado, então pede outro
      print('\nEmail já cadastrado! Tente outro.\n')
      email = input('Qual o seu email? ')
    else:
      vdd2 = True #se não estiver cadastrado, ele sai desse while e vai para o próx
  
  while vdd == False and vdd2 == True:
    if '@' in email and '.' in email:
      print('\nEmail válido')
      vdd = True
    else:
      print('\nEmail inválido')
      email = input('Qual o seu email? ')

  return email

#função para ajustar a altura e o peso irá receber um parâmetro (ajustar - pergunta) e irá ajeitar caso o paciente cadastre a informação com vírgula no lugar do ponto

def verifAltVal(num):
  #considerando que a menor altura é 0.72 m, e a maior 2.51 m  
  tamanho = len(num)
  
  if tamanho != 0 and tamanho != 2: #não poderia ter altura 12/11...
    if ' ' in num:
      listnum = []
      for i in range(tamanho):
        if num[i] != ' ':
          listnum = listnum + [num[i]]

      tamanho = len(listnum)
      if tamanho > 0 and tamanho < 5 and tamanho != 2:
        if tamanho != 1: #no caso, seria como se ele tivesse digitado 12, não poderia, pois ele não colocou vírgula nem ponto, ou seja, não ficou 1,2...
          if '.' not in listnum and ',' not in listnum:
            return 'Inválido'
            
          else:
            for i in range(tamanho):
              if i == 0:
                num = listnum[i] #vai receber a primeira posição da listnum
              elif i == 1:
                num = num + listnum[i]
              elif i == 2:
                num = num + listnum[i]
              else:
                num = num + listnum[i]

      else:
        return 'Inválido'

    if ',' in num:
      listnum = []
      for i in range(len(num)):
        listnum = listnum + [num[i]]
  
      listaux = []
      for i in range(len(listnum)):
        if listnum[i] == ',':
          listaux = listaux + [listnum[i]]
          
      if len(listaux) != 1: #ou seja, para a vírgula
        return 'Inválido'

      else:
        tamanho = len(listnum)
      
        if tamanho > 0 and tamanho < 5 and tamanho != 2:
          for i in range(tamanho):
            if i == 0:
              num = listnum[i]
            elif i == 1:
              num = num + '.'
            elif i == 2:
              num = num + listnum[i]
            else:
              num = num + listnum[i]

    tuplaNum = ('0','1','2','3','4','5','6','7','8','9','.')
    listaux = []
      
    if len(num) == 1 and num == '.':
      return 'Inválido'
    elif len(num) > 4:
      return 'Inválido'
    elif len(num) != 1:
      if '.' not in num:
        return 'Inválido'
      else:
        for i in range(len(num)):
          if num[i] == '.':
            listaux = listaux + [num[i]]
          
        if len(listaux) != 1:
          return 'Inválido'
        
    vdd = True  
          
    if vdd == True:
      for i in range(len(num)):
        if num[i] in tuplaNum:
          listaux = listaux + ['t'] #se não tiver na tupla, armazena um 't'
        else:
          listaux = listaux + ['f']
        
      if 'f' in listaux:
        return 'Inválido'
      else:
        if float(num) >= 0.72 and float(num) <= 2.51 and len(num) != 2:
          return num
        else:
          return 'Inválido'
                    
  else:
    return 'Inválido'
    
#função de cadastro:
def cadastrarPaciente():
  os.system('clear')
  print()
  print('==============================================')
  print('============= Cadastrar paciente =============')
  print('==============================================')
  email = verificarEmail() #primeiro verifica o email, que é a chave
          
  nome = analisarNome()
  
  idade = analisarIdade()
  
  altura = analisarAltura()

  peso = analisarPeso()

  finalidade = escolhaDieta()

  paciente[email] = [nome, idade, altura, peso, finalidade]
  
  atualizarArquivo()
  
  print('Paciente cadastrado com sucesso!')
  
#tela da função de edição:
def escolhaEditar():
      os.system('clear')
      print('==============================================')
      print()
      print('\t1 - Editar nome')
      print('\t2 - Editar idade')
      print('\t3 - Editar altura')
      print('\t4 - Editar peso')
      print('\t5 - Editar finalidade da dieta')
      print('\t6 - Editar tudo')
      print('\t0 - Cancelar')
      print()
      print('==============================================')
      esc = input('Selecione sua opção: ')
      return esc

def delPaciente():
  print()
  print('==============================================')
  print('============= Deletar pacientes ==============')
  print('==============================================')
  print()
  
  delete = input('Qual paciente deseja deletar? ')
  achou = False
  for pac in paciente:
    if delete in paciente[pac][0]:
      aux = pac
      achou = True
      
# nesse primeiro achou = True, ele vai informar que achou o paciente na posição 0, caso ache, ele entrará nesse novo if e mostrará as opções para deletar
  
  if achou == True:
    print('\nNome: ' , paciente[aux][0] , '\nEmail: ' , aux , '\nIdade: ' , paciente[aux][1], ' anos' , '\nAltura: ' , paciente[aux][2] , ' metros' '\nPeso: ' , paciente[aux][3] , 'quilos' , '\nFinalidade da dieta: ' , paciente[aux][4]) 
    print()
    confirmar = input('Deseja realmente deletar? ')

# upper = comando para identificar as letras em minúsculo e passar para maiúsculo
    
    if confirmar.upper() == 'SIM' or confirmar.upper() == 'S':
      del paciente[aux]
      atualizarArquivo()
      print('Paciente excluído com sucesso!')

  else: 
    print('\nPaciente não cadastrado!')

  input('Pressione ENTER')  

def editarPaciente():
  print()
  print('==============================================')
  print('============== Editar paciente ===============')
  print('==============================================')
  print()
#o pac está percorrendo o dicionário e ele vai assumindo o nome de cada chave que está contida no dicionário, ele analisa se na posição 0 está o nome procurado (1° for)
#paciente[pac][0]: o paciente é o dicionário que estamos acessando, o pac é a chave e a posição 0 é onde se encontra o nome
#a variavel 'achou' é usada para caso se o nome procurado n estiver no dicionario, ele dirá que não tem esse paciente
  
  perg = input('Qual paciente você deseja alterar? ')
  achou = False
  
  for pac in paciente:
    if perg in paciente[pac][0]:
      aux = pac
      achou = True
  
  if achou == False:
    print('Paciente não cadastrado')
  elif achou == True:
    alt = paciente[pac][2]
    pes = paciente[pac][3]
    print('\nNome: ' , paciente[aux][0] , '\nEmail: ' , aux , '\nIdade: ' , paciente[aux][1], ' anos' , '\nAltura: ' , paciente[aux][2] , ' metros' '\nPeso: ' , paciente[aux][3] , 'quilos\n' , imc(alt,pes) , '\nFinalidade da dieta: ' , paciente[aux][4]) 
    
    esc = escolhaEditar() #chama a tela de escolha editar

    while esc != '0':
      if esc == '1': 
        print('Editar nome')
        nome = analisarNome()
        paciente[aux][0] = nome
      elif esc == '2':
        print('Editar idade')
        idade = analisarIdade()
        paciente[aux][1] = idade
      elif esc == '3':
        print('Editar altura')
        altura = analisarAltura()
        paciente[aux][2] = altura
      elif esc == '4':
        print('Editar peso')
        peso = analisarPeso()
        paciente[aux][3] = peso
      elif esc == '5':
        print('Editar finalidade da dieta')
        finalidade = escolhaDieta()
        paciente[aux][4] = finalidade
      else:
        print('Editar todos')
        print()
             
        print('Editar nome')
        nome = analisarNome()
        paciente[aux][0] = nome
        print()
             
        print('Editar idade')
        idade = analisarIdade()
        paciente[aux][1] = idade
        print()

        print('Editar altura')
        altura = analisarAltura()
        paciente[aux][2] = altura
        print()

        print('Editar peso')
        peso = analisarPeso()
        paciente[aux][3] = peso
        print()   

        print('Editar finalidade da dieta')
        finalidade = escolhaDieta()
        paciente[aux][4] = finalidade
        print()

      print('Paciente atualizado com sucesso!')
      esc = escolhaEditar()

def pesquisarPaciente():
  perg = input('\nDigite o nome que deseja encontrar: ')
  for pac in paciente:
    nome = paciente[pac][0]
    nome = nome.upper()
    perg = perg.upper()
    if nome.startswith(perg):
      alt = paciente[pac][2]
      pes = paciente[pac][3]
      
      print('\nNome: ' , paciente[pac][0] , '\nEmail: ' , pac , '\nIdade: ' , paciente[pac][1], ' anos' , '\nAltura: ' , paciente[pac][2] , ' metros' '\nPeso: ' , paciente[pac][3] , 'quilos\nIMC: ' , imc(alt,pes) , '\nFinalidade da dieta: ' , paciente[pac][4]) 
    print()

  input('\nDigite ENTER')
    
def moduloPaciente():
  esc = menuPaciente()

  while esc != '0':
    if esc == '1':
      cadastrarPaciente()
      
    elif esc == '2':
      editarPaciente()
      
    elif esc == '3':
      pesquisarPaciente()
      
    elif esc == '4':
      delPaciente()
      
    else:
      print('Seleção inválida') 
    print()

    esc = menuPaciente() 