
def readLines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

def stringToList(string):
    return list(string)

def checkPose(pose: tuple, matrix):
    for i in range(max(0, pose[0] - 1), min(len(matrix), pose[0] + 2)):
        for j in range(max(0, pose[1] - 1), min(len(matrix[0]), pose[1] + 2)):
            if not matrix[i][j].isnumeric() and matrix[i][j] != '.':
                return True
    return False

def checkPoseStar(pose: tuple, matrix):
    for i in range(max(0, pose[0] - 1), min(len(matrix), pose[0] + 2)):
        for j in range(max(0, pose[1] - 1), min(len(matrix[0]), pose[1] + 2)):
            if matrix[i][j] == '*':
                return (i,j), True
    return (-1,-1), False
    
if __name__ == "__main__":
    lines = readLines("input2.txt")
    lines_matrix = [stringToList(line.strip()) for line in lines]
    num_poses = []
    for i, row in enumerate(lines_matrix):
        num = ''
        poses = []
        for j, value in enumerate(lines_matrix[i]):
            if value.isnumeric():
                num += value
                poses.append((i, j))
                if j == len(lines_matrix[i])-1:
                    num_poses.append((num, poses))
                    num = ''
                    poses = []
            else:
                if num != '':
                    num_poses.append((num, poses))
                    num = ''
                    poses = []
    sum = 0
    for num_poses_ in num_poses:
        for pose in num_poses_[1]:
            if checkPose(pose, lines_matrix):
                sum += int(num_poses_[0])
                break
    print(f"part1: {sum}")
    sum = 0
    start_list = {}
    for i, num_poses_ in enumerate(num_poses):
        for pose in num_poses_[1]:
            star_pose, found = checkPoseStar(pose, lines_matrix)
            if found:
                if not star_pose in start_list:
                    start_list[star_pose] = [num_poses_[0]]
                else:
                    start_list[star_pose].append(num_poses_[0])
                    sum += int(start_list[star_pose][0])*int(start_list[star_pose][1])
                break
    print(f"part2: {sum}")
