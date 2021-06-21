# argument parser
import argparse

# position argument
# if we want to write optional argument we write --Number1
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Number1", help="First Number Input")
    parser.add_argument("Number2", help="Second Number Input")
    parser.add_argument("Operation", help="Operation",
                        choices=["Substract", "Add", "Multiply"])
    args = parser.parse_args()

    print(args.Number1)
    print(args.Number2)
    print(args.Operation)

    n1 = int(args.Number1)
    n2 = int(args.Number2)
    result = None
    if args.Operation == "Substract":
        result = n1-n2
    elif args.Operation == "Add":
        result = n1+n2
    elif args.Operation == "Multiply":
        result = n1*n2

    print(result)
