import csv
def passwd_to_csv(source: str, dest: str):
    with open(source, "r") as src, open(dest, "w") as dst:
        writer = csv.writer(dst, delimiter="\t")
        
        for line in src:
            if line.strip() and not line.startswith("#"):
                username, _, id, *_ = line.strip().split(":")
                writer.writerow([username, id])
    