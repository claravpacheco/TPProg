from atributosUsuarios.cuil import Cuil
from atributosUsuarios.password import Password
from atributosUsuarios.telefono import Telefono



class Ciudadano:
    def __init__(self, telefono, cuil, usersname, password):
        self.telefono = Telefono(telefono)
        self.cuil = Cuil(cuil)
        self.UsersName = usersname
        self.password = Password(password)