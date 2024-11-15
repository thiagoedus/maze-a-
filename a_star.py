def a_star(maze_map, initial_position, end_position):
    y = list(maze_map.items())[-1][0][0]
    x = list(maze_map.items())[-1][0][1]

    print(f'x: {x} y: {y}')
    print('Posição agente: ', initial_position)
    print('Posição de chegada: ', end_position)

    open_list = []
    closed_list = []

    # [posicao-inicial, custo-ate-fim, custo-percorrido, pai] - se pai = 0, não tem pai
    open_list.append((initial_position, 0, 0, 0))

    # while True:
    if not open_list:
        print("No path was found")
    else:
        position = open_list[-1]
        




# Recebe um posição atual e um movimento e retorna a nova posição
def new_position(position, move):
    if move == 'E':
        next_position = (position[0], position[1]+1)
        return next_position
    elif move == 'W':
        next_position = (position[0], position[1]-1)
        return next_position
    elif move == 'N':
        next_position = (position[0]-1, position[1])
        return next_position
    elif move == 'S':
        next_position = (position[0]+1, position[1])
        return next_position
    else:
        print("Position not found")

# Calcula o custo da posição inicial até a posição final
def calculate_cost_destiny(position, end_position):
    return abs((position[0] - end_position[0]) + (position[1] - end_position[1]))

# [mapa, posição, posição-final, lista-fechada] - explora o mapa com base na posição;
# explora seus vizinhos calculando o custo de cada um; 
# verifica se existe na lista fechada e retorna ordenando por custo
def explore_neighborhood(maze_map, position, end_position, closed_list):
    neighborhood = [neighbor for neighbor, value in maze_map[position].items() if value == 1]
    neighbors = []
    for neighbor in neighborhood:
        position_finded = new_position(position, neighbor)
        # TODO adicionar verificação e arrumar posição - List Comprehension
        if position_finded not in closed_list:
            neighbors.append([position_finded, 
                              calculate_cost_destiny(position_finded, end_position),
                              position[1] + 1, position[0]])
            
    return neighbors