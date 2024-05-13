def read_input(file_path):
    rounds = []
    with open(file_path, 'r') as file:
        for line in file:
            shape, outcome = line.strip().split()
            rounds.append((shape, outcome))
    return rounds

def calculate_score(rounds):
    shape_outcome_scores = {
        ('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8,
        ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
        ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7
    }

    score = sum(shape_outcome_scores[shape_outcome] for shape_outcome in rounds)
    return score

# Main program
file_path = "trial[1].txt"  # Replace with the path to your input file
rounds = read_input(file_path)
total_score = calculate_score(rounds)
print("Total Score:", total_score)
