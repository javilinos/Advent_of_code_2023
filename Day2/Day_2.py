
def readLines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

if __name__ == '__main__':
    data = {}
    condition = [12, 13, 14]
    lines = readLines("input.txt")
    # part 1
    for line in lines:
        game = line.split(":")
        game_number = int(game[0].split("Game")[1])
        data[game_number] = [0, 0, 0] # rgb
        game_data = game[1].split(";")
        for batch in game_data:
            batch_data = batch.split(",")
            for color_number in batch_data:
                index = color_number.find("red")
                if index != -1:
                   data[game_number][0] = int(color_number[:index]) if data[game_number][0] < int(color_number[:index]) else data[game_number][0]
                index = color_number.find("green")
                if index != -1:
                   data[game_number][1] = int(color_number[:index]) if data[game_number][1] < int(color_number[:index]) else data[game_number][1]
                index = color_number.find("blue")
                if index != -1:
                   data[game_number][2] = int(color_number[:index]) if data[game_number][2] < int(color_number[:index]) else data[game_number][2]
    sum_days = 0
    sum_mul_values = 0
    for day, values in data.items():
        if values[0] <= condition[0] and values[1] <= condition[1] and values[2] <= condition[2]:
            sum_days += day
        sum_mul_values += values[0]*values[1]*values[2]
    print(sum_days)
    print(sum_mul_values)
    
