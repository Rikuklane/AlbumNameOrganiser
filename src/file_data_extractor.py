import os
import re
import platform
from pathlib import Path
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

class FileDataExtractor:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    file_name: str = lambda self: self.file_path.name
    file_parent_folder_name: str = lambda self: self.file_path.parent.name

    def extract_date_from_name(self) -> datetime | None:
        patterns = [
            # yyyyMMdd_HHmmss or yyyyMMdd-HHmmss with optional milliseconds
            r"(?:.*_)?(\d{4})(\d{2})(\d{2})[-_]?(\d{2})(\d{2})(\d{2})(?:[-_]?(\d{3}))?",
            r"(?:.*-)?(\d{4})-(\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{2})[-_]?(\d{3})?",  # yyyy-MM-dd-HH-mm-ss-SSS
            r"(\d{13})",  # Unix timestamp in milliseconds
        ]
        for pattern in patterns:
            match = re.search(pattern, self.file_name)
            if match:
                try:
                    # Handle Unix timestamps
                    if len(match.groups()) == 1 and len(match.group(1)) == 13:
                        return datetime.fromtimestamp(int(match.group(1)) / 1000)
                    # Handle general datetime patterns
                    return datetime(*map(int, filter(None, match.groups())))
                except ValueError:
                    pass
        return None

    def get_oldest_file_date_property(self) -> datetime:
        creation_date = self.__get_creation_date()
        modification_date = os.path.getmtime(self.file_path)
        min_date = datetime.fromtimestamp(min(creation_date, modification_date))
        exif_date = self.__get_exif_date()
        if exif_date:
            return min(min_date, exif_date)
        return min_date

    def __get_creation_date(self) -> float:
        """
        Try to get the date that a file was created, falling back to when it was
        last modified if that isn't possible.
        See http://stackoverflow.com/a/39501288/1709587 for explanation.
        """
        if platform.system() == 'Windows':
            return os.path.getctime(self.file_path)
        else:
            stat = os.stat(self.file_path)
            try:
                return stat.st_birthtime
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here,
                # so we'll settle for when its content was last modified.
                return stat.st_mtime

    def __get_exif_date(self) -> datetime | None:
        if self.file_path.suffix.lower() not in {".jpg", ".jpeg"}:
            return None
        try:
            image = Image.open(self.file_path)
            exif_data = image.getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name == "DateTime":
                        return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
        except Exception:
            pass
        return None

    def get_date_hint_from_folder(self) -> datetime | None:
        folder_date_match = re.search(r"(\d{4})(?:_(\d{2}))?(?:_(\d{2}))?", self.file_parent_folder_name)
        if folder_date_match:
            try:
                year = int(folder_date_match.group(1))
                month = int(folder_date_match.group(2)) if folder_date_match.group(2) else 1
                day = int(folder_date_match.group(3)) if folder_date_match.group(3) else 1
                folder_date = datetime(year, month, day)
                return folder_date
            except ValueError:
                pass
        return None