def read_csv(filename):
    """Reads a CSV file and returns data as a list of lists"""
    data = []
    with open(filename, "r") as f:
        for line in f:
            row = line.strip().split(",")   # split by comma
            data.append(row)
    return data


def find_s_algorithm(data):
    target_col = len(data[0]) - 1
    hypothesis = None
    step = 1

    print("\n--- FIND-S ALGORITHM DEMONSTRATION ---\n")

    for row in data:
        if row[target_col].lower() == "yes":  
            if hypothesis is None:
                hypothesis = row[:-1]     
                print(f"Step {step}: First positive example -> Hypothesis = {hypothesis}")
            else:
                print(f"Step {step}: Comparing with {row[:-1]}")
                for i in range(len(hypothesis)):
                    if hypothesis[i] != row[i]:
                        hypothesis[i] = "?"
                print(f"Updated Hypothesis: {hypothesis}")
            step += 1
        else:
            print(f"Step {step}: Negative example ignored -> {row[:-1]}")
            step += 1

    return hypothesis

if __name__ == "__main__":
    # Example CSV format:
    # Sunny,Warm,Normal,Strong,Warm,Same,Yes
    # Sunny,Warm,High,Strong,Warm,Same,Yes
    # Rainy,Cold,High,Strong,Warm,Change,No
    # Sunny,Warm,High,Strong,Cool,Change,Yes

    filename = "training.csv"   # Path to your file
    import os
    print("Looking for file in:", os.getcwd())

    data = read_csv(filename)
    final_hypothesis = find_s_algorithm(data)
