import math


def Chance_for_x_successes(success_amount, success_barrier, dice_thrown_amount, amount_of_sides):

    if success_amount > dice_thrown_amount:
        return 'Incorrect input (amount of successes > amount of dice thrown)!'

    # make the set bigger,to match the success_barrier
    i = (amount_of_sides - success_barrier) + 1

    # Math equation
    p = (i/amount_of_sides)
    combination = math.factorial(dice_thrown_amount)/(math.factorial(success_amount) * math.factorial(dice_thrown_amount - success_amount))
    probability = (combination * (p**success_amount) * (1-p)**(dice_thrown_amount - success_amount)) * 100

    if probability <= 0:
        probability = 0
    if probability > 100:
        probability = 100

    probability = str(round(probability, 5)) + '%'

    return probability

def Chance_for_1(success_barrier, dice_thrown_amount, amount_of_sides, success_amount):

    i = (amount_of_sides - success_barrier) + 1

    # Chance for success
    p = (i / amount_of_sides)

    # math for exactly 1 success
    combination = math.factorial(dice_thrown_amount) / (
                math.factorial(success_amount) * math.factorial(dice_thrown_amount - success_amount))
    probability = (combination * (p ** success_amount) * (1 - p) ** (dice_thrown_amount - success_amount)) * 100

    # math for exactly 1,2,3,4,5... dice_thrown_amount success summed up
    for i in range(dice_thrown_amount-1):
        success_amount += 1
        combination = math.factorial(dice_thrown_amount) / (
                math.factorial(success_amount) * math.factorial(dice_thrown_amount - success_amount))
        probability += (combination * (p ** success_amount) * (1 - p) ** (dice_thrown_amount - success_amount)) * 100

    # grammatical variation
    if probability <= 0:
        probability = 0
    if probability > 100:
        probability = 100

    probability = str(round(probability, 5)) + '%'

    return probability


def Chance_every_side_equal_x(dice_thrown_amount, amount_of_sides, expected_value):

    if expected_value > amount_of_sides:
        return 'Incorrect input (X > amount of sides)'
    if expected_value <= 0:
        return 'Incorrect input (X <= 0)'

    probability = (1/amount_of_sides)**dice_thrown_amount * 100

    if probability <= 0:
        probability = 0
    if probability > 100:
        probability = 100

    probability = str(round(probability, 5)) + '%'

    return probability


def Chance_equal_greater(dice_thrown_amount, amount_of_sides, value):

    if value > amount_of_sides:
        return 'Incorrect input (X > amount of sides)'
    if value <= 0:
        return 'Incorrect input (X <= 0)'

    probability = ((amount_of_sides - value + 1)/amount_of_sides)**dice_thrown_amount * 100

    if probability <= 0:
        probability = 0
    if probability > 100:
        probability = 100

    probability = str(round(probability, 5)) + '%'

    return probability


def Chance_equal_lower(dice_thrown_amount, amount_of_sides, value):

    if value > amount_of_sides:
        return 'Incorrect input (X > amount of sides)'
    if value <= 0:
        return 'Incorrect input (X <= 0)'

    probability = (value/amount_of_sides)**dice_thrown_amount * 100

    if probability <= 0:
        probability = 0
    if probability > 100:
        probability = 100

    probability = str(round(probability, 5)) + '%'

    return probability
