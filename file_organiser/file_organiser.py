import os
import shutil


file_categories = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Images": [".png", ".jpg"],
    "Others": []
}


def organise_files(directory):

    if not os.path.isdir(directory):
        print(f"{directory} is an invalid directory")
        return

    for category in file_categories:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    for filename in os.listdir(directory):

        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        category_found = False

        for category, extensions in file_categories.items():

            if any(filename.lower().endswith(ext) for ext in extensions):

                shutil.move(
                    file_path,
                    os.path.join(directory, category, filename)
                )

                category_found = True
                break

        if not category_found:
            shutil.move(
                file_path,
                os.path.join(directory, "Others", filename)
            )


organise_directory = input("Enter directory path: ")
organise_files(organise_directory)


