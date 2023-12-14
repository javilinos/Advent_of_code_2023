from dataclasses import dataclass

DICT_ = {'-': ['\u2500', '\u2501'] , '|': ['\u2502', '\u2503'] , 'F': ['\u250C', '\u250F'], '7': ['\u2510', '\u2513'],
          'L': ['\u2514', '\u2517'], 'J': ['\u2518', '\u251B'], 'S': ['\u2502', '\u2503']}

def readLines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def shoelaceMethod(vertices: list[tuple]): # didn't work xD
    if vertices[0] != vertices[-1]:
        vertices.append(vertices[0])
    first_knot = 0
    second_knot = 0
    for i, vertice in enumerate(vertices[:-1]):
        first_knot += vertice[0] * vertices[i+1][1]
        second_knot += vertice[1] * vertices[i+1][0]

    res = abs(first_knot - second_knot) / 2
    return res

def IsPointInsidePolygon(x, y, poly): # checks how many loop lines surrounds the point
    n = len(poly)
    winding_number = 0

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        if y1 <= y:
            if y2 > y:
                if (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1) > 0:
                    winding_number += 1
        else:
            if y2 <= y:
                if (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1) < 0:
                    winding_number -= 1

    return winding_number != 0


@dataclass
class pipe:
    def __init__(self, from_: str | None, to_: str | None, position: (int, int), symbol: str):
        self.directions = [from_, to_]
        self.position = position
        self.value = 0
        self.loop_part = False
        self.symbol = symbol

    def __str__(self) -> str:
        return f"pipe({self.directions[0]}, {self.directions[1]}, {self.position})"

    def isConnectedTo(self, pipe_: "pipe"):
        if "north" in self.directions and "south" in pipe_.directions:
            if self.position[0] > pipe_.position[0]:
                return True
        if "north" in pipe_.directions and "south" in self.directions:
            if self.position[0] < pipe_.position[0]:
                return True
        if "east" in self.directions and "west" in pipe_.directions:
            if self.position[1] < pipe_.position[1]:
                return True
        if "east" in pipe_.directions and "west" in self.directions:
            if self.position[1] > pipe_.position[1]:
                return True
        return False


@dataclass
class grid:
    def __init__(self, grid_list: [[pipe]], position: (int, int)):
        self.grid_list = grid_list
        self.path_position = position
        self.max_value = 0
        self.vertices_list = []
        # self.path_2_position = position
        self.path_old_position: (int, int) = None
        # self.path_2_old_position: (int, int)

    def move(self):
        for i in range(
            max(0, self.path_position[0] - 1),
            min(len(self.grid_list), self.path_position[0] + 2),
        ):
            if i != self.path_position[0]:
                if (
                    self.grid_list[i][self.path_position[1]] is not None
                    and self.grid_list[i][self.path_position[1]].isConnectedTo(
                        self.grid_list[self.path_position[0]][self.path_position[1]]
                    )
                    and (i, self.path_position[1]) != self.path_old_position
                ):
                    self.grid_list[i][self.path_position[1]].value = (
                        self.grid_list[self.path_position[0]][
                            self.path_position[1]
                        ].value
                        + 1
                    )
                    self.grid_list[self.path_position[0]][
                        self.path_position[1]
                    ].loop_part = True
                    if self.grid_list[self.path_position[0]][self.path_position[1]].symbol in ('7', 'L', 'F', 'J'):
                        self.vertices_list.append(self.path_position)
                    self.path_old_position = self.path_position
                    self.path_position = (i, self.path_position[1])
                    self.max_value += 1
                    return
        for i in range(
            max(0, self.path_position[1] - 1),
            min(len(self.grid_list[0]), self.path_position[1] + 2),
        ):
            if i != self.path_position[1]:
                if (
                    self.grid_list[self.path_position[0]][i] is not None
                    and self.grid_list[self.path_position[0]][i].isConnectedTo(
                        self.grid_list[self.path_position[0]][self.path_position[1]]
                    )
                    and (self.path_position[0], i) != self.path_old_position
                ):
                    self.grid_list[self.path_position[0]][i].value = (
                        self.grid_list[self.path_position[0]][
                            self.path_position[1]
                        ].value
                        + 1
                    )
                    self.grid_list[self.path_position[0]][
                        self.path_position[1]
                    ].loop_part = True
                    if self.grid_list[self.path_position[0]][self.path_position[1]].symbol in ('7', 'L', 'F', 'J'):
                        self.vertices_list.append(self.path_position)
                    self.path_old_position = self.path_position
                    self.path_position = (self.path_position[0], i)
                    self.max_value += 1
                    return

    def __str__(self) -> str:
        ret = ""
        for pipe_list in self.grid_list:
            for pipe in pipe_list:
                if pipe is not None:
                    if pipe.loop_part:
                        ret += DICT_[pipe.symbol][1]
                    else:
                        ret += "0"
                else:
                    ret += "0"
            ret += "\n"
        return ret


def checkPipeType(obj: str):
    if obj == "." or obj == "S":
        return None, None
    if obj == "|":
        return "north", "south"
    if obj == "-":
        return "east", "west"
    if obj == "F":
        return "south", "east"
    if obj == "7":
        return "south", "west"
    if obj == "J":
        return "north", "west"
    if obj == "L":
        return "north", "east"


if __name__ == "__main__":
    lines = readLines("input.txt")
    grid_ = grid([], (0, 0))
    starting_position = (0, 0)
    for i, line in enumerate(lines):
        row_list = []
        line = line.replace("\n", "")
        for j, obj in enumerate(line):
            if obj == "S":
                hidden_pipe_from = ""
                hidden_pipe_to = ""
                for k in range(max(0, i - 1), min(len(lines), i + 2)):
                    from_, to_ = checkPipeType(lines[k][j])
                    if k == i - 1:
                        if from_ == "south" or to_ == "south":
                            if hidden_pipe_from == "":
                                hidden_pipe_from = "north"
                            else:
                                hidden_pipe_to = "north"
                    if k == i + 1:
                        if from_ == "north" or to_ == "north":
                            if hidden_pipe_from == "":
                                hidden_pipe_from = "south"
                            else:
                                hidden_pipe_to = "south"
                for p in range(max(0, j - 1), min(len(line), j + 2)):
                    from_, to_ = checkPipeType(lines[i][p])
                    if p == j - 1:
                        if from_ == "east" or to_ == "east":
                            if hidden_pipe_from == "":
                                hidden_pipe_from = "west"
                            else:
                                hidden_pipe_to = "west"
                    if p == j + 1:
                        if from_ == "west" or to_ == "west":
                            if hidden_pipe_from == "":
                                hidden_pipe_from = "east"
                            else:
                                hidden_pipe_to = "east"

                row_list.append(pipe(hidden_pipe_from, hidden_pipe_to, (i, j), 'S'))
                grid_.path_position = (i, j)
            else:
                from_, to_ = checkPipeType(obj)
                if from_ is not None:
                    row_list.append(pipe(from_, to_, (i, j), obj))
                else:
                    row_list.append(None)

        grid_.grid_list.append(row_list)
    initial_position = grid_.path_position
    grid_.move()
    while grid_.path_position != initial_position:
        grid_.move()
    print(f"part1: {grid_.max_value/2}")
    res = 0
    for i, point_list in enumerate(grid_.grid_list):
        for j, point in enumerate(point_list):
            if point == None:
                if IsPointInsidePolygon(i, j, grid_.vertices_list):
                    res += 1
            elif not point.loop_part:
                if IsPointInsidePolygon(i, j, grid_.vertices_list):
                    res += 1
    print(res)             