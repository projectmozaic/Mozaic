#read the new activities
activities = open("Dockerfile").read()
print(type(activities))

#read the old version
log_his = open ( 'log.txt',"r" ).readlines()
if len(log_his) != 0:
    ver = log_his[len(log_his)-1]
    v_num = int(ver[3:])+1
    print v_num
#gold image case
else:
    v_num = 0

#update the log, with activities and new version num
with open("log.txt", "a") as log:
    log.write('\n')
    log.write(activities)
    log.write('\nver' + str(v_num))
