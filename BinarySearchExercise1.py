def locate_cards(cards, query):
  pass
# coming up with some example inputs and outputs. Trying to cover all edge cases
cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3
result = locate_cards(cards, query)
print(result)
result == output
test = {
    'input':{
       'cards' : [4, 2, 1, -1],
        'query' : 4
    },
    'output' : 0
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
test
result = locate_card(test['input']['cards'], test['input']['query'])
print("The expected result is: ", output)
print("Result is: " , result)

print(" The Result matched the expected Result: ", result == output)     
