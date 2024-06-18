import builtins

class GravaDados:

    def salvaDados( self ):    
    #open (nomeArquivo, modoAbertura) é uma função do python3 que lê escreve arquivos
    #w - write - escrita
    #r - read - leitura
    #r+ - escrita/leitura
        
        with open( "lanchonete\\Modulos\\dados.txt", "w") as dados:
            print( f"No arquivo temos: \n {dados}" )
            dados.write("Linha 01 \n")
            dados.write("Linha 02 \n")
            dados.close()
            
            dados.write( self.usuariosCadastrados)
            
            dados.close
            
        print("dados Armazenados")    

    def leDados( self ):
        # para ler usamos a classe builtins no Python3
        with builtins.open( "Lanchonete\\Modulos\\dados.txt", "r" ) as dados:
            
            print( f"No arquivo temos: \n" )
            #for é um laço de repetição
            #para cada linha o arquivo de texto
            for linha in dados.readlines() :
                print( linha.strip() )

    def exportaDados( self ):
        print("")

dados = GravaDados()
dados.salvaDados()
dados.leDados