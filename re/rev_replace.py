import re

def replace_pattern(input_string):
    # Define the regular expression pattern
    pattern = re.compile(r'\\rev{([^}]*)}')

    # Find all matches in the input string
    matches = pattern.findall(input_string)
    
    print(len(matches))

    # Replace each match with its content
    for match in matches:
        input_string = input_string.replace(f"\\rev{{{match}}}", match)

    return input_string

def main():
    # Specify input and output file paths
    input_file_path = 'main.tex'
    output_file_path = 'main_modify.tex'

    try:
        # Read content from the input file
        with open(input_file_path, 'r') as input_file:
            input_content = input_file.read()
            

        # Perform the replacement
        output_content = replace_pattern(input_content)

        # Write the modified content to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(output_content)

        print(f"Replacement completed. Output written to {output_file_path}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()