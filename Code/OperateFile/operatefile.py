import re
def getfile(path):
    f = open(path, "r")
    r = f.readlines()
    contents = []
    for i in range(0, len(r)):
        content = r[i].strip('\n')
        # content = int(content)
        contents.append(content)
    f.close()
    return contents

def get_all_file(path):
    f = open(path, "r")
    r = f.readlines()
    num = r[0].strip(" ")
    contents = r[1].split(" ")
    content = []
    for i in range(0, len(contents)):
        content.append(int(contents[i]))
    return num, content

def getfiles(path, name, start, num):
    filename = []
    for i in range(start, num + 1):
        Fname = ""
        Fname = path + name + str(i) + ".IN"
        filename.append(Fname)
    return filename

def writefile(content, path):
    f = open(path, "w+")
    if type(content) == "list":
        for i in content:
            f.write(str(i) + '\n')
    else:
        f.write(str(content) + '\n')
    f.close()