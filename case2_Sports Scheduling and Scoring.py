# Case Study 92: Sports Scheduling and Scoring

# Event tuple: (event, team1, team2, time)
events = [
    ("Cricket", "Team A", "Team B", "10:00"),
    ("Football", "Team C", "Team D", "10:00"),
    ("Volleyball", "Team A", "Team C", "11:00"),
    ("Basketball", "Team B", "Team D", "12:00")
]

# Result tuple: (event, winner)
results = [
    ("Cricket", "Team A"),
    ("Football", "Team D"),
    ("Volleyball", "Team A"),
    ("Basketball", "Team B")
]

teams = ["Team A", "Team B", "Team C", "Team D"]
points = [0, 0, 0, 0]

print("SCHEDULE")
for event in events:
    print(event)

print("\nSCHEDULING CONFLICTS")

conflicts = 0

for i in range(len(events)):
    for j in range(i + 1, len(events)):
        event1, team1a, team1b, time1 = events[i]
        event2, team2a, team2b, time2 = events[j]

        if time1 == time2:
            print(event1, "and", event2,
                  "occur at the same time")
            conflicts += 1

print("Total time conflicts:", conflicts)

# Award 3 points for a win
for event_name, winner in results:
    for i in range(len(teams)):
        if teams[i] == winner:
            points[i] += 3

# Create ranking records
ranking = []

for i in range(len(teams)):
    ranking.append((teams[i], points[i]))

# Sort by points in descending order
for i in range(len(ranking)):
    for j in range(i + 1, len(ranking)):
        if ranking[j][1] > ranking[i][1]:
            ranking[i], ranking[j] = ranking[j], ranking[i]

print("\nFINAL RANKINGS")
for position, (team, score) in enumerate(ranking, start=1):
    print(position, team, score, "points")