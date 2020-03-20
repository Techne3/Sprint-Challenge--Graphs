from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Graph as a dictionary
mapDictionary = {}

rev_dir = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
# USING BFS to search for shortest path


# #### TODO:  ######


def bfs(starting_room_id):
    # Create an empty queue
    q = Queue()
# Add a path to the starting room to the queue
    q.enqueue([starting_room_id])
# Create an empty set to store visited rooms
    visited = set()
# WHile the queue is not empty...
    while q.size() > 0:
        # Dequeue the first path
        path = q.dequeue()
# Grab the last room from the path
        current_room = path[-1]
# add Current_room to visited
        visited.add(current_room)
        # for each direction in the maps graphs current room..
        for direction in mapDictionary[current_room]:
            # Check if the current room's direction is a '?'
            if mapDictionary[current_room][direction] is '?':
                # if it is, return the path
                return path
                # check else if the current rooms direction is not visited..
            if mapDictionary[current_room][direction] not in visited:

                # If not, create a new path, add the direction.
                new_path = list(path)
                new_path.append(mapDictionary[current_room][direction])
                q.enqueue(new_path)

                # print(current_room, 'current')
                # print(new_path, 'this is new path')
                # print(direction, 'dir')


while len(mapDictionary) != len(room_graph):
    # the room the player is in

    ###### TODO:  ######
    # use the player.current.room to get the room id's
    # store thouse id's into a dictionary
    # get_exits()   => Returns an array of valid directions

    current_room = player.current_room
    # the rooms id
    room_id = current_room.id
    current_room_dic = {}  # current_room_dictionary

    # Check to see if player has explored the room already
    if room_id not in mapDictionary:
        # Record exits and add key as '?'
        for i in current_room.get_exits():
            current_room_dic[i] = '?'
        # Update with previous room id
        if traversal_path:
            # prev room is the oppsite of the last travel path
            prev_dir = rev_dir[traversal_path[-1]]
            current_room_dic[prev_dir] = visited_room_id
        # Update room dictionary with the unexplored exit
        mapDictionary[room_id] = current_room_dic
    # If it already visited, grab data from outer dictionary using room_id
    else:
        current_room_dic = mapDictionary[room_id]

    # Check to see if there are still unvisited rooms connected
    # storing the exits ('?')
    unexplored_exits = list()
    # loop through the room dictionary
    for direction in current_room_dic:
        if current_room_dic[direction] == '?':
            unexplored_exits.append(direction)  # storing exists based on the ?

    # If unexplored exist, go in that the directions
    if len(unexplored_exits) != 0:
        direction = unexplored_exits[0]
        traversal_path.append(direction)
        player.travel(direction)
        # Update the exists
        room_move = player.current_room
        mapDictionary[current_room.id][direction] = room_move.id
        visited_room_id = current_room.id
    # Otherwise, find a way back to closest room with an unknown exit
    else:
        # Find closest room using the bfs
        path_to_next = bfs(room_id)

        # check that data is returned from bfs
        if path_to_next is not None and len(path_to_next) > 0:
            # Have the player travel back to room with unknown exits
            # iterate the length of the dictionary
            for i in range(len(path_to_next) - 1):
                # loop the through the mapDictionary to find the direction
                for direction in mapDictionary[path_to_next[i]]:
                    # if mapDictionary path to next room  and direction matches the room index found in the bfs
                    if mapDictionary[path_to_next[i]][direction] == path_to_next[i + 1]:
                        traversal_path.append(direction)
                        # player will move in that direction if available
                        player.travel(direction)

            # otherwise break that sh#t
        else:
            break

            # TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)


# if len(visited_rooms) == len(room_graph):
#     print(
#         f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


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
