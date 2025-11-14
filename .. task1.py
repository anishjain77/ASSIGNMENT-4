# Python program to read a file line by line with error handling

def read_file():
    try:
        # Open the file in read mode
        with open("sample.txt", "r") as file:
            # Read and print each line
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file 'sample.txt' does not exist.")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Call the function
read_file()
