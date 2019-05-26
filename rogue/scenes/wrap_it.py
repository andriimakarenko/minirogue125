from curses import wrapper


def wrap_it(func):
    wrapper(func)
    return wrapper


def say_hello():
    print("Hello!")


def main():
    print("start")
    wrap_it(say_hello())


if __name__ == '__main__':
    main()
