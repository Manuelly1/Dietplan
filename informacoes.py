import os

def informacoes():
  os.system('clear')
  print('==============================================')
  print('========== INFORMAÇÕES DO PROJETO ============')
  print('==============================================')
  print()
  print('\t1 - Informações do projeto')
  print('\t2 - Participantes')  
  print('\t0 - Voltar ao menu principal')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  
  return esc
# o módulo vai resgatar o que foi adicionado aqui nas informações e vai retornar em esc
  
def verInfo():
  os.system('clear')
  print()
  print('==============================================')
  print('============== SOBRE O PROJETO ===============')
  print('==============================================')

  print('\nO nosso projeto consiste em apresentar um planejamento de dietas (DietPlan), o qual contém alimentos já cadastrados, possibilita também aos usuários (pacientes) a opção de cadastrá-los e indica 4 opções diferentes para cada refeição, as quais vão sendo fornecidas a partir da finalidade do paciente.')

  print('')
  input('Pressione ENTER')
  
  

def verParticipantes():
  os.system('clear')
  print()
  print('==============================================')
  print('=============== PARTICIPANTES ================')
  print('==============================================')
  
  print('\nAs alunas desenvolvedoras foram Dayanne Xavier Lucena e Manuelly Rodrigues Victor. Alunas do curso de Sistemas de Informação do primeiro período')

  print('')
  input('Pressione ENTER')
  
# O módulo principal dessa parte:
def moduloInformacoes():
  esc = informacoes()
  
  while esc != '0':
    if esc == '1':
      verInfo()
      
    elif esc == '2':
      verParticipantes()
      
    else:
      print('Seleção inválida') 
    print()
    
    esc = informacoes()
