last_pos = None
num_list = [10, 5, 5]
index = 0

for a in range(sum(num_list)):
    x_pos = a // 6
    y_pos = a % 6
    print(f"({x_pos}, {y_pos})")
    
    if a == sum(num_list[:index+1])-1:
        print("Next Array Value", index)
        index += 1
        
