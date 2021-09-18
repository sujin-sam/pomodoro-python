import time as timeObj

def startCycles(cycleCount, workTime, breakTime):

    for cycle in range(cycleCount):
        cycle += 1
        print("Cycle " + str(cycle) + " starts")

        for i in range(2):
            if i == 0:
                time = workTime * 60
                print("Work for Cycle " + str(cycle) + " starts, concentrate harder")
            else:
                time = breakTime * 60
                print("Break for Cycle " + str(cycle) + " starts, Take a break!!")

            while time:
                mins, secs = divmod(time, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                timeObj.sleep(1)
                time -= 1
            
            if i == 0:
                print("Work for Cycle " + str(cycle) + " is completed")
            else:
                print("Break for Cycle " + str(cycle) + " is completed")
        
        print("All the activities of Cycle " + str(cycle) + " are completed")
        
    print("Every Cycles are completed")
            

# get inputs
cycleCount = int(input("Enter the number of cycles: "))
workTime = int(input("Enter the time in minutes for work: "))
breakTime = int(input("Enter the time in minutes for break: "))

startCycles(cycleCount, workTime, breakTime)
