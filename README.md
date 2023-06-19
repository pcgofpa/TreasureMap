<h1>TreasureMap</h1>
 <p>
 This project was an exercise from a 100 Days of Code course that I bought to go through with my daughter.
 </p>
 <h3>Instructions</h3>
You are going to write a program that will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what the nested list looks like:

[['', '', ''],['', '', ''],['', '', '']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 

['', '', '']

['', '', '']

['', '', '']

Now it looks a bit more like the coordinates of a real map:

<img src="https://github.com/pcgofpa/TreasureMap/blob/main/Images/TreasureMap.png">

Your job is to write a program that allows you to mark a square on the map using a two-digit system. 

The first digit in the input will specify the column (the position on the horizontal axis).

The second digit in the input will specify the row number (the position on the vertical axis). 

So an input of 23 should place an X at the position shown below:
