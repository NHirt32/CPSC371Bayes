
def unknown_mushroom_list_probability(known_mushroom_list, unknown_mushroom_list):
    for index in range(len(unknown_mushroom_list)):
        edibility_odds = (x_probability(known_mushroom_list,unknown_mushroom_list[index]) *
                          x_probability_given_edible(known_mushroom_list,unknown_mushroom_list[index]))/ edible_probability(known_mushroom_list)
        poison_odds = (x_probability(known_mushroom_list, unknown_mushroom_list[index]) *
                          x_probability_given_poisonous(known_mushroom_list,
                                                     unknown_mushroom_list[index])) / poison_probability(known_mushroom_list)
        if edibility_odds > poison_odds:
            unknown_mushroom_list[index][0] = 'e'
        else:
            unknown_mushroom_list[index][0] = 'p'


def x_probability(known_mushroom_list, unknown_mushroom):
    # This function iterates through every attribute in a given unknown mushroom and compares it to our list of known mushrooms
    probability = 1 # We start our probability at 100* so we can multiply by each discovered probability
    mushroom_attribute_count = 22  # Variable to check the number of attributes our mushroom contains
    attribute_position = 1 # We start at one to ignore the edibility column
    while attribute_position < mushroom_attribute_count:    # We are going to iterate through every attribute of our unknown_mushroom
        current_attribute = unknown_mushroom[attribute_position]
        shared_attributes = 0
        for index in range(len(known_mushroom_list)):
            if known_mushroom_list[index][attribute_position] == current_attribute: # If our current attribute is present at an index +=1 to shared attributes
                shared_attributes += 1
        shared_over_total = shared_attributes/len(known_mushroom_list)
        probability = probability * (shared_attributes/len(known_mushroom_list)) # P(A) AND P(B) = P(A) * P(B)
        attribute_position += 1
    return probability

def x_probability_given_edible(known_mushroom_list, unknown_mushroom):
    # Very similar to x_probability, however, before adding something to our shared attribute count we must also confirm that it is edible
    # Debug print
    probability = 1 # We start our probability at 100* so we can multiply by each discovered probability
    mushroom_attribute_count = 22  # Variable to check the number of attributes our mushroom contains
    attribute_position = 1 # We start at one to ignore the edibility column
    while attribute_position < mushroom_attribute_count:    # We are going to iterate through every attribute of our unknown_mushroom
        current_attribute = unknown_mushroom[attribute_position]
        shared_attributes = 0
        for mushrooms in known_mushroom_list:
            if mushrooms[attribute_position] == current_attribute and mushrooms[0] == 'e':
                shared_attributes += 1
        shared_over_total = shared_attributes / len(known_mushroom_list)
        probability = probability * shared_over_total  # P(A) AND P(B) = P(A) * P(B)
        attribute_position += 1
    return probability

def x_probability_given_poisonous(known_mushroom_list, unknown_mushroom):
    # Very similar to x_probability, however, before adding something to our shared attribute count we must also confirm that it is poisonous
    # Debug print
    probability = 1 # We start our probability at 100* so we can multiply by each discovered probability
    mushroom_attribute_count = 22  # Variable to check the number of attributes our mushroom contains
    attribute_position = 1 # We start at one to ignore the edibility column
    while attribute_position < mushroom_attribute_count:    # We are going to iterate through every attribute of our unknown_mushroom
        current_attribute = unknown_mushroom[attribute_position]
        shared_attributes = 0
        for mushrooms in known_mushroom_list:
            if mushrooms[attribute_position] == current_attribute and mushrooms[0] == 'p':
                shared_attributes += 1
        shared_over_total = shared_attributes / len(known_mushroom_list)
        probability = probability * shared_over_total  # P(A) AND P(B) = P(A) * P(B)
        attribute_position += 1
    return probability

def edible_probability(known_mushroom_list):
    edible_count = 0
    for mushrooms in known_mushroom_list:
        if mushrooms[0] == 'e':
            edible_count += 1
    probability = edible_count/len(known_mushroom_list)
    return probability

def poison_probability(known_mushroom_list):
    edible_count = 0
    for mushrooms in known_mushroom_list:
        if mushrooms[0] == 'p':
            edible_count += 1
    probability = edible_count/len(known_mushroom_list)
    return probability
