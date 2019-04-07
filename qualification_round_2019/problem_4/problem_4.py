'''
command line arguments to this script:
first line takes the number of test cases, in format given in the sample code
second line reads the N, B, F value in the format provided, where N: number of 
workers, B: number of broken workers, and F: number of lines you may send to 
the master computer
'''

# number of test cases
test_case = readline_int()

# Number of workers, number of broken workers, and numbers of line you can send
N, B, F = readline_int_list()

# Initializing the n bit data with zeros (list)
check_list = ['0'] * N
# converting it to string of n bit data
check_str = ''.join(check_list)

'''
my concept:
I will send n bit data with 1 at 0th index and rest all zeros if I got 1 in
in returned data that means 0th index worker is working fine and shift this 1
to next index and check again. Repeat this till nth bit. At the end you will 
get a list of index of broken workers.
'''
broken_worker_index = []
for i in range(F):
    # putting one at ith index of n bit data
    check_str1 = check_str[:i] + '1' + check_str[i + 1:]
    printline check_str1 to stdout
    
    flush stdout
    # reading response from master computer
    response = readline_str()
    # '1' is not in response string, put the index in list
    if '1' not in response:
        broken_worker_index.append(i)
    
# sorting the index
index.sort()
# creating a string of index with space separated
string = ' '.join(index)
printline string to stdout

exit()
