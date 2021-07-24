row1 = ["🚗","🚗","🚗"]
row2 = ["🚗","🚗","🚗"]
row3 = ["🚗","🚗","🚗"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
column = int(input("Enter the column number"))
row = int(input("Enter the row number"))
map[row][column] = "🚎"
print(f"{row1}\n{row2}\n{row3}")