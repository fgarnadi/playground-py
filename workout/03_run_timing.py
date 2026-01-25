def run_timing():
    runs = []
    while True:
        raw = input("Enter 10 km run time: ")
        if not raw:
            break

        try:
            run = float(raw)
        except ValueError:
            print("Please input a whole number.")
            continue

        runs.append(run)

    if runs:
        average = sum(runs) / len(runs)
        print(f"\nAverage of {average:.2f} over {len(runs)} runs")


if __name__ == "__main__":
    run_timing()
