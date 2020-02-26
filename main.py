import sqlite3
import os
conn = sqlite3.connect('maindb.db')

def totais():
    os.system("cls")
    print("Menu > Totais - Alerta: nada implementado nessa sessão!")
    print ("1 - Ver tudo")
    print ("2 - Ver resumo baseado em tempo")
    print ("3 - Ver registros")
    print ("0 - voltar")
    print("> ", end="")
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
        print("> ", end="")
        option = input()

        try:
            option = int (option)
        except:
            option = 99

        if option == 1:
            os.system('cls')
            print("Menu > Produtos > Novo produto")
            print("Digite o CÓDIGO do produto: ")
            print("> ", end="")
            prodID = input()
            print("Digite o NOME do produto: ")
            print("> ", end="")
            prodNome = input()
            print("Digite o CUSTO do produto: ")
            print("> ", end="")
            prodPrice = input()
            print("Observação para estoque: ")
            print("> ", end="")
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
                if len(obs) > 1:
                    c.execute("UPDATE stock SET obs = :obs WHERE product_id = :id", {"obs": obs,"id": value})
                conn.commit()

        elif option == 3:
            print("Menu > Produtos > Exluir item \n -> Opção desabilitada! <-")
            os.system("pause")
        elif option == 4:
            os.system('cls')
            c.execute("SELECT * FROM product")
            obj = c.fetchall()
            row_count = len(obj)
            i = 0
            print("COD  +      DESCRIÇÃO      +   CUSTO")
            print("-----------------------------------------")
            while i < row_count:
                if i%2 == 1:
                    print (obj[i][0], ' | ', obj[i][1], " |  R$", obj[i][2])
                else:
                    print (obj[i][0], ' | ', obj[i][1], " |  R$", obj[i][2])
                i = i+ 1

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
    os.system('cls')
    voltar = 0
    while voltar == 0:
        c = conn.cursor()
        os.system('cls')
        print("Menu > Estoque")
        print ("1 - Alterar estoque")
        print ("2 - Relatório")
        print ("0 - voltar")
        print("> ", end="")
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
            print("> ", end="")
            cod = input()
            print("Digite a quantidade a ser incrementada em estoque no produto " + cod + ": ")
            print("> ", end="")
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
    option = input()

#end of registros

