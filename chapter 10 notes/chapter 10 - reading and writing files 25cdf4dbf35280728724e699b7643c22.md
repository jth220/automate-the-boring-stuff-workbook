# chapter 10 - reading and writing files

**Files and Filepaths**

- File = data stored permanently on disk
- Contains filename + path
- Path = location of file in filesystem
- File name extension (e.g., .docx, .txt) tells type
- Folders = directories; can contain files and + subfolders
- Root folder: **C:\** on Windows or **\** (macOS/Linux)
- Drives : Windows (D:\, E:\), macOS (\Volumes), Linux(\mnt)

Path Separators & pathlib

- Windows uses \
- pathlib.Path() normalises across OS.

```python
from pathlib import Path
Path('spam', 'bacon', 'eggs')  
# WindowsPath('spam/bacon/eggs')

```

Following from this example

- Path converts it into a WindowsPath object for the joined path
- However note that this is separators used in linux
- If you wanted a Windows seperator, you would have to convert it into a string

```python
returns 'spam\\bacon\\eggs'
```

- backslash is used to escape the other backslashes
- Path can join a path object and a string using the / operator

```python
>>> from pathlib import Path
>>> Path('spam') / 'bacon' / 'eggs'
WindowsPath('spam/bacon/eggs')
>>> Path('spam') / Path('bacon/eggs')
WindowsPath('spam/bacon/eggs')
>>> Path('spam') / Path('bacon', 'eggs')
WindowsPath('spam/bacon/eggs')
```

```python
>>> from pathlib import Path
>>> my_files = ['accounts.txt', 'details.csv', 'invite.docx']
>>> for filename in my_files:
...     print(Path(r'C:\Users\Al', filename))
...
C:\Users\Al\accounts.txt
C:\Users\Al\details.csv
C:\Users\Al\invite.docx
```

Why we use Path()

- its thought as the blueprint for a location in your filesystem
- it doesnt have to exist currently, but there are formal descriptions of it that exists
- you can eventually make it real
- Rather than using a flat out string to give you the location of a file
- You can treat it as an object and perform methods

Current & Home Directories

- Where relative paths are based

```python
Path.cwd()        # get cwd
os.chdir(path)    # change cwd
```

**Absolute vs Relative Paths**

- **Absolute path**: starts at root (`C:\`, `/`).
- **Relative path**: based on CWD.
- Special names:
    - `.` = current folder.
    - `..` = parent folder.

Creating Folders

- `os.makedirs(path)` → creates intermediate folders.
- `Path(path).mkdir(parents=True)` → modern way.

## Handling & Inspecting Paths

- `is_absolute()` → check absolute path.
- `absolute()` → get absolute path.
- Path attributes:
    - `.anchor` = root
    - `.parent` = containing folder
    - `.name` = filename
    - `.stem` = base name (without extension)
    - `.suffix` = extension
    - `.drive` = drive letter (Windows only)
    - `.parts` = tuple of path components
    - `.parents[]` = ancestor directories

`Path.stat()` → size & timestamps.

- `st_size`: file size (bytes).
- `st_mtime`: last modified time (Unix epoch).
- `st_ctime`: creation (Windows) or metadata change (Unix).
- `st_atime`: last accessed.

## Finding Files (glob)

- Glob patterns:
    - `.txt` → all `.txt` files.
    - `project?.txt` → `project1.txt`, etc.
    - → all files.
- `Path.glob(pattern)` → returns generator of matching files.

'*.txt' matches all files that end with *.txt*.

'project?.txt' matches 'project1.txt', 'project2.txt', or 'projectX.txt'.

'*project?.*' matches 'catproject5.txt' or 'secret_project7.docx'.

'*' matches all filenames.

- treat glob like a simplified regex language, describe the pattern first

## Path Validity

- `p.exists()` → path exists?
- `p.is_file()` → is file?
- `p.is_dir()` → is directory?

## Reading & Writing Text Files

### Using pathlib - basic interaction

```python
p = Path('spam.txt')
p.write_text('Hello, world!')
p.read_text()

```

### Using `open()` - more common

3-step process:

1. `open(file, mode)` → returns File object.
2. `read()`, `readlines()`, `write()`
3. `close()`
- Modes:
    - `'r'`: read (default)
    - `'w'`: write (overwrite or create new)
    - `'a'`: append
- `encoding='utf-8'` recommended for cross-platform text files.

## 📌 Writing Example

```python
bacon_file = open('bacon.txt', 'w', encoding='utf-8')
bacon_file.write('Hello, world!\n')
bacon_file.close()

```

Append mode:

```python
bacon_file = open('bacon.txt', 'a', encoding='utf-8')
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()

```

## Using `with` Statements

- Automatically closes files.

```python
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, world!')

```

## shelve Module (Saving Variables)

- Store Python objects persistently in binary shelf files.
- Works like a dictionary.

```python
import shelve
s = shelve.open('mydata')
s['cats'] = ['Zophie', 'Pooka']
s.close()

```

- Creates files (`.bak`, `.dat`, `.dir` on Windows).
- Keys & values retrievable later.