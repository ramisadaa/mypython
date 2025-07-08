# Writing to a file
data = {"name": "John", "age": 30, "city": "New York"}
with open("data.txt", "w") as f:
    f.write(str(data))

# Reading from a file and converting to dictionary
with open("data.txt", "r") as f:
    content = f.read()
    data_read = eval(content)  # Convert string to dictionary

# print(data_read)

# # Writing to a JSON file
# import json
# data = {"name": "John", "age": 30, "city": "New York"}
# with open("data.json", "w") as f:
#     json.dump(data, f)

# # Reading from a JSON file
# with open("data.json", "r") as f:
#     data_read = json.load(f)

# print(data_read)

# # Writing to a CSV file
# import csv
# data = [["name", "age", "city"], ["John", 30, "New York"], ["Jane", 25, "London"]]
# with open("data.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(data)

# # Reading from a CSV file
# with open("data.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)