def which_prize(points):
    prize = ""
    if points <= 50 and points >= 0 :
        prize = "wooden rabbit"
    elif points > 150 and points <= 180 :
        prize = "wafer-thin mint"
    elif points > 180 and points <= 200 :
        prize = "penguin"
    if prize == "" :
        return "Oh dear, no prize this time."
    else :
        return "Congratulations! You have won a " + prize + "!"



print(which_prize(51))
print(which_prize(121))
print(which_prize(183))
print(which_prize(50)) 