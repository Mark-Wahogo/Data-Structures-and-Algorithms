def count_rotations(nums):
    pass
nums =[3] #[3, 4, 5, 7, 9, 1]
Output = 0
result = count_rotations(nums)
result == Output

test = {
    'input':{
        'nums': [3]#[3, 4, 5, 7, 9, 1]
    },
    'Output': 0
}

def count_rotations(nums):

    position =  0
    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position
        position +=1
    return 0

result =count_rotations(test['input']['nums'])

print("The Expected number of rotations is: ", Output)
print("The number of rotations is: ", result)   
print("The Expected number of Rotations is equivalent to the obtained number of rotations: ", result == Output) 