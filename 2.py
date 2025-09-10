import csv

def load_data(filename):
    concepts = []
    target = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            concepts.append(row[:-1])
            target.append(row[-1])
    return concepts, target

def candidate_elimination(concepts, target):
    specific_h = concepts[0].copy()
    general_h = [['?' for _ in range(len(specific_h))]]  # most general

    print("\nInitial Specific Hypothesis:", specific_h)
    print("Initial General Hypothesis:", general_h)

    for i, instance in enumerate(concepts):
        if target[i].lower() == "yes":
            # Positive example: update S
            for j in range(len(specific_h)):
                if instance[j] != specific_h[j]:
                    specific_h[j] = '?'
            # Remove G inconsistent with S
            general_h = [g for g in general_h if all(
                g[j] == '?' or g[j] == specific_h[j] for j in range(len(specific_h))
            )]
        else:
            # Negative example: specialize G
            new_general = []
            for g in general_h:
                for j in range(len(specific_h)):
                    if g[j] == '?':
                        h = g.copy()
                        h[j] = specific_h[j]
                        if h not in new_general:
                            new_general.append(h)
                    elif g[j] != instance[j]:
                        if g not in new_general:
                            new_general.append(g)
            general_h = new_general

        print(f"\nAfter instance {i+1} ({instance}, {target[i]}):")
        print("Specific Hypothesis:", specific_h)
        print("General Hypothesis:", general_h)

    return specific_h, general_h

# Run
filename = "training.csv"
concepts, target = load_data(filename)
s_final, g_final = candidate_elimination(concepts, target)

print("\n================== FINAL RESULT ==================")
print("Final Specific Hypothesis:", s_final)
print("Final General Hypothesis:", g_final)
