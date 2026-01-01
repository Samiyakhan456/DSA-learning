shelf = [10,20,30,40]
left_index = 0
right_index = -1

while left_index < len(shelf)/2:
    temp = shelf[left_index]
    shelf[left_index] = shelf[right_index]
    shelf[right_index] = temp
    left_index = left_index+1
    right_index = right_index-1

print(shelf)