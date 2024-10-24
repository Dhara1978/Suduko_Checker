def create_sudoku_lists(input_data):
    
    #create lists to check rows, columns and boxes
    row_lists = []
    column_lists = []
    box_lists = []
    return_list = []
    
    #create lists of row numbers
    for i in range(9):
        row_list = list(input_data[i][0])
        row_lists.append(row_list)
    
    #create lists of columns 
    for i in range(9):
        check_columns = []
        for j in range(9):
            check_columns.append(row_lists[j][i])
        column_lists.append(check_columns)
    
    #create lists of boxes
    box_1 = []
    box_2 = []
    box_3 = []
    box_4 = []
    box_5 = []
    box_6 = []
    box_7 = []
    box_8 = []
    box_9 = []
    for i in range(3):
        for j in range(9):
            if j < 3:
                #print(i, j)
                box_1.append(row_lists[i][j])
            elif j < 6:
                box_2.append(row_lists[i][j])
            elif j < 9:
                box_3.append(row_lists[i][j])  
    box_lists.append(box_1)
    box_lists.append(box_2)
    box_lists.append(box_3)
    for k in range(3, 6):
        for l in range(9):
            if l < 3:
                box_4.append(row_lists[k][l])
            elif l < 6:
                box_5.append(row_lists[k][l])
            elif l < 9:
                box_6.append(row_lists[k][l])
    box_lists.append(box_4)
    box_lists.append(box_5)
    box_lists.append(box_6)
    for m in range(6, 9):
        for n in range(9):
            if n < 3:
                box_7.append(row_lists[m][n])
            elif n < 6:
                box_8.append(row_lists[m][n])
            elif n < 9:
                box_9.append(row_lists[m][n])
    box_lists.append(box_7)
    box_lists.append(box_8)
    box_lists.append(box_9)
    
    return_list.append(row_lists)
    return_list.append(column_lists)
    return_list.append(box_lists)
    
    return return_list
        
    
def sudoku_checker(input_data):
    check_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    results_list = []
    all_lists = create_sudoku_lists(input_data)
    for i in range(3):
        for j in range(9):
            all_lists[i][j].sort()
            if all_lists[i][j] == check_list:
                results_list.append('Yes')
            else:
                results_list.append('No')
    
    if 'No' in results_list:
        print('No')
    else:
        print('Yes')
            

input_data_1 = [['295743861'], ['431865927'], ['876192543'], ['387459216'], ['612387495'], ['549216738'], ['763524189'], ['928671354'], ['154938672']]
input_data_2 = [['195743862'], ['431865927'], ['876192543'], ['387459216'], ['612387495'], ['549216738'], ['763524189'], ['928671354'], ['254938671']]

sudoku_checker(input_data_1)
sudoku_checker(input_data_2)
