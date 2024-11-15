import heapq

def a_star(maze_map, initial_position, end_position):
    open_list = []
    closed_list = []

    # [posicao-inicial, custo-ate-fim, custo-percorrido, pai] - se pai = 0, não tem pai
    open_list.append((initial_position, calculate_cost_destiny(initial_position, end_position), 0, 0))

    while True:
        if not open_list:
            print("No path was found")
        else:
            struct_neighborhood = []
            for position in open_list:

                if position[1] == 0:
                    total_path = get_path(position, closed_list)
                    return total_path

                new_neighbors = explore_neighborhood(maze_map, position[0], position[2], end_position, closed_list)
                for neighbor in new_neighbors:
                    cost = neighbor[1] + neighbor[2]
                    heapq.heappush(struct_neighborhood, (cost, neighbor))
            
            closed_list.extend(open_list)
            open_list.clear()

            while struct_neighborhood:
                cost, item = heapq.heappop(struct_neighborhood)
                open_list.append(item)   
       

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
    return abs(position[0] - end_position[0]) + abs(position[1] - end_position[1])

# [mapa, posição, custo_percorrido, posição-final, lista-fechada] - explora o mapa com base na posição;
# explora seus vizinhos calculando o custo de cada um; 
# verifica se existe na lista fechada e retorna ordenando por custo
def explore_neighborhood(maze_map, position, cost_traveled, end_position, closed_list):
    neighborhood = [neighbor for neighbor, value in maze_map[position].items() if value == 1]
    neighbors = []
    for neighbor in neighborhood:
        position_finded = new_position(position, neighbor)
        is_on_the_closed_list = any([position_finded == p[0] for p in closed_list])
        if is_on_the_closed_list == False:
            neighbors.append((position_finded, 
                              calculate_cost_destiny(position_finded, end_position),
                              cost_traveled + 1, 
                              position))
            
    return neighbors

def get_path(position, closed_list):
    path = [position]
    while True:
        if position[3] != 0:
            path.extend([p for p in closed_list if path[-1][3] == p[0]])
            position = path[-1]
        else:
            formated_path = [p[0] for p in path]
            formated_path.reverse()

            dict_formated_path = {}

            for i in range(len(formated_path)-1):
                if i != formated_path[-1]:
                    dict_formated_path[formated_path[i]] = formated_path[i+1]

            return dict_formated_path

    
