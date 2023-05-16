import os  
import shutil   

def remove_orphaned_original_jpgs(source_dir, target_dir, orphaned_dir):

    # Create the orphaned files directory if it doesn't exist  
    if not os.path.exists(orphaned_dir):  
        os.makedirs(orphaned_dir)  
  
    # Get the list of files in the source and target directories  
    source_files = set(os.listdir(source_dir))  
    target_files = os.listdir(target_dir)  
  
    # Iterate through the target files and check if they are present in the source directory  
    for file in target_files:  
        if file not in source_files:  
            # Move the orphaned file to the orphaned files directory  
            shutil.move(os.path.join(target_dir, file), os.path.join(orphaned_dir, file))  
            print(f"Moved orphaned file: {file}")

if __name__ == "__main__":
    source_dir = './low_res_photos'  
    target_dir = './photos'  
    orphaned_dir = './jpg_orphans'
    remove_orphaned_original_jpgs(source_dir, target_dir, orphaned_dir) 