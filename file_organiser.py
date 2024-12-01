import os
import shutil

# Define the directory to be organized
directory_to_organize = "/Users/iasonaszakynthinos/Desktop/destop"  # Change this to your target directory

# Define file type categories and corresponding folders
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Others': []  # All other file types
}

# Create folders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(directory_to_organize, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to move files to the appropriate folders
def organize_files():
    for filename in os.listdir(directory_to_organize):
        # Skip directories
        if os.path.isdir(os.path.join(directory_to_organize, filename)):
            continue
        
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        
        # Move files to the corresponding folder based on file extension
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(
                    os.path.join(directory_to_organize, filename),
                    os.path.join(directory_to_organize, folder, filename)
                )
                moved = True
                break
        
        # Move files with unknown extensions to the 'Others' folder
        if not moved:
            shutil.move(
                os.path.join(directory_to_organize, filename),
                os.path.join(directory_to_organize, 'Others', filename)
            )

# Run the organize_files function
if __name__ == "__main__":
    organize_files()
    print("Files have been organized.")
