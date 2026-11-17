class Incidente:
    def __init__(self, id_inc, ip, ataque, estado, riesgo):
        self.id = id_inc
        self.ip = ip
        self.ataque = ataque
        self.estado = estado
        self.riesgo = riesgo

    def __str__(self):
        return f"ID: {self.id} | IP: {self.ip} | Ataque: {self.ataque} | Estado: {self.estado} | Riesgo: {self.riesgo}"


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijoIzquierdo = None
        self.hijoDerecho = None

    def __str__(self):
        return str(self.dato)


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def isEmpty(self):
        return self.raiz is None

    def insertar(self, incidente):
        self.raiz = self._insertar(self.raiz, incidente)

    def _insertar(self, actual, incidente):
        if actual is None:
            return Nodo(incidente)
        
        if incidente.id < actual.dato.id:
            actual.hijoIzquierdo = self._insertar(actual.hijoIzquierdo, incidente)
        elif incidente.id > actual.dato.id:
            actual.hijoDerecho = self._insertar(actual.hijoDerecho, incidente)
        else:
            print(f"Error: El incidente con ID {incidente.id} ya existe en el arbol.")
        return actual

    def imprimirArbol(self):
        self._imprimir(self.raiz, 0)

    def _imprimir(self, actual, nivel):
        if actual is not None:
            self._imprimir(actual.hijoDerecho, nivel + 1)
            print("    " * nivel + str(actual.dato.id))
            self._imprimir(actual.hijoIzquierdo, nivel + 1)

    # RECORRIDOS
    def recorridoInorden(self):
        self._inorden(self.raiz)
        print()

    def _inorden(self, actual):
        if actual is not None:
            self._inorden(actual.hijoIzquierdo)
            print(actual.dato.id, end=" ")
            self._inorden(actual.hijoDerecho)

    def recorridoPreorden(self):
        self._preorden(self.raiz)
        print()

    def _preorden(self, actual):
        if actual is not None:
            print(actual.dato.id, end=" ")
            self._preorden(actual.hijoIzquierdo)
            self._preorden(actual.hijoDerecho)

    def recorridoPostorden(self):
        self._postorden(self.raiz)
        print()

    def _postorden(self, actual):
        if actual is not None:
            self._postorden(actual.hijoIzquierdo)
            self._postorden(actual.hijoDerecho)
            print(actual.dato.id, end=" ")

    # BUSCAR NODO POR ID
    def buscar(self, id_buscado):
        return self._buscar(self.raiz, id_buscado)

    def _buscar(self, actual, id_buscado):
        if actual is None:
            return None
        if actual.dato.id == id_buscado:
            return actual.dato
        if id_buscado < actual.dato.id:
            return self._buscar(actual.hijoIzquierdo, id_buscado)
        else:
            return self._buscar(actual.hijoDerecho, id_buscado)

    # CONTAR NODOS
    def contarNodos(self):
        return self._contar(self.raiz)

    def _contar(self, actual):
        if actual is None:
            return 0
        return 1 + self._contar(actual.hijoIzquierdo) + self._contar(actual.hijoDerecho)

    # OBTENER MENOR
    def obtenerMenor(self):
        if self.isEmpty():
            return None
        actual = self.raiz
        while actual.hijoIzquierdo is not None:
            actual = actual.hijoIzquierdo
        return actual.dato

    # OBTENER MAYOR
    def obtenerMayor(self):
        if self.isEmpty():
            return None
        actual = self.raiz
        while actual.hijoDerecho is not None:
            actual = actual.hijoDerecho
        return actual.dato

    # BUSCAR POR NIVEL DE RIESGO
    def buscarPorNivelRiesgo(self, nivel):
        res = []
        self._buscarNivelRiesgo(self.raiz, nivel, res)
        return res

    def _buscarNivelRiesgo(self, actual, nivel, res):
        if actual is not None:
            self._buscarNivelRiesgo(actual.hijoIzquierdo, nivel, res)
            if actual.dato.riesgo.lower() == nivel.lower():
                res.append(actual.dato)
            self._buscarNivelRiesgo(actual.hijoDerecho, nivel, res)