import time as timeLib
import activityVoice

def startCycles(cycleCount, activityList, activityTimeList):

    for cycle in range(cycleCount):
        cycle += 1
        activityVoice.playAudio("Cycle " + str(cycle) + " starts")

        for i in range(len(activityList)):
            time = activityTimeList[i] * 60
            boostWords = ""

            if activityList[i].lower() == "work":
                boostWords = "concentrate harder"
            elif activityList[i].lower() == "break":
                boostWords = "Take a break to fresh up"

            activityVoice.playAudio(activityList[i] + " for Cycle " + str(cycle) + " starts, " + boostWords)

            while time:
                try:
                    mins, secs = divmod(time, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(timer, end="\r")
                    timeLib.sleep(1)
                    time -= 1
                except KeyboardInterrupt:
                    activityVoice.playAudio(activityList[i] + " for Cycle " + str(cycle) + " is paused")
                    activityVoice.playAudio("press ENTER to resume or ctrl+c to exit...")
                    key = input()
                    activityVoice.playAudio(activityList[i] + " for Cycle " + str(cycle) + " is resumed")
                    continue
            
            activityVoice.playAudio(activityList[i] + " for Cycle " + str(cycle) + " is completed")
        
        activityVoice.playAudio("All the activities of Cycle " + str(cycle) + " are completed")
        
    activityVoice.playAudio("Every Cycles are completed, Good job, keep going")