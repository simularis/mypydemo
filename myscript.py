from argparse import ArgumentParser
from tqdm import tqdm
from time import sleep

def say_hello(name: str):
    print("Hello, world.")
    print(f"Hello, {name}.")

def add_two_numbers(number1, number2):
    sum = number1 + number2
    print(f"{number1} + {number2} = {sum}")

def bake_a_cake(duration: float, use_tqdm=True, **kwargs):
    print(f"Starting the kitchen timer for {duration} s")
    if use_tqdm:
        # Command line mode
        with tqdm(total=100) as pbar:
            for i in range(100):
                sleep(duration / 100.)
                pbar.update(1)
    else:
        # Text only output mode for Gooey
        for i in range(100):
            sleep(duration / 100.)
            print(f"Overall progress: {i}/100")

    print("Done baking.")

def main(inargs: list = None, use_tqdm=True):
    parser = ArgumentParser(
        description="Multipurpose tool says hello, adds numbers, bakes cake.",
        epilog=None
    )

    subparsers = parser.add_subparsers(
        title='subcommands',
        description='valid subcommands',
        dest='subparser_name')

    # Create the parser for hello world.
    parser_a = subparsers.add_parser(
        name='say_hello',
        help='Says hello to you.'
    )
    parser_a.add_argument('name', type=str, help='Enter your name')
    parser_a.set_defaults(func=say_hello)

    # Create the parser for adding numbers.
    parser_b = subparsers.add_parser(
        name='add_numbers',
        help='Add two numbers.'
    )
    parser_b.add_argument('numbers', type=float, nargs=2,
                          help='The numbers you want to add, separated by a space. E.g. 1 2.')
    parser_b.set_defaults(func=add_two_numbers)
    
    # Create the parser for progress bar.
    parser_c = subparsers.add_parser(
        name='bake',
        help='Does something slowly with progress updates.'
    )
    parser_c.add_argument('duration', type=float, default=10, help='How many seconds')
    parser_c.set_defaults(func=bake_a_cake)

    args = parser.parse_args(inargs)
    #if args.subparser_name:
    #    args.func(args)
    if args.subparser_name == "say_hello":
        say_hello(args.name)
    elif args.subparser_name == "add_numbers":
        add_two_numbers(*args.numbers)
    elif args.subparser_name == "bake":
        bake_a_cake(use_tqdm=use_tqdm, **args.__dict__)
    else:
        parser.print_usage()

if "__main__" == __name__:
    main()
