#print content of global list at two places
# 1} inside process 2}inside main program
from multiprocessing import Process
result =[]
def sq_list(mylist):
    global result
    for i in mylist:
        result.append(i**2)
    #print global list result
    print("result (in process p1):{}".format(result))

if __name__=="__main__":
    mylist=[2,3,4,5]

    #creating new process
    p1 = Process(target=sq_list, args = (mylist,))
    p1.start()
    p1.join()
    #print global result list
    print("result(in main program):{}".format(result))

 ##output=>result (in process p1):[4, 9, 16, 25]
##          result(in main program):[]
