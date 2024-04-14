import os
import uuid


class FileUtils:

    @staticmethod
    def save(file, upload_dir: str) -> str:
        try:
            # check if file is empty
            if file.filename == "":
                return "No selected file"

            # create dir if doesn't exist
            os.makedirs(upload_dir, exist_ok=True)

            # modify file name
            filename = FileUtils.get_unique_filename(file.filename)

            # get full path
            path = os.path.join(upload_dir, filename)

            # Save file
            file.save(path)

            # return path
            return path
        except Exception as e:
            return None

    @staticmethod
    def delete() -> bool:
        try:
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_unique_filename(filename):
        # Generate a unique identifier
        unique_id = uuid.uuid4().hex
        # Split the filename and extension
        name, ext = os.path.splitext(filename)
        # Concatenate the unique identifier with the filename
        return f"{unique_id}_{name}{ext}"
