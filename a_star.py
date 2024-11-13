def a_star(maze_map, initial_position, end_position):
    y = list(maze_map.items())[-1][0][0]
    x = list(maze_map.items())[-1][0][1]

    print(f'x: {x} y: {y}')
    print('Posição agente: ', initial_position)
    print('Posição de chegada: ', end_position)

    open_list = []
    closed_list = []

    open_list.append((initial_position, 0))

    # while True:
    if not open_list:
        print("No path was found")
    else:
        position = open_list[-1][0]
        neighborhood = [neighbor for neighbor, value in maze_map[position].items() if value == 1]
        print(neighborhood)


def new_position(position, move):
    if move == 'E':
        position[1] += 1
        return position
    elif move == 'W':
        position[1] -= 1
        return position
    elif move == 'N':
        position[0] -= 1
        return position
    elif move == 'S':
        position[0] += 1
        return position
    else:
        print("Position not found")

def calculate_cost_destiny(position, end_position):
    return abs((position[0] - end_position[0]) + (position[1] - end_position[1]))