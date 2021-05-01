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


class DataPipelineGenerator:
    def __init__(self):
        file_name = 'techcrunch.csv'
        lines = (line for line in open(file_name))
        list_lines = (s.rstrip().split(",") for s in lines)
        col = next(list_lines)
        self.company_dict = (dict(zip(col, data)) for data in list_lines)

    def funding_raise(self):
        funding = (
            int(company_dict['raisedAmt'])
            for company_dict in self.company_dict
            if company_dict["round"] == "a"
        )
        return funding


if __name__ == "__main__":
    a = DataPipelineGenerator()
    col = sum(a.funding_raise())
    print('The funding for round a =', col)

# print(col)
"""To help you filter and perform operations on the data, you’ll create dictionaries where the keys 
are the column names from the CSV:"""

# company_dicts = (dict(zip(col, data)) for data in list_lines)
# print(next(company_dicts))

"""This generator expression iterates through the lists produced by list_line. Then, it uses zip() and dict() to 
create the dictionary as specified above. Now, you’ll use a fourth generator to filter the funding round you want and 
pull raisedAmt as well: """
# funding = (
#    int(company_dict['raisedAmt'])
#    for company_dict in company_dicts
#    if company_dict["round"] == "a"
# )
"""
In this code snippet, your generator expression iterates through the results of company_dicts and takes the raisedAmt for any company_dict where the round key is "a".

Remember, you aren’t iterating through all these at once in the generator expression. In fact, you aren’t iterating through anything until you actually use a for loop or a function that works on iterables, like sum(). In fact, call sum() now to iterate through the generators:

"""
# total_series_a = sum(funding)
# print('The Funding for Round a =', total_series_a)
