import os
import sys

if len(sys.argv) < 2:
    print("Usage: python rename_files.py /path/to/folder")
    sys.exit(1)

folder = sys.argv[1]

# List all files
files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
files.sort()

# Rename files
for i, filename in enumerate(files):
    ext = os.path.splitext(filename)[1]
    new_name = f"{i:07d}{ext}"
    src = os.path.join(folder, filename)
    dst = os.path.join(folder, new_name)
    os.rename(src, dst)

print(f"Renamed {len(files)} files.")

