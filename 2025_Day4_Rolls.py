with open('test_input.txt','r') as f:
    input_list = list(f.readlines())
    
    stri_list = [s.strip() for s in input_list]


    def test_input():
        for i in enumerate(stri_list):
        # (index, value)
        

            for value in enumerate(i[1]):
        
                count = 0
                try:
                    if (value[0]+1) or (value[0]-1) == '@':

                        count += 1
                    #repeat this 7 more times

                    elif (value[0]-1) == '@':
                        count += 1

                except:
                    pass
                print(count)
                if count <= 4:

                    return True
    
    

    #print(stri_list)