from src.file_organiser import FileOrganiser

if __name__ == "__main__":
    folder = input("Enter the directory path to organize: ").strip()
    FileOrganiser(folder).organize_files()
