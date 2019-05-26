def parser_txt(filename):
    array = []

    repl_to = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    repl_to.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    repl_to.extend(['@', '!', '*'])

    with open(filename, 'r') as f:
        data = f.readlines()

    for line in data:
        new_line = ''

        # yes, it works through the ass, but .replace not work here for some reason
        for ch in line:
            if ch in repl_to:
                new_line += '.'
            else:
                new_line += ch
        array.append(new_line)
    return array


def main():
    ret = parser_txt('file.txt')
    for line in ret:
        print(line)


if __name__ == '__main__':
    main()
