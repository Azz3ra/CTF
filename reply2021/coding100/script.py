map = open("map.txt", "r")

phase = 0

start_flag = ''
a = 0
b = 0
c = 0
finish_flag = ''


result = []

# maze.txt to 2-dimensional array
maze_map = []
maze = open("maze.txt", "r")
for content in maze.read().splitlines():
    maze_map.append(list(content))
print(maze_map)

for line in map.read().splitlines():
    # print('phase' + str(phase) + ', reading: ' + line)

    if (phase == 0):
        start_flag = line
    elif (phase == 1):
        a = int(line)
    elif (phase == 2):
        b = int(line)
    elif (phase == 3):
        c = int(line)
    elif (phase == 4):
        finish_flag = line
    elif (phase == 5):

        # Flags diff
        maze = open("maze.txt", "r")
        flag_start_column = 0
        flag_start_line = 0
        flags_lenght = len(start_flag)
        for line, content in enumerate(maze.read().splitlines()):
            if start_flag in content:
                flag_start_line = line
                flag_start_column = content.find(start_flag)

        result.append(maze_map[flag_start_line + a][flag_start_column + b])

    if phase == 5:
        phase = 0
    else:
        phase += 1

print("".join(result))
