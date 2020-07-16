from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

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
### END WORLD GEN ###



### START PLAYER FUNCTIONALITY ###
total_rooms = len(room_graph)
# print("Total Rooms: ", total_rooms)
player = Player(world.starting_room)
room_info = player.current_room
explored_rooms = 1
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited = set()

path = Stack()
path.push(0)


while explored_rooms < total_rooms:
    next_move = Stack()
    current_room = path.stack[-1]

    visited.add(current_room)

    available_dirs = room_graph[current_room][1]

    for move, next_room in available_dirs.items():
        if next_room not in visited:
            next_move.push(next_room)

    if next_move.size() > 0:
        room = next_move.stack[0]
        path.push(room)
        explored_rooms += 1
    else:
        room = path.stack[-2]
        path.pop()

    for move, next_room in available_dirs.items():
        if next_room == room:
            traversal_path.append(move)
            
print("Total Rooms: ", total_rooms)
print("Total Explored Rooms: ", explored_rooms)




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    print("Move: ", move)
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
