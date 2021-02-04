'''

先谢谢大家，求问一道脸书的python题。 写code 把stream 改成 real-time data 实时
更新每步的平均时间。

input：[session, step, time_start] | data like [[a,1,110], [a,2,120], 
[a,3,150], [b,1,110],[b,2,190],[b,3,220]]
output: {1:45, 2:35}

我的理解是，点在于如何随时有新的[session, step, time_start] 进行实时更新output。
使用extend() 新的input吗？求各位大神赐教


'''

outputDict = {} #{1:45, 2:35}
sessionDict = {} #{'a':[1,110], 'b':[1,110]} keep the latest step of each session
stepCountDict = {} #{1:2, 2:2}
 
#input [a,1,110]
def step_avg_time(session, step, time_start):
    last_session = sessionDict.get(session)
    #for new session, no change
    if not last_session:
        sessionDict[session] = [step, time_start]
        stepCountDict[step] = stepCountDict.get(step,0) + 1
        return outputDict

    time_spend = time_start - last_session[1]
    last_step = last_session[0]
    step_avg = outputDict.get(last_step, 0.0)
    #update the average
    step_avg = step_avg + (time_spend - step_avg) / (stepCountDict.get(last_step,0) + 1)
    outputDict[last_step] = step_avg
    #update the sessionDict
    sessionDict[session] = [step, time_start]
    #update stepCountDict
    print('laststep', last_step)
    stepCountDict[last_step] = stepCountDict.get(last_step,0) + 1
    return outputDict
 
#call the function
if __name__ == "__main__":

    inputList = [['a',1,110], ['a',2,120], ['a',3,150], 
                 ['b',1,110], ['b',2,190], ['b',3,220]]
    for i in inputList:
        print(step_avg_time(*i))