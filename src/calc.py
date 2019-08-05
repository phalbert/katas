def check_string(string):
    """determine if exactly 3 question marks exist between every pair of numbers that add up to 10"""
    if not isinstance(string, str):
       raise TypeError('Parameter must be a string')
   
    words = partition(string)
    print(words)

    count = 0
    for word in words:     
        sum_of_numbers = get_sum(word)
        if sum_of_numbers != 10:
            count += 1
        if sum_of_numbers == 10 and not check_condition(word):#only check if sum is 10
            return False          
    
    if count == len(words): #no sum=10 found
        return False
 
    return True

def partition(string):
    count = 0
    indexes = []
    lists, index_lists = [], []


    for char in string:
        if char.isdigit():
            indexes.append(count)
            
        count+= 1
    
    print(indexes)

    i = 0
    while i < len(indexes):
        start = indexes[i]
        try:
            end = indexes[i + 1]
        except:
            end = 0
            
        m_list = [start, end]
        index_lists.append(m_list)

        start = end
        i += 1
   
    # index_lists = [indexes[i:i+2] for i  in range(0, len(indexes), 2)]

    for a_list in index_lists:
        first = a_list[0]
        try:
           second = a_list[1] + 1
        except:
           second = 0

        if (len(string) < second) or (second == 0):
            word = string[first:]
        else:
            word = string[first:second]
        lists.append(word)

    return lists
    
def get_sum(string):
    try:
        last_index = (len(string) - 1)
        sum_of_numbers = int(string[0]) + int(string[last_index])

        print('Sum', sum_of_numbers)
        return sum_of_numbers
    except:
        return 0


def check_condition(string):
    print('Word',string)
    last_index = (len(string) - 1)
    count = 0

    for char in string[1:last_index]:
        if char == '?':
            count += 1
    
    print('Count',count)

    if count == 3:
        return True
    else:
        return False

