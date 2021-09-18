import time as timeLib
import activityVoice

def startCycles(cycleCount, workTime, breakTime):

    for cycle in range(cycleCount):
        cycle += 1
        activityVoice.playAudio("Cycle " + str(cycle) + " starts")

        for i in range(2):
            if i == 0:
                time = workTime * 60
                activityVoice.playAudio("Work for Cycle " + str(cycle) + " starts, concentrate harder")
            else:
                time = breakTime * 60
                activityVoice.playAudio("Break for Cycle " + str(cycle) + " starts, Take a break")

            while time:
                mins, secs = divmod(time, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                timeLib.sleep(1)
                time -= 1
            
            if i == 0:
                activityVoice.playAudio("Work for Cycle " + str(cycle) + " is completed")
            else:
                activityVoice.playAudio("Break for Cycle " + str(cycle) + " is completed")
        
        activityVoice.playAudio("All the activities of Cycle " + str(cycle) + " are completed")
        
    activityVoice.playAudio("Every Cycles are completed, Good job, keep going")