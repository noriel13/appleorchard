#Import everything your program needs/does
from orchard import AppleOrchard
from frontend import menu

def main():
    a_orch = AppleOrchard()

    option = ''

    while option != 'q' and option != 'Q':
        a_orch.display_orchard()

        option = input(menu)
  
        if option == 'A':
            print(f'Number of trees: {a_orch.num_trees()}')


if __name__ == "__main__":
    main()