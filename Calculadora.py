class Calculadora:
    def sumar(self, a, b):
        """
        Devuelve la suma de a y b.

        >>> c = Calculadora()
        >>> c.sumar(3, 3)
        6
        >>> c.sumar(-1, 1)
        0
        """
        return a + b

    def restar(self, a, b):
        """
        Devuelve la resta de a y b.

        >>> c = Calculadora()
        >>> c.restar(5, 3)
        2
        >>> c.restar(3, 5)
        -2
        """
        return a - b

    def multiplicar(self, a, b):
        """
        Devuelve la multiplicación de a y b.

        >>> c = Calculadora()
        >>> c.multiplicar(4, 3)
        12
        >>> c.multiplicar(-2, 3)
        -6
        """
        return a * b

    def dividir(self, a, b):
        """
        Devuelve la división de a entre b.

        >>> c = Calculadora()
        >>> c.dividir(10, 2)
        5.0
        >>> c.dividir(3, 2)
        1.5
        >>> c.dividir(5, 0)
        ZeroDivisionError: No se puede dividir por cero
        """
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b


if __name__ == "__main__":
    import doctest
    doctest.testmod()

