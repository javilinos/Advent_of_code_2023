from tqdm import tqdm
import multiprocessing

def readLines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def checkRange(dest_source_range: tuple, source_input):

    if (dest_source_range[1] + dest_source_range[2]-1) >= source_input and source_input >= dest_source_range[1]:
        result = dest_source_range[0] - dest_source_range[1] + source_input
        return result
    return source_input
    

def getLowestValue(input_list: list):
    lowest = input_list[0]
    for i in input_list:
        if i < lowest:
            lowest = i
    return lowest

def generateValidData(from_list, to_list):
    for i, data in enumerate(from_list):
        result = 0
        for to_data in to_list:
            result = checkRange(to_data, data)
            if result != data:
                from_list[i] = result
                break
        if result == data:
            from_list[i] = result
    return from_list

def getLocationValue(from_list, to_list):
    # print(from_list)
    data_list = []
    for data_type in to_list:
        data_list = generateValidData(from_list, data_type)
    return data_list


def process_seed(seed_range, map_list, last_seed, lowest_value):
    for j in tqdm(seed_range, "seed progress"):
        location_list = getLocationValue([last_seed + j], map_list)
        if lowest_value == 0 or lowest_value > location_list[0]:
            lowest_value = location_list[0]
    return lowest_value

if __name__ == "__main__":
    part = 2
    lines = readLines("test.txt")
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    data_type = 0
    for line in lines:
        if "seeds:" in line:
            pass
        elif "seed-to-soil map:" in line:
            pass
        elif "soil-to-fertilizer map:" in line:
            data_type+=1
        elif "fertilizer-to-water map:" in line:
            data_type+=1
        elif "water-to-light map:" in line:
            data_type+=1
        elif "light-to-temperature map:" in line:
            data_type+=1
        elif "temperature-to-humidity map:" in line:
            data_type+=1
        elif "humidity-to-location map:" in line:
            data_type+=1
        elif line == ['\n']:
            pass
        else:
            if data_type == 0:
                data = line.replace("\n", '').split(" ")
                if data[0] != '':
                    data = [int(x) for x in data]
                    seed_to_soil.append(tuple(data))
            elif data_type == 1:
                data = line.replace("\n", '').split(" ")
                if data[0] != '':
                    data = [int(x) for x in data]
                    soil_to_fertilizer.append(tuple(data))
            elif data_type == 2:
                data = line.replace("\n", '').split(" ")
                if data[0] != '':
                    data = [int(x) for x in data]
                    fertilizer_to_water.append(tuple(data))
            elif data_type == 3:
                data = line.replace("\n", '').split(" ")
                if data[0] != '':
                    data = [int(x) for x in data]
                    water_to_light.append(tuple(data))
            elif data_type == 4:
                data = line.replace("\n", '').split(" ")
                if data[0] != '':
                    data = [int(x) for x in data]
                    light_to_temperature.append(tuple(data))
            elif data_type == 5:
                data = line.replace("\n", '').split(" ")
                if data[0] != '':
                    data = [int(x) for x in data]
                    temperature_to_humidity.append(tuple(data))
            elif data_type == 6:
                data = line.replace("\n", '').split(" ")
                if data[0] != '':
                    data = [int(x) for x in data]
                    humidity_to_location.append(tuple(data))
    map_list = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
    if part == 1:
        seeds = lines[0].split("seeds:")[1].split(" ")
        seeds = [int(seed.replace('\n', '')) for seed in seeds if seed != '']
    elif part == 2:
        seeds_to_build = lines[0].split("seeds:")[1].split(" ")
        seeds_to_build = [int(seed.replace('\n', '')) for seed in seeds_to_build if seed != '']
        last_seed = 0
        lowest_value = 0
        for i, seed in tqdm(enumerate(seeds_to_build), "overall progress bar"):
            if i % 2 == 0:
                last_seed = seed
                location_list = getLocationValue([seed], map_list)
                if lowest_value == 0 or lowest_value > location_list[0]:
                    lowest_value = location_list[0]
            else:
                seed_range = range(1, seed)
                num_processes = multiprocessing.cpu_count()
                chunk_size = len(seed_range) // num_processes
                chunks = [seed_range[i:i + chunk_size] for i in range(0, len(seed_range), chunk_size)]

                pool = multiprocessing.Pool(processes=num_processes)
                results = [pool.apply_async(process_seed, args=(chunk, map_list, last_seed, lowest_value)) for chunk in chunks]
                pool.close()
                pool.join()

                for res in results:
                    result = res.get()
                    if lowest_value == 0 or lowest_value > result:
                        lowest_value = result

        print(f"part1-part2: {lowest_value}")

