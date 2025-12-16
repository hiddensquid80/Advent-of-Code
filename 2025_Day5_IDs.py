with open('Input.txt','r') as id_list:
    
    cleaned_ids = id_list.readlines()

    cleaned_ids = [i.strip('\n') for i in cleaned_ids]

    ### PART 1

    ranges = []
    checks = []
    count = 0
    for i in cleaned_ids:

        if '-' in i:

            new_range = i.split('-')
            
            ranges.append(new_range)
        elif i == '':
            pass

        else:
            checks.append(i)
    
    for tested_id in checks:
        
        
        for range_test in ranges:

            if int(tested_id) in range(int(range_test[0]),int(range_test[1])+1):
                count += 1
                break
    

    ### PART 2

    total_valid = [0]

    ranges_to_test = []

    for i in cleaned_ids:

        if '-' in i:

            lower, upper = i.split('-')

            ranges_to_test.append([int(lower),int(upper)])
        else:
            pass

    ranges_to_test.sort(key=lambda x: x[0])
    
    current_low, current_high = ranges_to_test[0]
    
    for i in ranges_to_test[1:]:

        if current_high +1 <= i[0]:
        # if the current highest bound is less than the lower bound of the next 
        # lowest bound, set the new lowest and highest bound to the new tuple and append
        # the old one to the list
            total_valid.append([current_low,current_high])
            current_low, current_high = i
            continue
        elif current_high + 1 <= i[1]:
        # if the current highest bound is less than the upper bound of the new range
        # set the current highest bound to the upper bound of the new range
            current_high = i[1]
        
    total_valid.append([current_low,current_high])
    
    for a_range in total_valid[1:]:

        total_valid[0] += (a_range[1] - a_range[0] + 1)
    print(f'The count of valid IDs is {count}')
    print(f'The total possible valid IDs is {total_valid[0]}')

    # Expected output is 
    # 345755049374932
    # 321734886414263 was the output before current_high + 1 <= was implemented 
    # thanks to chatgpt