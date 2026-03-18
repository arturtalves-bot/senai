estoque = {}
print ("bem-vindo ao sistema de gestao de estoque desenvolvimento por: artur freitas ")
while True:
     operação =input("deseja registrar a saida e saida de produtos? (digite 'entrada' ou 'saida') ou 'sair'").lower()

     if operação == "sair":
          break
     if operaçao not in ['entrada', 'saida']:
          print("operação invalida, ")
          continue
  if operação == "sair":
     break
     produto = input("digite o nome do produto: ").strip()
     quantidade = int(input("digite a quantidade: "))
     if operação == "entrada":
          estoque[produtos] = estoque.get(produto, 0) + quantidade
     elif operação == "saida":
          if estoque.get(produto, 0) >= quantidade:
               estoque[produto] -= quantidade
          else:
               print("erro:prouto inexistente ou estoque insuficiente ", produto)

print("\n ---estoque final---: ")
for produto, quantidade in estoque.items():
     print(f"{produto}: {quantidade}")
     opniao = input("o que voce achou do sistema? (digite 'bom' ou 'ruim')").lower()
     if opniao == "bom e muito sistematico":
          print("obrigado pelo feedback positivo! ficamos felizes em saber que gostou do sistema.")  
          if opniao == "ruim e muito confuso":
          print ("agradecemos pelo feedback construtivo! estamos sempre buscando melhorar, e sua opinião é valiosa para nós.")   
          else:
          print("obrigado pelo feedback! estamos sempre buscando melhorar, e sua opinião é valiosa para nós.")







      


