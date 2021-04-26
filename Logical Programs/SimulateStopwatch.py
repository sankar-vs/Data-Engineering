'''
@Author: Sankar
@Date: 2021-04-01 10:17:14
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 19:45:46
@Title : SimulateStopwatch
'''
import time
def time_covert(seconds):
    '''
    Description:
        Converts given seconds to Hr:Min:Sec format and prints the time
    Parameter:
        seconds (float): difference between end_time and start_time in seconds
    Return:
        None
    '''
    minutes = seconds / 60
    seconds = seconds % 60
    hours = minutes / 60
    minutes = minutes % 60
    print("Time Lapsed = {}:{}:{}".format(int(hours), int(minutes), int(seconds)))

input("Press Enter to start timer")
start_time = time.time()

input("Press Enter to stop timer")
end_time = time.time()

time_lapsed = end_time - start_time
time_covert(time_lapsed)