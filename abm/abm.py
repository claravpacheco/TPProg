from excepciones.usuarioexistente import UsuarioExistente


class AMB:
    def crearAdministrador(self,ususario,contrasena):
        if self.buscarAdminstrador(ususario) == ususario:
            raise UsuarioExistente("Este usuario ya esta registrado, elija otro nombre de usuario")
        else:



    def buscarAdminstrador(self):


    def quitarAdministrador(self):
        pass


    def ingresarAdminenArchivo(self):
        archivo = open("Prog2/EvenIt/archivodetexto/administradoresRegistrados.txt")
        
