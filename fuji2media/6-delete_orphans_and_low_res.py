import os
import shutil   

def prepare_dirs_for_deletion(dirs_to_delete, deletion_dir):
    if not os.path.exists(deletion_dir):  
            os.makedirs(deletion_dir)

    for dir in dirs_to_delete:
          shutil.move(dir, deletion_dir)
          print(f"prepared {dir} for deletion")

if __name__ == "__main__":
      dirs_to_delete = ["./low_res_photos", "jpg_orphans", "raw_orphans"]
      deletion_dir = "./DELETE_ME"
      prepare_dirs_for_deletion(dirs_to_delete, deletion_dir)