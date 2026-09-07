#### instructions
# delete all contents of public
# copy all files, subdirectories, nested files etc
# log each copy

def copy_static_to_public(static, public):
    print_contents_of_directory(static)
    print_contents_of_directory(public)

def print_contents_of_directory(directory):
    print(f"checking directory {directory}")
