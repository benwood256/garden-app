# Hardcoded values for the season and plant type
season = input("Enter your favourite season: ") 
plant_type = input("Enter your favourite plant: ") 

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
# depending on what the user set as the season, the advice variable will be updated
# there is a specific advice set for summer & winter but none for spring & autumn
# there is nothing stopping someone from entering a string that isn't a season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
# depending on what the user set as their favourite plant type, the advice variable will be updated
# if the user specified a unique plant type, there will be a string 'No advice for this type of plant.'
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
