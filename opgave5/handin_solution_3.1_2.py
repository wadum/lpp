with open("experimentalResults.txt") as f:

    list_of_lists = []

    # Read file as a list of lines and iterate over it
    for line in f.readlines():

        # Create empty field list for numeric values
        field_list_num = []

        # Translate string values to floats
        for element in line.split():
            field_list_num.append(float(element))

        # Add field_list_num to outer list
        list_of_lists.append(field_list_num)