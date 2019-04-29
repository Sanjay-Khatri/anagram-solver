from itertools import permutations
from multiprocessing import Process, Pool, cpu_count
import time


def foo(swords,start):
    with open("C:\words.txt") as reader:
        wordlist = reader.read().split()
        for sword in swords:
            if sword in wordlist:
                print("RESULT:\t"+sword)
                # timenow= time.time()
                # print("TIME IN SEARCH:" + str(timenow - start))

    # endtime = time.time()
    # print("EXECUTION TIME:" + str(endtime - start))


def Main():


    while True:
        start = time.time()
        given = input("STRING?\n")

        processor_cores = cpu_count()
        # print(processor_cores)

        s = [''.join(p) for p in permutations(given)]
        t_list = round(len(s)/processor_cores)
        # print("total words per list: {}" .format(t_list))
        wordlist_record =[]
        # print("total permutation: {}".format(len(s)))
        # print(len(s)/4)
        # print(math.ceil(len(s)/4))
        next=t_list
        prev=0
        for i in range(0, processor_cores):
            listname = "mylist"+str(i)
            listname = list()
            wordlist_record.append(listname)

            try:
                for word_count in range(prev, next):
                    listname.append(s[word_count])
            except:
                pass

            prev = next
            next = next + t_list

        process_list = []
        for process in range(0, processor_cores):
            if wordlist_record[process]:
                process_name = "process" + str(process)
                process_name = Process(target=foo, args=(wordlist_record[process], start))
                process_list.append(process_name)
                process_name.start()


        for proc in process_list:
            proc.join()

if __name__ == '__main__':
    Main()