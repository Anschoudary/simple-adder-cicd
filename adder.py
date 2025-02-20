def add(x, y):
    """Adds two numbers."""
    return x + y

def process_data(input_file, output_file):
    """Reads data from input_file, adds the numbers, and writes the result to output_file."""
    try:
        with open(input_file, 'r') as f:
            line = f.readline().strip()
            num1, num2 = map(int, line.split(','))

        result = add(num1, num2)

        with open(output_file, 'w') as f:
            f.write(str(result))

    except FileNotFoundError:
        print(f"Error: File not found.")
    except ValueError:
        print(f"Error: Invalid data format in {input_file}")

if __name__ == "__main__":
    input_file = "data.txt"
    output_file = "results.txt"
    process_data(input_file, output_file)