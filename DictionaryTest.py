def locate_Consumption (Consumption, query):
    pass
Consumption = [2500, 2000,1800,  1700, 1500, 1400, 1000]
query = 2000
Output = 1
result = locate_Consumption(Consumption, query)
print(result)
result == Output

test = {
     'input' : {
        'Consumption' :[2500, 2000,1800,  1700, 1500, 1400, 1000],
        'query' : 2000
    },
    'output' : 1
}
locate_Consumption(**test['input']) == test['output']

def locate_Consumption(Consumption, query):

    #create a variable position with the value 0
    position = 0
    
    #set up a loop for repetition
    while True:

        #check if element at the current position match the query
        if Consumption[position] == query:

            #Answer found! return and exit..
            return position
        
        #Increment the position
        position += 1

        #Check if we have reached the end of the array
        if position == len(Consumption):

            #Number not found, return -1
            return -1


# Below Function is used to reduce the amount of time taken to search for a Number.
#  The Function used is Binary Search

def locate_Consumption(Consumption, query):
    lo, hi = 0, len(Consumption) -1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = Consumption[mid]

        print("lo: ", lo, "hi: ", hi, "mid: ", mid, "mid_number: ", mid_number)

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1
    return -1     

# Below function is used to correct the case for the list like [8,8,6,6,6,2,2,2,0,0,], 
# to make sure that the first instance of 6 is recognized instead of the last instance of 6

def test_location(Consumption, query, mid):
    mid_number = Consumption[mid]
    print("mid: ", mid, "Mid_number: ", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and Consumption[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'    
def locate_Consumption(Consumption, query):
    lo, hi = 0, len(Consumption) - 1

    while lo <= hi:
        print("lo: ", lo, "hi: ", hi)
        mid = (lo + hi) // 2
        result = test_location(Consumption, query, mid)

        if result == 'found':
            return mid  
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1                  

result = locate_Consumption(test['input']['Consumption'], test['input']['query'])
print("The expected result is: ", Output)
print("The result is: " , result)

print(" The Result matched the expected Result: ", result == Output) 