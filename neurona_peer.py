import random
import math

class NeuronaPeer:
    def __init__(self, id):
        self.id = id
        self.vecinos = []
        self.peso = random.uniform(-1, 1)
        self.bias = random.uniform(-0.5, 0.5)
        self.estado = 0.0
        self.buffer = 0.0  # acumula entradas antes de activarse

    def conectar(self, otra):
        if otra not in self.vecinos and otra != self:
            self.vecinos.append(otra)
            otra.vecinos.append(self)  # conexión bidireccional

    def recibir(self, valor):
        self.buffer += valor * self.peso

    def activar(self):
        # Función de activación (sigmoide)
        self.estado = 1 / (1 + math.exp(-(self.buffer + self.bias)))
        self.buffer = 0.0  # limpiar para la siguiente ronda

    def propagar(self):
        for v in self.vecinos:
            v.recibir(self.estado)


# Crear red aleatoria de N neuronas
N = 10
neuronas = [NeuronaPeer(i) for i in range(N)]

# Conectar aleatoriamente (estilo P2P)
for _ in range(N * 2):  # más conexiones = más enlaces en el grafo
    a, b = random.sample(neuronas, 2)
    a.conectar(b)

# Inyectar señal en neurona aleatoria
entrada_inicial = random.choice(neuronas)
entrada_inicial.recibir(1.0)
print(f"Señal inicial en neurona {entrada_inicial.id}")

# Simular propagación
PASOS = 8
for paso in range(PASOS):
    print(f"\n--- Paso {paso+1} ---")
    # Activar todas las neuronas
    for n in neuronas:
        n.activar()
    # Mostrar estado
    for n in neuronas:
        print(f"Neurona {n.id}: {n.estado:.3f}")
    # Propagar
    for n in neuronas:
        n.propagar()
