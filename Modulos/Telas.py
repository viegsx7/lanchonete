import time
class Telas:
    
    def entradaSistema( self ):
        print( f"+------------------------------------------------------------------------+" )
        print( f"|                                                                        |" )
        print( f"|                  ** Seja bem vindo ao sistema **                       |" )
        print( f"|                                                                        |" )
        print( f"+------------------------------------------------------------------------+" ) 
        
        self.esperaLimpa()
        
    def esperaLimpa( self, tempo = 3 ):
       # esperar X segundos
       time.sleep( tempo )
       # limpa a tela
       self.limpaConsole()
        
    def saidaSistema( self ):
        print( f"+------------------------------------------------------------------------+" )
        print( f"|                                                                        |" )
        print( f"|                  ** Obrigado por usar o sistema **                     |" )
        print( f"|                                                                        |" )
        print( f"+------------------------------------------------------------------------+" ) 
    
    def mensagemSistema( self, mensagem ):
        print( f"+------------------------------------------------------------------------+" )
        print( f"|                                                                        |" )
        print( f"                  ** {mensagem} **                       " )
        print( f"|                                                                        |" )
        print( f"+------------------------------------------------------------------------+" )     
    
    def limpaConsole( self ):

        #if os.name == "nt": # windows nt - Linux posix - Mac darwin
            #os.system( "cls" )
        
        #elif os.name == "darwin":
            #os.system( "clear" )    
        #else:
            #os.system( "clear" )
            
        tipoSistema = os.name
        switch( tipoSistema ):
            case "nt":
                os.system("cls")
                break:    