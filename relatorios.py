import os
from pacient import paciente
from pacient import imc
from alimentO import alimento
from refeicao import cafeManha
from refeicao import almoco
from refeicao import lanche
from refeicao import janta

def verPaciente():
  print()
  print('==============================================')
  print('=============== Ver pacientes ================')
  print('==============================================')
  print()
  0
#o for vai ser criado para procurar cada chave, vai recuperar o paciente e as suas informações  
  for pac in paciente: #pac é uma variável que assume o valor da chave ao percorrer o dicionário
    alt = paciente[pac][2] #variáveis que estão sendo recuperada para calcular o IMC
    pes = paciente[pac][3]
     
    print('\nNome: ' , paciente[pac][0] , '\nEmail: ' , pac , '\nIdade: ' , paciente[pac][1], ' anos' , '\nAltura: ' , paciente[pac][2] , ' metros' '\nPeso: ' , paciente[pac][3] , 'quilos\nIMC: ' , imc(alt,pes) , '\nFinalidade da dieta: ' , paciente[pac][4]) 
    print()

  input('Pressione ENTER')

def verAlimentos():
  for x in alimento:
    if alimento[x][0] == x:
          if alimento[x][1] == '100':
            print('Alimento: ' , alimento[x][0] , '\nQuantidade: ' , alimento[x][1] , 'g\nProteínas: ' , alimento[x][2] , 'g\nGordura: ' , alimento[x][3] , 'g\nCarboidrato: ' , alimento[x][4] , 'g')
            print()
            
          elif alimento[x][1] == '1':
            print('Alimento: ' , alimento[x][0] , '\nQuantidade: ' , alimento[x][1] , 'und\nProteínas: ' , alimento[x][2] , 'g\nGordura: ' , alimento[x][3] , 'g\nCarboidrato: ' , alimento[x][4] , 'g')
            print()

  input('Pressione ENTER')


def verCafeManha():
  for cafe in cafeManha: 
    print()
    print(cafe)
    print('\nAlimentos:\n')
    for i in cafeManha[cafe]: 
      print(i)

  input('Pressione ENTER')

def verAlmoco():
  for almoc in almoco: 
    print()
    print(almoc)
    print('\nAlimentos:\n')
    for i in almoco[almoc]: 
      print(i)

  input('Pressione ENTER')

def verLanche():
  for lanch in lanche: 
    print()
    print(lanch)
    print('\nAlimentos:\n')
    for i in lanche[lanch]: 
      print(i)

  input('Pressione ENTER')

def verJanta():
  for jant in janta: 
    print()
    print(jant)
    print('\nAlimentos:\n')
    for i in janta[jant]: 
      print(i)

  input('Pressione ENTER')  

def menuRelatorios():
  os.system('clear')
  print('==============================================')
  print('================= RELATÓRIOS =================')
  print('==============================================')
  print()
  print('\t1 - Relatório Paciente')
  print('\t2 - Relatório Alimento')
  print('\t3 - Relatório Café da Manhã')
  print('\t4 - Relatório Almoço')
  print('\t5 - Relatório Lanche')
  print('\t6 - Relatório Janta')
  print('\t0 - Voltar ao menu principal')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  return esc

def moduloRelatorios():
  esc = menuRelatorios()
  while esc != '0':
    if esc == '1':
      verPaciente()
  
    elif esc == '2':
      verAlimentos()
      
    elif esc == '3':
      verCafeManha()
      
    elif esc == '4':
      verAlmoco()
  
    elif esc == '5':
      verLanche()
  
    elif esc == '6':
      verJanta()
      
    else:
      print('Seleção inválida') 
    print()
    
    esc = menuRelatorios()
  
  print() 
import os
from pacient import paciente
from pacient import imc
from alimentO import alimento
from refeicao import cafeManha
from refeicao import almoco
from refeicao import lanche
from refeicao import janta

def verPaciente():
  print()
  print('==============================================')
  print('=============== Ver pacientes ================')
  print('==============================================')
  print()
  0
#o for vai ser criado para procurar cada chave, vai recuperar o paciente e as suas informações  
  for pac in paciente: #pac é uma variável que assume o valor da chave ao percorrer o dicionário
    alt = paciente[pac][2] #variáveis que estão sendo recuperada para calcular o IMC
    pes = paciente[pac][3]
     
    print('\nNome: ' , paciente[pac][0] , '\nEmail: ' , pac , '\nIdade: ' , paciente[pac][1], ' anos' , '\nAltura: ' , paciente[pac][2] , ' metros' '\nPeso: ' , paciente[pac][3] , 'quilos\nIMC: ' , imc(alt,pes) , '\nFinalidade da dieta: ' , paciente[pac][4]) 
    print()

  input('Pressione ENTER')

def verAlimentos():
  for x in alimento:
    if alimento[x][0] == x:
          if alimento[x][1] == '100':
            print('Alimento: ' , alimento[x][0] , '\nQuantidade: ' , alimento[x][1] , 'g\nProteínas: ' , alimento[x][2] , 'g\nGordura: ' , alimento[x][3] , 'g\nCarboidrato: ' , alimento[x][4] , 'g')
            print()
            
          elif alimento[x][1] == '1':
            print('Alimento: ' , alimento[x][0] , '\nQuantidade: ' , alimento[x][1] , 'und\nProteínas: ' , alimento[x][2] , 'g\nGordura: ' , alimento[x][3] , 'g\nCarboidrato: ' , alimento[x][4] , 'g')
            print()

  input('Pressione ENTER')


def verCafeManha():
  for cafe in cafeManha: 
    print()
    print(cafe)
    print('\nAlimentos:\n')
    for i in cafeManha[cafe]: 
      print(i)

  input('Pressione ENTER')

def verAlmoco():
  for almoc in almoco: 
    print()
    print(almoc)
    print('\nAlimentos:\n')
    for i in almoco[almoc]: 
      print(i)

  input('Pressione ENTER')

def verLanche():
  for lanch in lanche: 
    print()
    print(lanch)
    print('\nAlimentos:\n')
    for i in lanche[lanch]: 
      print(i)

  input('Pressione ENTER')

def verJanta():
  for jant in janta: 
    print()
    print(jant)
    print('\nAlimentos:\n')
    for i in janta[jant]: 
      print(i)

  input('Pressione ENTER')  

def menuRelatorios():
  os.system('clear')
  print('==============================================')
  print('================= RELATÓRIOS =================')
  print('==============================================')
  print()
  print('\t1 - Relatório Paciente')
  print('\t2 - Relatório Alimento')
  print('\t3 - Relatório Café da Manhã')
  print('\t4 - Relatório Almoço')
  print('\t5 - Relatório Lanche')
  print('\t6 - Relatório Janta')
  print('\t0 - Voltar ao menu principal')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  return esc

def moduloRelatorios():
  esc = menuRelatorios()
  while esc != '0':
    if esc == '1':
      verPaciente()
  
    elif esc == '2':
      verAlimentos()
      
    elif esc == '3':
      verCafeManha()
      
    elif esc == '4':
      verAlmoco()
  
    elif esc == '5':
      verLanche()
  
    elif esc == '6':
      verJanta()
      
    else:
      print('Seleção inválida') 
    print()
    
    esc = menuRelatorios()
  
  print()