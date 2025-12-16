with open('Input.txt','r') as all_banks:
#with open('Test_input.txt','r') as all_banks:    
    banks = all_banks.readlines()
    # Read all the lines in the text file and assign each to a new object in a list

    for lines in enumerate(banks):
          line = lines[1].strip()
          banks[lines[0]] = line
    # Make a line variable for each line in banks and remove the new line character
    # Replace the object at index n that lines came from with line

    jolts = []
    
    for line in banks:
        nums = list(line)

        #digits = sorted(nums)[-2:]

        #print(f'Line 23 - {digits}')
        current_jolts = ''

        digits = sorted(nums)

        num_check = nums.index(digits[-1])
        
        if num_check == (len(nums)-1):

            num_check = nums.index(digits[-2])
        check_list = []
        for i in enumerate(nums):
             
            if i[0] <= num_check:
                continue
            else:
                check_list.append(nums[num_check] + i[1])
        check_list.sort()
        jolts.append(int(check_list[-1]))

    
    print(f'Output for part 1 is {sum(jolts)}')




# Expected test output is 357 for part 1
                  