def pedidos():
    c = conn.cursor()
    sair = 0
    while sair == 0:
        os.system('cls')
        print ("Menu > Pedidos")
        print("1 - Cadastrar novo pedido")
        print("2 - Pedidos em aberto")
        print("3 - Pedidos finalizados")
        print("4 - Pedido por período")
        print("5 - Todos os pedidos")
        print("6 - Excluir pedido")
        print("0 - Voltar")
        print ("> ", end="")
        option = input()
  
        try:
            option = int (option)
        except:
            option = 99

        if option == 1:
            os.system('cls')
            print ("Menu > Pedidos > Cadastrar novo pedido")
            c.execute("INSERT INTO oc (obs, total, date, finalizado) VALUES (' ', 0, '25/02/2020', true)")
            conn.commit()
            pedID = c.lastrowid
            print(pedID)
            print("Pedido ", pedID, " gerado com sucesso!")
            os.system("pause")
            fechar = 0
            while fechar == 0:
                os.system("cls")
                print ("Menu > Pedidos > Pedido ", pedID)
                c.execute("SELECT * FROM item WHERE oc_id = :ped", {"ped": pedID})
                items = c.fetchall()
                i = 0
                while i < len(items):
                    print(items[i])
                    i = i + 1

                c.execute("SELECT total FROM oc WHERE id = :pedID", {"pedID": pedID})
                total = c.fetchone()
                total = total[0]
                print("Total: R$ ", total)
                
                print("\n1 - Adicionar Item")
                print("2 - Remover Item")
                print("3 - Concluir este pedido")
                print("4 - Cancelar este pedido")
                print ("> ", end="")
                option = input()
  
                try:
                    option = int (option)
                except:
                    option = 99
                
                if option == 1:
                    os.system("cls")
                    print ("Menu > Pedidos > Pedido ", pedID, "> Inserir")
                    c.execute("SELECT * FROM product")
                    ret = c.fetchall()
                    i = 0

                    print("Digite o CÓDIGO do produto")
                    print ("> ", end="")
                    prodID= input()
                    c.execute("SELECT id FROM product WHERE id = :input", {"input": prodID})
                    if c.fetchone():
                        c.execute("SELECT quant FROM stock WHERE product_id = :prodID", {"prodID": prodID})
                        estoque = c.fetchone()
                        estoque = estoque[0]
                        if estoque > 0:
                            print("Insira o preço de venda do do produto ", prodID, ": \n", ">", end="")
                            valor = input()
                            c.execute("INSERT INTO item (price, product_id, oc_id) VALUES (:valor, :option, :pedID)", {"valor": valor, "option": option, "pedID": pedID})
                            conn.commit()
                            c.execute("SELECT total FROM oc WHERE id = :pedID", {"pedID": pedID})
                            total = c.fetchone()
                            total = total[0] + float(valor)
                            c.execute("UPDATE oc SET total = :total WHERE id = :pedID", {"total": total, "pedID": pedID})
                            c.execute("UPDATE stock SET quant = :estoque WHERE product_id = :prodID", {"estoque": estoque - 1, "prodID": prodID})
                            conn.commit()
                            print("Produto ", prodID, " inserido no pedido ", pedID, " com sucesso!")
                            os.system("pause")
                        else:
                            print("Estoque do produto ", prodID, " está zerado! Produto não adicionado ao pedido.")
                            os.system("pause")
                    else:
                        print("Produto não existe!")
                if option == 2:
                    os.system('cls')
                    print ("Menu > Pedidos > Pedido ", pedID, "> Remover")
                    print("Pedido atual:")
                    c.execute("SELECT * FROM item WHERE oc_id = :ped", {"ped": pedID})
                    items = c.fetchall()
                    i = 0
                    while i < len(items):
                        print(items[i])
                        i = i + 1
                    print("Digite o código do produto a ser removido:\n", ">", end="")
                    r_cod = input()
                    c.execute("SELECT id FROM item WHERE oc_id = :ped AND product_id = :r_cod", {"ped": pedID, "r_cod": r_cod})
                    print(pedID, "+ " , r_cod)
                    record = c.fetchone()
                    print("record", record)
                    if n > 0:
                        print("remove")
                    else:
                        print('not remove')
                    os.system('pause')

                if option == 3:
                    os.system('cls')
                    print ("Menu > Pedidos > Pedido ", pedID, " > Concluir")
                    print("Pedido ", pedID, " salvo com sucesso!")
                    conn.commit()
                    os.system("pause")
                    fechar = 1
                if option == 4:
                    os.system('cls')
                    print ("Menu > Pedidos > Pedido ", pedID, " > Cancelar")
                    print("Limpando itens do pedido ", prodID, "...")
                    c.execute("DELETE FROM item WHERE oc_id = :prodID", {"prodID": prodID})
                    print("Pedido ", pedID, " foi cancelado")
                    os.system("cls")
                    fechar = 1
        if option == 5:
            c.execute("SELECT id, total FROM oc")
            obj = c.fetchall()
            row_count = len(obj)
            i = 0
            print("COD   +   TOTAL      ")
            print("---------------------")
            while i < row_count:
                print (obj[i][0],  " |  R$", obj[i][1])
                i = i + 1           
            os.system('pause')
                    
        if option == 3:
            os.system('cls')
            c.execute("SELECT * FROM oc WHERE finalizado = true")
            obj = c.fetchall()
            i = 0
            while i < len(obj):
                print(obj[i])
                i = i + 1
            os.system("pause")
        if option == 4:
            os.system('cls')
            c.execute("SELECT * FROM oc")
            obj = c.fetchall()
            i = 0
            while i < len(obj):
                print(obj[i])
                i = i + 1
            os.system("pause")
        if option == 0:
            sair = 1

c = conn.cursor()

sair = 0
while sair == 0:
    os.system('cls')
    print ("Menu")
    print ("1 - Ver dados totais")
    print ("2 - Gerenciar Produtos")
    print ("3 - Caixa")
    print ("4 - Estoque")
    print ("5 - Pedidos")
    print ("6 - Registros")
    print ("0 - Sair")
    print ("> ", end="")

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
        pedidos()
    elif option == 6:
        registros()
    elif option == 0:
        sair = 1
        conn.close()
    else:
        print("Opção inválida!\n\n\n\n")


        
        
