import sqlite3

import os
conn = sqlite3.connect('maindb.db')


def totais():
    print ("1 - Ver tudo")
    print ("2 - Ver resumo baseado em tempo")
    print ("3 - Ver registros")
    print ("0 - voltar")
    option = input()

#end of totais

def produtos():
    
    sair = 0
    while sair == 0:
        c = conn.cursor()
        os.system('cls')
        print("Menu > Produtos")
        print ("1 - Novo produto")
        print ("2 - Editar produto")
        print ("3 - Excluir produto")
        print ("4 - Relartório")
        print ("0 - voltar")
        option = input()

        try:
            option = int (option)
        except:
            option = 99

        if option == 1:
            os.system('cls')
            print("Menu > Produtos > Novo produto")
            print("Digite o CÓDIGO do produto: ", end=""))
            prodID = input()
            print("Digite o NOME do produto: ", end="")
            prodNome = input()
            print("Digite o CUSTO do produto: ", end=""))
            prodPrice = input()
            print("Observação para estoque: ", end=""))
            obs = input()
            c.execute("INSERT INTO product VALUES (:ID,:nome,:custo)" , {"ID": prodID, "nome": prodNome, "custo":prodPrice})
            c.execute("INSERT INTO stock (obs, quant, product_id) VALUES (:obs, :quant, :product_id)", {"obs":obs, "quant":0, "product_id": prodID})
            print(prodID + " | " + prodNome + " | " + prodPrice + " Adicionado ")
            conn.commit()
            
        
        elif option == 2:
            os.system('cls')
            print("Menu > Produtos > Editar produto")
            print("Digite o CÓDIGO do produto a ser editado: ")
            value = input()
            c.execute("SELECT * FROM product WHERE ID = :id" , {"id": value})
            if not c.fetchone():
                print("Nenhum produto com este código!")
                os.system("pause")
            else:
                print("Digite o novo NOME do produto " + value + ": ", end="")
                nome = input()
                print("Digite o novo PREÇO DE CUSTO do produto " + value + ": ", end="")
                price = input()
                print("Digite a nova OBSERVAÇÃO DE ESTOQUE do produto " + value + ": ", end="")
                obs = input()
                c.execute("UPDATE product SET name = :new_name, cost = :new_cost WHERE id = :id", {"new_name": nome, "new_cost": price, "id": value})
                c.execute("UPDATE stock SET obs WHERE producto_id = :id", {"id": value})
                conn.commit()

        elif option == 3:
            print("Opção desabilitada!")
            os.system("pause")
        elif option == 4:
            os.system('cls')
            c.execute("SELECT * FROM product")
            print(c.fetchone())
            os.system("pause")
        elif option == 0:
            sair = 1

#end of produtos

def caixa():
    print ("1 - Histórico")
    print ("2 - Tezouraria")
    print ("3 - Ralatório")
    print ("0 - voltar")
    option = input()

#end of caixa

def estoque():
    voltar = 0
    while voltar == 0:
        c = conn.cursor()
        os.system('cls')
        print("Menu > Estoque")
        print ("1 - Alterar estoque")
        print ("2 - Relatório")
        print ("0 - voltar")
        option = input()

        try:
            option = int (option)
        except:
            option = 99

        if option == 1:
            os.system('cls')
            print("Menu > Estoque > Alterar estoque")
            c.execute("Select * FROM product")
            c.fetchall()
            print("Digite o CÓDIGO do produto a ser adicionado em estoque: ")
            cod = input()
            print("Digite a quantidade a ser incrementada em estoque no produto " + cod + ": ")
            quantidade = input()
            c.execute("SELECT quant FROM stock WHERE product_id = :cod", {"cod": cod})
            value = c.fetchone()
            qtd = int(value[0])
            quantidade = int(quantidade)
            if value:
                c.execute("UPDATE stock SET quant  = :new_quant WHERE product_id = :cod", {"new_quant": qtd + quantidade, "cod": cod})
                conn.commit()
            else:
                print("Código de produto inexistente")
        if option == 2:
            os.system('cls')
            print("Menu > Estoque > Relatório")
            c.execute("SELECT * FROM stock")
            print(c.fetchall())
            os.system("pause")
        if option == 0:
            voltar = 1
        

#end of estoque

def registros():
    print ("TODO")

#end of registros

c = conn.cursor()

sair = 0
while sair == 0:
    os.system('cls')
    print ("Selecione a opção desejada: ")
    print ("1 - Ver dados totais")
    print ("2 - Gerenciar Produtos")
    print ("3 - Caixa")
    print ("4 - Estoque")
    print ("5 - Registros")
    print ("0 - Sair")

    option = input()
  
    try:
        option = int (option)
    except:
        option = 99

    if option == 1:
        totais()
    elif option == 2:
        produtos()
    elif option == 3:
        caixa()
    elif option == 4:
        estoque()
    elif option == 5:
        registros()
    elif option == 0:
        sair = 1
        conn.close()
    else:
        print("Opção inválida!\n\n\n\n")


        
        
