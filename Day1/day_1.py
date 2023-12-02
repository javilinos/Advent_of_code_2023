    
def load_file_lines(file_path):
    with open(file_path, "r") as f:
        return f.readlines()

if __name__ == "__main__":
    numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    file_array = load_file_lines("input2.txt")
    values_array = []
    for line in file_array:
        a = ""
        b = ""
        found_a = False
        found_b = False
        for i, character in enumerate(line):
            if (character.isnumeric()):
                a = character
                break
            else:
                subLine = line[0:i+1]
                for number_str in numbers:
                    if number_str in subLine:
                        a = numbers[number_str]
                        found_a = True
                        break
                if found_a:
                    break
                        
        for i, character in enumerate(reversed(line)):
            if (character.isnumeric()):
                b = character
                break
            else:
                subLine = line[len(line)-i-1:len(line)]
                for number_str in numbers:
                    if number_str in subLine:
                        b = numbers[number_str]
                        found_b = True
                        break 
                if found_b:
                    break                     
        values_array.append(int(a + b))
    result = 0
    for value in values_array:
        result += value
    
    print(values_array)
    print(result)
