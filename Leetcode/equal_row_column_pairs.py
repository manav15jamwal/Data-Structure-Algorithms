# # LeetCode 2352 — Equal Row and Column Pairs
# Goal : To find number of equal rows and columns in a matrix
# Approach : Use hashmap to count the frequency of rows and columns 

def equal_row_column(matrix):
    rows,columns = {},{}
    answer = 0
    for row in matrix:
         row = tuple(row)
         rows[row]= rows.get(row,0)+1 
    for column in range(len(matrix[0])):
         column =tuple(matrix[row][column] for row in range(len(matrix)))
         columns[column] = columns.get(column,0)+1
         answer += rows.get(column,0)
    return answer

print(equal_row_column(matrix = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 8, 9]
]))
         
