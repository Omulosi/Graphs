from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from stack import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk

traversal_path = []
starting_path = [world.starting_room]  # stack
visited = set()

opposite_dir = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e',
}

stack = Stack()
stack.push(starting_path)

while len(visited) < 500:
    local_path = stack.pop()
    current_node = local_path[-1]
    try:
        if current_node not in visited:
            visited.add(current_node)

            neighbor_nodes = set()
            stored_direction = []

            for direction in current_node.get_exits():
                room = current_node.get_room_in_direction(direction)
                stored_direction.append({"room": room, "dir": direction})
                neighbor_nodes.add(room)

            unvisited_neighbors = neighbor_nodes - visited
            if len(unvisited_neighbors) == 0:
                raise Exception
            random_neighbor = random.sample(unvisited_neighbors, 1)[-1]
            new_local = local_path.copy()
            new_local.append(random_neighbor)

            direction =  [stored for stored in stored_direction if stored["room"] == random_neighbor]

            room_dir = direction[-1]["dir"]

            traversal_path.append(room_dir)
            stack.push(new_local)
        else: raise Exception
    except:
        current_node = local_path[-1]
        neighbor_nodes = set()
        stored_direction = []

        for direction in current_node.get_exits():
            room = current_node.get_room_in_direction(direction)
            stored_direction.append({"room": room, "dir": direction})
            neighbor_nodes.add(room)

        unvisited_neighbors = neighbor_nodes - visited
        if len(unvisited_neighbors) == 0:
            new_local = local_path[:-1]
            last_node = new_local[-1]
            stored_direction = []

            for direction in last_node.get_exits():
                room = last_node.get_room_in_direction(direction)
                if room == current_node:
                    stored_direction.append({"room": room, "dir": direction})

            direction = stored_direction[-1]['dir']

            back_dir =  opposite_dir[f"{direction}"]

            traversal_path.append(back_dir)
            stack.push(new_local)
        else:
            neighbor_nodes = set()
            stored_direction = []

            for direction in current_node.get_exits():
                room = current_node.get_room_in_direction(direction)
                stored_direction.append({"room": room, "dir": direction})
                neighbor_nodes.add(room)

            unvisited_neighbors = neighbor_nodes - visited
            random_neighbor = random.sample(unvisited_neighbors, 1)[-1]
            new_local = local_path.copy()
            new_local.append(random_neighbor)

            direction =  [stored for stored in stored_direction if stored["room"] == random_neighbor]

            room_dir = direction[-1]["dir"]

            traversal_path.append(room_dir)
            stack.push(new_local)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
