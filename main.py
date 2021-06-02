#Import everything your program needs/does
from otherfile import giveMe7


def main():

    option = ''

    while option != 'q' and option != 'Q':
        option = input('Give me something to do: ')
        print(option)


if __name__ == "__main__":
    main()