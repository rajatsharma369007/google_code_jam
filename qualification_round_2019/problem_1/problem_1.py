'''
command line arguments to this script:
first line takes the number of test cases and then, each line consists of one line
with an integer N.
for more info, watch the problem statement

'''

# function for checking whether '4' is present in the number or not.
def checkdigit(var):
    if '4' in str(var):
        return False
    else:
        return True

# taking the number of test cases
test_cases = int(input())

# for each test case
for i in range(1, test_cases+1):
    # each input number
    number = int(input())
    length = int(number/2)+1
    '''
    my concept:
    Take 2 numbers. From starting to half of the number, substracts one to copied
    number and add one to other number, and check whether both numbers contain 4
    or not. If do not contain, then just print those 2 numbers and exit().
    '''
    for j in range(1,length):
        var1 = number - j
        var2 = j
        # iterating for finding the 4 in the set of numbers
        if(checkdigit(var1) and checkdigit(var2)):
            print("Case #{}: {} {}".format(i, var1, var2))
            break

# necessary, otherwise shows "Time Limit Exceeded"
exit()