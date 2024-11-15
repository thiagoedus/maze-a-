from pyamaze import maze, agent
from a_star import a_star

# Define as dimensões do labirinto
maze = maze(40, 40)

# Definido a posição final
end_position = (1, 1)

# Passando a posição final; loopPercent = número de caminhos possíveis
maze.CreateMaze(y=end_position[0], x=end_position[1], loopPercent=10)


mapa = maze.maze_map

maze_agent = agent(maze, filled=True, footprints=True) 


position_agent = maze_agent.position


caminho = a_star(mapa, position_agent, end_position)
maze.tracePath({maze_agent: caminho}, delay=10)

maze.run()