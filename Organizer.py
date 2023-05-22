from pathlib import Path

def main():
    move_by_ext()

def list_extensions_in_CWD():
    print(f"Extensions in {Path.cwd().name}:")
    extension_set = set()
    
    for file_path in Path.cwd().glob("*.*"):
        extension_set.add((file_path.name.split("."))[-1])  # Quite difficult to read but basically holds the extension

    for extension in extension_set:
        print(f"[+] {extension}")
    
    print()

def make_Directory(directory):
    print(f"\nDestination Folder Set to: {directory}")

    print("Creating Folder...",end=" ")
    new_directory = Path(Path.cwd()/directory)
    new_directory.mkdir(exist_ok=True)  # Creates the destination folder for matching entries
    print("SUCCESS!!!\n")

    return new_directory    

def move_by_ext():
    extension = input("What extension will we be organizing: ")
    print() # New Line
    
    # Ask the user for the name of the folder to place the files in

    destination = input("Enter Destination Folder (of all matching files): ")
    destination_directory = make_Directory(destination)

    # The above 2 lines create a folder to store the matching files

    for matched_files_filePath in Path.cwd().glob("*."+extension):
        new_path_for_matchedFile = destination_directory/matched_files_filePath.name
        print(f"Moving {matched_files_filePath.name}\nTo:{new_path_for_matchedFile.parent.name}... ",end="\t\t")
        matched_files_filePath.replace(new_path_for_matchedFile)
        print("SUCCESS!!!\n")

if __name__ == "__main__":
    print(f"Running script in: {Path(__file__)}\t\tParent Folder is: {Path(__file__).parent}\n")
    list_extensions_in_CWD()
    main()