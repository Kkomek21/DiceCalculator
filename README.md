# DiceCalculator
Dice throws probability.

Made mainly for fun, but also to integrate into future electronic projects.

All scenarios are flexible in the amount of sides on a die, amount of dice thrown, and sometimes the success barriers and success amounts etc. .

First few versions were made using itertools and NumPy, and were not optimised at all because of their premise. for all scenarios I created a real sample_space, by calculating the
cartesian product of all possible throw results for given amount of dice and amount of sides on 1 die, then using NumPy's Ufuncs I sifted out acceptable results for given scenarios.
Operating time was ok for up to 6-7 dice, but above that my computer started to have huge problems. Current version is done by pure math equations.

I hope someone will find it helpful :).
