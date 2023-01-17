# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#part 1

player_score1 = ("Ruud Gullit")
player_score2 = ("Marco van Basten")

goal_0 = 32
goal_1 = 54 

scorers = (player_score1 + " " + str(goal_0)+ "," + " " + player_score2 + " " +str(goal_1))

print  (scorers)

qa = f"{player_score1} scored in the {goal_0}nd minute" 
qa2 = f"{player_score2} scored in the {goal_1}th minute" 

report = qa + "\n" + qa2

print (report)

player = "Ronald Koeman"

first_name = player[:player.find(" ")]

print(first_name)

last_name_len = ( len(player[7:])) 

print (last_name_len)

# part 2

name_short = "R. Koeman" 

chant = ("Ronald! " *6)[:-1]

print (chant)

good_chant = chant[-1] != " "

print (good_chant)


