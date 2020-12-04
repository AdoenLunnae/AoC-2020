from toboggan import Field, Toboggan


def silver(file_content):
    field = Field.from_string(file_content)
    toboggan = Toboggan()

    return toboggan.traverse_and_count_trees(field)


def gold(file_content):
    h_steps = [1, 3, 5, 7, 1]
    v_steps = [1, 1, 1, 1, 2]

    field = Field.from_string(file_content)
    num = 1
    for h_step, v_step in zip(h_steps, v_steps):
        toboggan = Toboggan(v_step, h_step)
        num *= toboggan.traverse_and_count_trees(field)
    return num


def main():
    input_file = input('Input file[input.txt]: ') or 'input.txt'

    with open(input_file, 'r') as file:
        content = file.read()

    print(f"Silver star: {silver(content)}")
    print(f"Gold star: {gold(content)}")


if __name__ == "__main__":
    main()
