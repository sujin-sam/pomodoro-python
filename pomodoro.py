import cycles

cycleCount = 0
activities = ""
activityTimeList = []

# get inputs
cycleCount = int(input("Pls enter the number of cycles: "))
activities = input("Pls enter the list of activities for each cycle (separated by comma, ex: work,break): ")

activityList = activities.split(',')

for i in range(len(activityList)):
    timeInput = int(input("Pls enter the time in minutes for " + activityList[i] + ": "))
    activityTimeList.append(timeInput)

cycles.startCycles(cycleCount, activityList, activityTimeList)
