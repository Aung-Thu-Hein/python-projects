import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory, '{directory}', does not exist")
        return

    file_types = {
        'documents': ['.odt', '.xlsx', '.ods', '.odt', '.docx', '.pdf'],
        'texts': ['.txt'],
        'figmas': ['.fig'],
        'xmls': ['.xml'],
        'images': ['.png', '.jpg', '.jpeg'],
        'others': []
    }

    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file_path)

        moved = False
        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(directory, 'others', filename))

    print(f"The directory {directory} has been origanized.")

directory_to_organize = input("Enter the path of the directory to organize: ")
organize_files(directory_to_organize)
