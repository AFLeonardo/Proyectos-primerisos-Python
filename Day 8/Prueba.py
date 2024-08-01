import unittest
import Cambia_texto


class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):

        palabra = "buen dia"
        resultado = Cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "Buen dia", "Test fallido, verificar funcionamiento.")


if __name__ == "__main__":
    unittest.main()