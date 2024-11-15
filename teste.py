import heapq
import random

# Dados fornecidos
dados = [
    ((random.randint(1, 10), random.randint(1, 10)), random.randint(1, 10), random.randint(1, 10), (random.randint(1, 10), random.randint(1, 10)))
    for _ in range(20)
]

# Usando o heapq para organizar os dados
# Vamos transformar cada item da lista em uma tupla (chave para ordenação, item original)
heap = []

# Inserindo os itens no heap com a chave de ordenação (x[1], x[2])
for item in dados:
    custo = item[1] + item[2]
    heapq.heappush(heap, (custo, item))

# O heap agora está ordenado de acordo com as posições 1 e 2
# Agora, podemos desempilhar os elementos do heap
while heap:
    # Retirar o menor elemento (o primeiro elemento da tupla é a chave de ordenação)
    custo, item = heapq.heappop(heap)
    print(item, "- Custo: ", custo)
