from random import shuffle as shuffle
from random import sample as sample
from statistics import mean as mean
from statistics import stdev as stdev
from math import sqrt as sqrt


trial = 0
trialLevelTracker = [[] for x in range(0,11)]
trialLimit = 10000
while trial < trialLimit:
    # Generate a random list of matching 'animals' (numbers)
    matchList = []
    for x in range(0,10):
        matchList.append(x)
        matchList.append(x)
    shuffle(matchList)

    # Randomly sample until all matches found
    step = 0
    matches = 0
    tracker = [0]
    myLimit = 1000

    while len(matchList) > 0:
        step += 1
        choice = sample(matchList, 2)
        if choice[0] == choice[1]:
            matches += 1
            tracker.append(step - sum(tracker))
            matchList = [x for x in matchList if x != choice[0]]

    # Track data across trials for stats analysis at the end
    trialLevelTracker[0].append(step)
    for x in range(1,11):
        trialLevelTracker[x].append(tracker[x])
    trial += 1

# Calculate final answer from trial data and print to screen
avgTotalGuesses = mean(trialLevelTracker[0])
sd = stdev(trialLevelTracker[0], avgTotalGuesses)
confInterval = 2.576 * (sd / sqrt(len(trialLevelTracker[0])))
output = f'Average guesses are {avgTotalGuesses:.2f} - distributed to find each match:\n'
for x in range(1,11):
    output += f'{x}: {mean(trialLevelTracker[x]):.2f}\n'
output += f'Total time to play: {int((avgTotalGuesses * 2) / 60)} mintues {((avgTotalGuesses * 2) % 60):.2f} seconds'
output += f' +/- {(confInterval * 2):.2f} seconds (99% confidence interval)'
print(output)
