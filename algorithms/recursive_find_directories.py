import os


def find_directories(directory):
    for filename in os.listdir(directory):
        if is_directory(directory, filename):
            print(os.path.join(directory, filename))

            # Recursively call this function on the subdirectory:
            find_directories(os.path.join(directory, filename))


def is_directory(directory, filename):
    return os.path.isdir(os.path.join(directory, filename)) and filename != "." and filename != ".."