# Program to write, append, and read a file

# Step 1: Take user input and write to file
text = input("Enter text to write to the file: ")

try:
    with open("output.txt", "w") as file:
        file.write(text + "\n")
    print("Data successfully written to output.txt.")
except Exception as e:
    print("Error writing to file:", e)

# Step 2: Append additional text to the file
additional_text = input("Enter additional text to append: ")

try:
    with open("output.txt", "a") as file:
        file.write(additional_text + "\n")
    print("Data successfully appended.")
except Exception as e:
    print("Error appending to file:", e)

# Step 3: Read and display final content
try:
    print("Final content of output.txt:")
    with open("output.txt", "r") as file:
        print(file.read())
except Exception as e:
    print("Error reading file:", e)
