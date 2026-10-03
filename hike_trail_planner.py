trails = []
trail_lengths = []
elevations = []
difficultys = []
trail_number = 0
number_of_match_trails = 0

does_difficulty_match = []
match_trail_numbers = []

match_trails = []
match_lengths = []
match_elevations = []
match_hike_times = []

with open("trails.csv", "r") as file:
    file.readline()
    for line in file:
        parts = line.strip().split(",")
        trail = parts[0]
        trails.append(trail)
        trail_length = float(parts[1])
        trail_lengths.append(trail_length)
        elevation = float(parts[2])
        elevations.append(elevation)
        difficulty = parts[3]
        difficultys.append(difficulty)
        
        
def estimate_hike_time(match_length, match_elev):
    e_h_t_unround = match_length/2 + match_elev/2000
    e_h_t_round = round(e_h_t_unround, 2)
    return e_h_t_round

max_hike_time = float(input("Enter maximum hiking time (in hours): "))
desired_difficulty = input("Enter desired difficulty (Easy, Moderate, or Hard): ")
    
if desired_difficulty == "Easy":
    for difficulty in difficultys:
        if difficulty == "Easy":
            does_difficulty_match.append("Y")
        else:
            does_difficulty_match.append("N")
            
if desired_difficulty == "Moderate":
    for difficulty in difficultys:
        if difficulty == "Moderate":
            does_difficulty_match.append("Y")
        else:
            does_difficulty_match.append("N")
    
if desired_difficulty == "Hard":
    for difficulty in difficultys:
        if difficulty == "Hard":
            does_difficulty_match.append("Y")
        else:
            does_difficulty_match.append("N")
            

for does_difficulty_match in does_difficulty_match:
    if does_difficulty_match == "Y":
        match_trail_numbers.append(trail_number)
    trail_number += 1
    
for match_trail_number in match_trail_numbers:
    match_length = float(trail_lengths[match_trail_number])
    match_lengths.append(match_length)
    match_elev = elevations[match_trail_number]
    match_elevations.append(match_elev)
    match_hike_time = estimate_hike_time(match_length, match_elev)
    if match_hike_time <= max_hike_time:
        match_hike_times.append(match_hike_time)
        match_trail = (trails[match_trail_number])
        match_trails.append(match_trail)
        number_of_match_trails += 1
        
def final_results(match_trail, match_hike_time):
    count_a = 0
    for match_trail in match_trails:
        print(match_trail, "-", match_hike_times[count_a], "hours \n")
        count_a += 1

print("\n Number of trails matching your plan: ", number_of_match_trails, "\n")
final_results(match_trail, match_hike_time)