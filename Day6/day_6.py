def readLines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
    lines = readLines("input.txt")
    times = lines[0].split(":")[1].split()
    distances = lines[1].split(":")[1].split()
    times = [int(time) for time in times]
    distances = [int(distance) for distance in distances]
    
    res = [0] * len(times)

    for i, time in enumerate(times):
        for j in range(1, time):
            possible_distance = j * (time-j)
            if possible_distance > distances[i]:
                res[i] += 1
    output = 1
    for result in res:
        output *= result
    print(f"part1: {output}")
    #part2
    lines = readLines("input.txt")
    times = lines[0].split(":")[1].split()
    distances = lines[1].split(":")[1].split()
    time = ""
    distance = ""
    for t in times:
        time += t
    for d in distances:
        distance += d
    time = int(time)
    distance = int(distance)

    res = 0
    for i in range(1, time):
        possible_distance = i * (time-i)
        if possible_distance > distance:
            res += 1
    print(f"part2: {res}")
