import os
import re
from datetime import datetime
from pathlib import Path
from src.file_data_extractor import FileDataExtractor


class FileOrganiser:
    def __init__(self, directory: str):
        self.directory = directory

    def organize_files(self):
        if not os.path.isdir(self.directory):
            print("Invalid directory path.")
            return

        supported_extensions = {".jpg", ".jpeg", ".png", ".mp4", ".mov", ".raw"}
        log = []

        for file_path in Path(self.directory).rglob("*"):
            if file_path.suffix.lower() not in supported_extensions:
                continue

            

        with open(Path(self.directory) / "rename_log.txt", "w") as log_file:
            log_file.write("\n".join(log))

        print("Files have been organized and logged.")

    def __decide_file_new_name(self, file_path: Path) -> str:
        file_data_extractor = FileDataExtractor(file_path)
        oldest_date_property: datetime = file_data_extractor.get_oldest_file_date_property()
        date_hint_from_folder: datetime | None = file_data_extractor.get_date_hint_from_folder()
        date_from_name: datetime | None = file_data_extractor.extract_date_from_name()

        # TODO figure out what to do here
        return "file-new-name"