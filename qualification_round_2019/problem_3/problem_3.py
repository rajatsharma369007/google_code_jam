'''
command line arguments to this script:
first line takes the number of test cases and then each test case contains 2 lines,
first line 2 numbers: N (use prime numbers less than N) and L (length of the list
of values of cyphertext), second line contains the list of values of cyphertext.
for more info, watch the problem statement

'''

# function for creating the list of prime numbers less N
def list_of_prime(N):
    prime_numbers = []
    for num in range(2, N+1):
        prime = True
        # checking for number other than 2 or itself
        for i in range(2, num):
            if (num%i == 0):
                prime = False
        if prime:
           prime_numbers.append(num)
    # prime number list, length of list
    return prime_numbers

# counting the number of same elements present in the list
def countX(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count 

# removing the duplicates in the list
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

# taking the number of test cases
test_case = int(input())

# for each test case
for q in range(test_case):
    # N: threshold for prime numbers list
    # L: number of cyphertext
    inputs = input()
    N, L = inputs.split(' ')
    N, L = int(N), int(L)
    
    # list of cyphertext values, read in string format
    cypher_code_str = input()
    cypher_code_str_list = cypher_code_str.split(' ')
    
    # converting the values in integers 
    cypher_code_list = []
    for j in range(L):
        cypher_code_list.append(int(cypher_code_str_list[j]))
        
    # creating list of prime numbers
    list_prime = list_of_prime(N)
    
    # creating the decrypt list of prime numbers from cyphertext code list
    container = []
    # for each value in cypher_code_list
    for number in cypher_code_list:
        count = 0
        # retreiving the factors of cypher code value
        for k in range(len(list_prime)):
            if (number%list_prime[k]) == 0:
                container.append(list_prime[k])
                count += 1
            elif count == 2:
                # when received the 2 prime numbers
                break
    
    # removing the common factors 
    decrypt = []
    for i in range(0,len(container)-1,4):
        if container[i] not in container[i+2:i+4]:
            decrypt.append(container[i])
            decrypt.append(container[i+1])
        else:
            decrypt.append(container[i+1])
            decrypt.append(container[i])
        
    
    # creating the mapping of character with prime number
    # taking copy of decrypt prime numbers 
    mapping_prime_list = decrypt.copy()
    # removing repeated prime numbers
    mapping_prime_list = Remove(mapping_prime_list)
    # sorting them in ascending order
    mapping_prime_list.sort()

    # creating list of alphabets
    mapping_alphabet_list = []
    # using ASCII value
    for letter in range(97,123):
        mapping_alphabet_list.append(chr(letter))
    
    # creating a dictionary for mapped values
    mapping = dict(zip(mapping_prime_list[::-1], mapping_alphabet_list[::-1]))
    
    # saving result as list
    result = []
    for i in range(L+1):
        result.append(mapping[decrypt[i]].upper())
        
    print('Case #{}: {}'.format(q+1, ''.join(result)))
        
exit()