def reverse_lines(source: str, dest: str):
    with open(source, "r") as src, open(dest, "w") as dst:
        for line in src:
            dst.write(line.strip()[::-1] + "\n")
