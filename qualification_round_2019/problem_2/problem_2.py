'''
command line arguments to this script:
first line takes the number of test cases and then in each test case, first line
will be the size of the maze and the second line will be the string containing
2N - 2 characters showing the direction of the motion either S or E. 
for more info, watch the problem statement

'''

# taking the number of test cases
test_case = int(input())

# for each test case
for i in range(1, test_case+1):
    # size of maze
    maze_size = int(input())
    # direction of Lydia's path
    given_path = input()
    # empty list for storing our path info.
    our_path = []
    '''
    my concept:
    for each direction of Lydia, we will move exactly opposite direction
    '''
    for j in range(2*(maze_size)-2):
        if given_path[j] == 'S':
            our_path.append('E')
        elif given_path[j] == 'E':
            our_path.append('S')
        
    print('Case #{}: {}'.format(i,''.join(our_path)))