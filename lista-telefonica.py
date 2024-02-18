'''- O contato pode ter os dados:
- Nome
- Telefone
- Email
- Favorito (está opção é para poder marcar um contato como favorito)'''

agendas={}

def adicionar_contatos(agendas,nome,telefone,email):
  agenda = agendas["nome","telefone","email","favorito"]= nome,telefone,email,True
  agendas = agenda
  print(f"\nNome: {nome}  telefone:{telefone} Email: {email} inserido com secesso!")
  return

def ver_agenda(agendas):
   for indice, agenda in enumerate(agendas.values(),start=1):
      status = "✓" if tarefa["completada"] else " "
      nome_tarefa = tarefa["tarefa"]
    print(f"{indice}- nome: {agenda[0]} telefone: {agenda[1]}email: {agenda[2]}")
  
def adicionar_contatos_atualizado(agendas,indice_agenda,novo_nome,novo_telefone,novo_email):
   indece_agenda_atualizar = int(indice_agenda)-1
   if indece_agenda_atualizar >= 0 and indece_agenda_atualizar < len(agendas):
        
        agendas[indece_agenda_atualizar] ["nome","telefone","email"]= novo_nome,novo_telefone,novo_email,
        print(f"Tarefa {indice_agenda} atualizar para  {novo_nome} {novo_telefone} {novo_email}")
        
   else:
        print("Indice de tarefa invalido.")
   return    
 

def deletar_contato(agendas):
  try:
    for agenda in agendas:
      if agenda["completada"]:
        agendas.remove(agenda)
    print("delerar agenda. ")
    return
  except Exception as erro:
    print(f"Erro: {erro}")






print("lista telefonica ")

while True:
  print("\n seu contatos ")
  print("1, inserir contatos ")
  
  print("3, editar contatos")
 
  print("5, deletar contatos")
  print("6, Sair da agenda ")
  
  escolha = input("Digite sua escolha:  ")
  
  if escolha == "1":
    nome = input("\nDigite seu nome: ")
    telefone = input("\nDigite seu telefone : ")
    email = input("\nDigite seu email: ")
    adicionar_contatos(agendas,nome,telefone,email)
    
  elif escolha == "2":
    ver_agenda(agendas)
    
  elif escolha == "3":
    ver_agenda(agendas)
    indice_agenda = input("Digite o indice da agenda que deseja editar: ")
    novo_nome = input("\nDigite seu nome: ")
    novo_telefone = input("\nDigite seu telefone : ")
    novo_email = input("\nDigite seu email: ")
    adicionar_contatos_atualizado(agendas,indice_agenda,novo_nome, novo_telefone, novo_email) 
    ver_agenda(agendas)   
    
  elif escolha == "5":
    deletar_contato(agendas)
    
  elif escolha == "6":
    break

print("Fim da agenda ")
  