email_tlmp = """
    ...: Olá, %(nome)s
    ...:
    ...: Tem interesse em comprar %(produto)s?
    ...:
    ...: Este produto é muito bom para resolver
    ...: %(texto)s
    ...:
    ...: Clique agora em %(link)s
    ...:
    ...: Apenas %(quantidade)d disponivel
    ...:
    ...: preco promocional %(preco).2f
    ...:
    ...: """

for cliente in clientes:
    print (
        email_tlmp 
        % {
            "nome": cliente, 
            "produto": "Caneta", 
            "texto": "Serve para escrever",
            "link": "hahaha",
            "quantidade": 1,
             "preco": 50.5,
     }
     ) 