from atributosUsuarios.password import Password


class Administrador:
    def __init__(self,usuario,contrasena):
        self.usuario = usuario
        self.contrasena = Password(contrasena)