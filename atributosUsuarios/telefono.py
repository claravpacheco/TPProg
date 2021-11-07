class Telefono:
    def __init__(self,telefono):
        if len(telefono) != 11:
            raise ValueError("EL numero telefonico debe tener 11 digitos")
        else:
            self.telefono = telefono

    def __str__(self):
        return self.telefono
