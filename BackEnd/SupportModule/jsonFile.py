import json


def read_json_data(dir):
    f = open(dir, "r")
    data = json.load(f)
    f.close()
    return data


def write_json_data(dir, data):
    f = open(dir, "w")
    data_json = json.dumps(data, indent="\t")
    f.write(data_json)
    f.close()
    return data_json


# data_example = [
#     {"1": 1, "2": 2},
#     {"1": 1, "2": 2},
#     {"1": 1, "2": 2},
# ]
# print(write_json_data("../Data/Item.json", data_example))
# print(read_json_data("../Data/Item.json"))