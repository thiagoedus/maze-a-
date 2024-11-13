from pyamaze import maze, agent

labirinto = maze()

labirinto.CreateMaze()

# celulas = labirinto.grid
# print(celulas)

# mapa = labirinto.maze_map
# print(mapa)

# caminho = labirinto.path
# print(caminho)

# agente = agent(labirinto, filled=True, footprints=True)

# posicao = agente.position
# print(posicao)
# agente.position = (10, 9)

# caminho = {(10, 10): (10, 9), (10, 9): (10, 8), (10, 8): (10, 7)}
# labirinto.tracePath({agente: caminho}, delay=700)

labirinto.run()