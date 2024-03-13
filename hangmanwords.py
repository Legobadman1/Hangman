import random


def randomanimal():
    animal_words = [
    "elephant", "giraffe", "cheetah", "monkey", "rhino",
    "zebra", "kangaroo", "hippo", "crocodile", "parrot",
    "gorilla", "octopus", "whale", "dolphin", "penguin",
    "seagull", "jaguar", "lizard", "rabbit", "hamster",
    "turtle", "hedgehog", "armadillo", "squirrel", "beaver",
    "butterfly", "spider", "crab", "lobster", "caterpillar",
    "dragonfly", "elephant", "giraffe", "cheetah", "monkey",
    "rhino", "zebra", "kangaroo", "hippo", "crocodile", 
    "parrot", "gorilla", "octopus", "whale", "dolphin", 
    "penguin", "seagull", "jaguar", "lizard", "rabbit"
    ]
    return random.choice(animal_words)


def randomlocation():
    location_names = [
    "school", "park", "hospital", "beach", "library",
    "garden", "restaurant", "cinema", "cafe", "market",
    "stadium", "gym", "airport", "trainstation", "busstop",
    "mall", "office", "hotel", "apartment", "house",
    "street", "alley", "bridge", "playground", "zoo",
    "golfcourse", "skatepark", "campground", "lake", "river",
    "forest", "mountain", "hill", "valley", "desert",
    "ocean", "sea", "lake", "pond", "island",
    "cave", "volcano", "waterfall", "waterpark", "toilet",
    "bathroom", "bedroom", "kitchen", "livingroom", "garage"
    ]
    return random.choice(location_names)