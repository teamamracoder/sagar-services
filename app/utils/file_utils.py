import os
import uuid
from .common_utils import CommonUtils

class FileUtils:

    @staticmethod
    def save(dir: str, files) -> (list | str | None):
        try:
            # added default location for files
            upload_dir=os.path.join("app","static","uploads",dir)

            # create dir if doesn't exist
            os.makedirs(upload_dir, exist_ok=True)

            uploaded_path_list=[]
            for file in files:
                # check if file is empty
                if file.filename == "":
                    return ""
                
                # modify file name
                filename = FileUtils.get_unique_filename(file.filename)
            
                # get full path
                path = os.path.join(upload_dir, filename)
                # Save file
                file.save(path)
                
                # adding uploaded file path to a list
                uploaded_path_list.append(path.replace("\\","/").replace("app/",""))

            if len(uploaded_path_list)>1:       # multiple file inserted
                return uploaded_path_list
            elif len(uploaded_path_list)==1:    # single file inserted
                return  uploaded_path_list[0]
            else:                               # no file inserted
                return None

        except Exception as e:
            return None

    @staticmethod
    def delete(file_path) -> bool:
        try:
            path = os.path.join("app", *file_path.split("/"))
            os.remove(path)
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_unique_filename(filename):
        # eliminate special chars (except _)
        filename = CommonUtils.replace_special_characters_with_underscore(filename)
        # Generate a unique identifier
        unique_id = uuid.uuid4().hex
        # Split the filename and extension
        name, ext = os.path.splitext(filename)
        # Concatenate the unique identifier with the filename
        return f"{unique_id}_{name}{ext}"
