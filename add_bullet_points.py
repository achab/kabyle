import os

indices = [44]

for i in indices:
    filename = f"cours_{i}.md"
    new_filename = f"original_cours_{i}.md"
    os.rename(filename, new_filename)

for i in indices:
    original_filename = f"original_cours_{i}.md"
    new_filename = f"cours_{i}.md"
    original = open(original_filename, "r")
    new = open(new_filename, "w")

    for line in original.readlines():
        if len(line) > 1 and line[0] not in ["#", "-"]:
            new.write(f"- {line}")
        else:
            new.write(line)

    original.close()
    new.close()
