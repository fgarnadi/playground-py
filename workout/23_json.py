import json
from collections import defaultdict
from glob import glob


def print_scores(path: str):
    for file in glob(f"{path}/*.json"):
        scores = defaultdict(list)
        with open(file, "r") as f:
            records = json.load(f)
            for record in records:
                for subject, score in record.items():
                    scores[subject].append(score)

        print(file)
        for subject, score in scores.items():
            print(
                f"  {subject}: min {min(score)}, max {max(score)}, average {sum(score) / len(score)}"
            )


if __name__ == "__main__":
    print_scores("files")
