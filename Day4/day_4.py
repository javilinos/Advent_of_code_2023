def readLines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

def stringToList(string):
    return list(string)

if __name__ == "__main__":
    lines = readLines("input2.txt")
    winning_list = []
    hand_list = []
    for line in lines:
        winning = line.split('|')[0].split(':')[1].split(" ")
        winning = [win for win in winning if win != '']
        hand = line.split('|')[1].split(" ")
        hand = [h.replace('\n', '') for h in hand if h != '']
        winning_list.append(winning)
        hand_list.append(hand)
    local_sum = 0
    part1_sum = 0
    n_copies_list = [1] * (len(winning_list))
    n_winning_list = [0] * (len(winning_list))
    for i, win_list in enumerate(winning_list):
        copies = i
        for win in win_list:
            if win in hand_list[i]:
                local_sum = local_sum * 2 if local_sum != 0 else 1
                if len(winning_list) > copies + 1:
                    n_copies_list[copies+1] += n_copies_list[i]
                    n_winning_list[i] += 1
                    copies += 1
        part1_sum += local_sum
        local_sum = 0
        
    print(f"part1 result: {part1_sum}")
    sum = 0
    for copy in n_copies_list:
        sum+=copy
    print(f"part2 result: {sum}")