import time
import tracemalloc

with open("server.log", "w") as file:
    file.write("INFO Server started\n")
    file.write("ERROR Database connection failed\n")
    file.write("INFO User logged in\n")
    file.write("ERROR File not found\n")
    file.write("WARNING Low memory\n")
    file.write("ERROR Network timeout\n")

def find_errors_list(filename):
    errors = []
    with open(filename, "r") as file:
        for line in file:
            if "ERROR" in line:
                errors.append(line)
    return errors

def find_errors_generator(filename):
    with open(filename, "r") as file:
        for line in file:
            if "ERROR" in line:
                yield line

tracemalloc.start()
start = time.time()

errors = find_errors_list("server.log")

list_time = time.time() - start
list_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

tracemalloc.start()
start = time.time()

for error in find_errors_generator("server.log"):
    pass

generator_time = time.time() - start
generator_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print("ERROR records:")
for error in errors:
    print(error, end="")

print("\nList Time:", list_time, "seconds")
print("List Memory:", list_memory, "bytes")

print("Generator Time:", generator_time, "seconds")
print("Generator Memory:", generator_memory, "bytes")
