import os

# Get the current working directory
current_directory = os.getcwd()

# List all files and directories in current directory
contents = os.listdir(current_directory)

print("Contents of the directory:")
for item in contents:
    print(item)
# import os

# # Specify the directory (you can replace it with any path)
# directory_path = os.getcwd()

# print(f"Contents of directory: {directory_path}\n")

# with os.scandir(directory_path) as entries:
#     for entry in entries:
#         if entry.is_file():
#             print(f"File: {entry.name}")
#         elif entry.is_dir():
#             print(f"Directory: {entry.name}")
