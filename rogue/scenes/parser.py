def parser_txt(filename):
    array = []

    repl_to = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    repl_to.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    repl_to.extend(['@', '!', '*'])

    with open(filename, 'r') as f:
        data = f.readlines()

    for line in data:
        new_line = ''.join(['.' if ch in repl_to else ch for ch in line]).rstrip()
        array.append(new_line)
    return array


def main():
    ret = parser_txt('file.txt')
    for n, line in enumerate(ret):
        print("{0}{1}".format(n, line))


if __name__ == '__main__':
    main()
