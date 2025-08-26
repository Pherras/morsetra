import os



def read_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return ""
    with open(filename, 'r', encoding='utf8') as file:
        return file.read()

def write_file( content, filename):
    # if not os.path.exists(filename):
    #     os.makedirs("out")
    if content:
        with open(filename, 'w', encoding='utf8') as file:
            file.write(content)

