import builtins
import json

class Testes:
    
    def carregaArquivo( self ):
        with builtins.open( "C:\\Users\\gustavo.vprado1\\OneDrive - SENAC - SP\\Área de Trabalho\\Lucas Python\\lanchonete\\textos.txt", "r" ) as dados:
            for linha in dados: 
                print( linha.rstrip())
                
    def carregaJson( self ):
        with open( "C:\\Users\\gustavo.vprado1\\OneDrive - SENAC - SP\\Área de Trabalho\\Lucas Python\\usuarios.json", "r" ) as dados:
            
            # recuperando os dados do JSON
            dadosJson = json.load( dados )
            
            print( f" Usuario: {dadosJson[0]['loginArmazenado'] } e a senha { dadosJson[0]['senhaArmazenada'] } " )             
teste = Testes()
teste.carregaJson()           