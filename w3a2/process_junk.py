from pathlib import Path

# Resolve junk.txt relative to this script's folder, so it works from any cwd
FILE_PATH = Path(__file__).with_name("junk.txt")
OUTPUT_PATH = Path(__file__).with_name("junk_copy.txt")

print("Processing file:", FILE_PATH)

# Open and read the file
with open(FILE_PATH, "r") as f:
    lines = f.readlines()

# 1. Total number of lines in the file
total_lines = len(lines)
print("Total number of lines:", total_lines)

# 3. Convert all text to lowercase (join back into a single string)
content = "".join(lines).lower()

# 2. Add a new line at the end of the file
content += "text file nanalyssis\n"

# 4. Save the processed content to a copy (original junk.txt is left untouched)
with open(OUTPUT_PATH, "w") as f:
    f.write(content)

print("Processed file saved to", OUTPUT_PATH)
