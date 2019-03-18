def combiner(items):
    #argument for the def

    string = []
    num = 0
    #initial definition

    for i in items:
        if isinstance(i, (int, float)):
        #use isinstance

            num += i
            #increment
        else:
        
            string.append(i)
            #append()

    string.append(str(num))
    #append(), str()

    final_answer = "".join(string)
    #join()

    return final_answer
    # indent of return
