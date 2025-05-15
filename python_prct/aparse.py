import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help = "Echo the string you use here")
# The options will be treated as strings

# parser.add_argument("square", help = "Display the square of a given number")
# Positional arguments are not optional
# The default value taken is as string

parser.add_argument("square", type=int, help="To display the square of a number")

parser.add_argument("-v", "--verbosity", help="Increase output verbosity")
# in the above line, the argument for --verbosity is compulsory

# To store it as a flag, use
parser.add_argument("--verbose", action="store_true", help="Add verbosity")

# To limit the choices to an argument. 
parser.add_argument("--power", type=int, choices=[0, 1, 2], help="The power")



# When an optional argument isn't used, the default value given to it will be None
args = parser.parse_args()
print(args.echo)
print(args.square**2)