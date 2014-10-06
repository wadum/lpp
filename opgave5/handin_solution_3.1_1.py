with open("experimentalResults.txt") as f:

    list_of_lists = []

    for line in f.readlines():

        field_list_num = []

        for element in line.split():
            field_list_num.append(float(element))

        list_of_lists.append(field_list_num)