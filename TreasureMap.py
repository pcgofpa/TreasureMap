# Don't Change the code below
row1 = ["","",""]
row2 = ["","",""]
row3 = ["","",""]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#Write code below this row
horizon_pos = int(position[0]) # Column
horizontal_position = horizon_pos - 1
vert_pos = int(position[1]) # Row
vert_pos_offset = vert_pos - 1

selected_row = map[vert_pos_offset]
selected_row[horizontal_position] = "X"

#Don't Change the code below
print(f"{row1}\n{row2}\n{row3}")