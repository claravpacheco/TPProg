import unittest


class GestiondeUsuario:
    def findbyphone(self,phone):

    def findbycuil(self,cuil):

class Ciudadano:
    def __init__(self,CUIL,celular):
        self.CUIL=CUIL
        self.celular = celular
        self.contactos = Contactos()
    def envio_solicitud(self,):




class Contactos:
    def __init__(self):
        self.solicitudes=[]
        self.contactos=[]



class MyTestCase(unittest.TestCase):
    def test_enviarsolicitud(self):

        self.assertEqual(len(Fran.lista_de_solicitudes), 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
