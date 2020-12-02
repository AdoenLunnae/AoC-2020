from sys import stderr

def read_file(filename):
    with open(filename, 'r') as f:
        raw_text = f.readlines()
    return  [line.strip() for line in raw_text]

def silver(input_data):
    for n1 in input_data:
        for n2 in input_data:
                if n1+n2 == 2020:
                    return(n1*n2)

def gold(input_data):
    for n1 in input_data:
        for n2 in input_data:
            for n3 in input_data:
                if n1+n2+n3 == 2020:
                    return(n1*n2*n3)

def main(filename):
    try:
        numbers = [int(x) for x in read_file(filename)]
    except FileNotFoundError:
        print("Invalid file", file=stderr)
        exit(1)
    print(f"Silver: {silver(numbers)}")
    print(f"Gold: {gold(numbers)}")


if __name__ == '__main__':
    main(input('Data file[input.txt]: ') or 'input.txt')