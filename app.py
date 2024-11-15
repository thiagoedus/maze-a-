from pyamaze import maze, agent
from a_star import a_star

labirinto = maze(10, 9)

end_position = (5, 5)

labirinto.CreateMaze(y=end_position[0], x=end_position[1])

# celulas = labirinto.grid
# print(celulas)

mapa = labirinto.maze_map
#print(mapa)

# caminho = labirinto.path
# print(caminho)

agente = agent(labirinto, filled=True) # Adicionar footprints = True

agente.position = (2, 3)
posicao = agente.position
print(posicao)

# caminho = {(10, 10): (10, 9), (10, 9): (10, 8), (10, 8): (10, 7)}
# labirinto.tracePath({agente: caminho}, delay=700)

a_star(mapa, posicao, end_position)

labirinto.run()