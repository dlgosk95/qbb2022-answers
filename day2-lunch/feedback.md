# Feedback day2-lunch

You've got a good start on adapting the bed parser, but there are several more steps you need to take

- You need to check that there are at least 3 fields per bed line
- You don't handle the complex fields at all. The itemRGB, blockSizes, and blockStarts fields need to be split and each entry needs to be converted in an int. You also need to make sure that the length of blockStarts and blockSizes equals the number in blockCount
- I assume that it was done for debugging, but uncommenting the `try` statement will be important. Right now your script will crash if it tries to convert a field into a data type that it can't.
- You need a way to keep track of the number of bad lines and not include them in the bed list

I'm guessing that you are (or perhaps were?) not very comfortable with python when you wrote this. Please ask a TA or instructor for help if you are still not comfortable completing this assignment as these particular concepts will get used again and again in the lab course. You can definitely do this. Keep it up!