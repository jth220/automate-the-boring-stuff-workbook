# chapter 11 - organising files

automating tasks such as copying, renaming, moving, deleting and compressing files

**shutil module** 

- `shutil.copy(src, dest)` → copies file to dest folder or new name.
- `shutil.copytree(src, dest)` → copies entire folder tree.

**Move/Rename**:

- `shutil.move(src, dest)` → moves file/folder.
    - If `dest` is folder → move inside.
    - If `dest` is filename → rename.

- **Delete**:
    - `shutil.rmtree(path)` → delete folder + all contents.
    - `os.unlink(path)` → delete single file.
    - `os.rmdir(path)` → delete empty folder.
- ⚠️ Be careful — permanent deletes!
- 🔄 Best practice: do a **dry run** with `print()` before real delete/move.

```python
import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    os.unlink(filename)
```

```python
import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    #os.unlink(filename)
    print('Deleting', filename)
```

## Safer Deletion with send2trash

- `send2trash.send2trash(path)` → moves file/folder to recycle bin instead of permanent delete.
- Safer but doesn’t free disk space until emptied.

## Walking Directory Trees

- **List folder contents**:
    - `os.listdir(path)` → list names in folder.
    - `Path(path).iterdir()` → list Path objects.
- **Walk tree**:
    - `os.walk(path)` → yields `(folder_name, subfolders, filenames)`.
    - Useful for recursive file operations (renaming, backing up).

Example Programs

```python
import os

folder = "C:/Users/Al/spam"
for name in os.listdir(folder):
    print(name)
```

```python
from pathlib import Path

folder = Path("C:/Users/Al/spam")
for item in folder.iterdir():
    print(item)
```

```python
import os

for folder_name, subfolders, filenames in os.walk("C:/Users/Al/spam"):
    print(f"Current folder: {folder_name}")

    for subfolder in subfolders:
        print(f"  SUBFOLDER: {subfolder}")

    for filename in filenames:
        print(f"  FILE: {filename}")
```