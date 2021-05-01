# Creating Data Pipelines With Generators
"""
Data pipelines allow you to string together code to process large datasets or streams of data without maxing out your
 machine’s memory.
 Imagine that you have a large CSV file:

This example is pulled from the TechCrunch Continental USA set, which describes funding rounds and dollar amounts for
various startups based in the USA. Click the link below to download the dataset:

It’s time to do some processing in Python! To demonstrate how to build pipelines with generators, you’re going to
analyze this file to get the total and average of all series A rounds in the dataset.

Let’s think of a strategy:

1. Read every line of the file.
2. Split each line into a list of values.
3. Extract the column names.
4. Use the column names and lists to create a dictionary.
5. Filter out the rounds you aren’t interested in.
6. Calculate the total and average values for the rounds you are interested in.
Normally, you can do this with a package like pandas, but you can also achieve this functionality with just a few
generators.
You’ll start by reading each line from the file with a generator expression:
"""

file_name = 'techcrunch.csv'
lines = (line for line in open(file_name))
list_lines = (s.rstrip().split(",") for s in lines)
col = next(list_lines)
#print(col)
"""To help you filter and perform operations on the data, you’ll create dictionaries where the keys 
are the column names from the CSV:"""

company_dicts = (dict(zip(col, data)) for data in list_lines)
print(next(company_dicts))
