def locate_cards(cards, query):
  pass
# coming up with some example inputs and outputs. Trying to cover all edge cases
cards = [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
query = 6
output = 2
result = locate_cards(cards, query)
print(result)
result == output
test = {
     'input' : {
        'cards' : [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query' : 6
    },
    'output' : 2
}
locate_cards(**test['input']) == test['output']
tests = []

# query occurs in the middle
tests.append(test)

tests.append({
    'input':{
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

#query is the first element
tests.append({
    'input' : {
        'cards' : [4, 2, 1, -1],
        'query' : 4
    },
    'output' : 0
})

#cards contains just one element, query
tests.append({
    'input' : {
        'cards' : [6],
        'query' : 6
    },
    'output' : 0
})

# Cards does not contain query
tests.append({
    'input' : {
        'cards' : [9, 7, 5, 2, -9],
        'query' : 4
    },
    'output' : -1
})

# Cards is empty
tests.append({
    'input' : {
        'cards' : [],
        'query' : 7
    },
    'output' : -1
})

# numbers can repeat in cards
tests.append({
    'input' : {
        'cards' : [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query' : 3
    },
    'output' : 7
})

# query occurs multiple times
tests.append({
    'input' : {
        'cards' : [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query' : 6
    },
    'output' : 2
})

def locate_card(cards, query):

    #create a variable position with the value 0
    position = 0
    
    #set up a loop for repetition
    while True:

        #check if element at the current position match the query
        if cards[position] == query:

            #Answer found! return and exit..
            return position
        
        #Increment the position
        position += 1

        #Check if we have reached the end of the array
        if position == len(cards):

            #Number not found, return -1
            return -1


# Below Function is used to reduce the amount of time taken to search for a Number.
#  The Function used is Binary Search

def locate_card(cards, query):
    lo, hi = 0, len(cards) -1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]

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

def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid: ", mid, "Mid_number: ", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'    
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        print("lo: ", lo, "hi: ", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid  
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1                  

result = locate_card(test['input']['cards'], test['input']['query'])
print("The expected result is: ", output)
print("Result is: " , result)

print(" The Result matched the expected Result: ", result == output)     