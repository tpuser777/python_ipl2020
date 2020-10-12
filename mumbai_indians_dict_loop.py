# make a dictionary

team_composition = {
  "Keeper" : "Quinton de Kock",
  "Batsman 1" : "Rohit Sharma",
  "Batsman 2" : "Suryakumar Yadav",
  "Batsman 3" : "Ishan Kishan",
  "Batsman 4" : "Hardik Pandya",
  "All Rounder 1" : "Kieron POLLARD",
  "All Rounder 2" : "Krunal Pandya",
  "All Rounder 3" : "Rahul Chahar",
  "Bowler 1" : "James Pattinson",
  "Bowler 2" : "Trent Boult",
  "Bowler 3" : "Jasprit Bumrah",
}

for key in team_composition:
    print("%s --> %s" %(key, team_composition[key]))

print ("========")

for key in team_composition:
    print("%s #--#> %s" %(key, team_composition[key]))

print ("========")    

for key, value in team_composition.items():
    print("%s --> %s" %(key, value))
