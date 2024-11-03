# import os

# Path = os.getcwd()
# infor = os.environ

# courses = {"LLM Concepts": "AI",
#            "Introduction to Data Pipelines": "Data Engineering",
#            "AI Ethics": "AI",
#            "Introduction to dbt": "Data Engineering",
#            "Writing Efficient Python Code": "Programming",
#            "Introduction to Docker": "Programming"}

# for key, value in courses.items():

#     # Check if the value is "AI"
#     if value == "AI":
#         print(key, "is an AI course")

#     # Check if the value is "Programming"
#     elif value == "Programming":
#         print(key, "is a Programming course")

#     # Otherwise, print that it is a "Data Engineering" course
#     else:
#         print(key, "is a Data Engineering course")

# Define a function called concat
# def concat(*args):

#     # Create an empty string
#     result = ""

#     # Iterate over the Python args tuple
#     for arg in args:
#         result += " " + arg
#     return result


# # Call the function
# print(concat("Python", "is", "great!"))


# Define a function called concat
def concat(**kwargs):

    # Create an empty string
    result = ""

    # Iterate over the Python kwargs
    for kwarg in kwargs:
        result += " " + kwarg
    return result


# Call the function
print(concat(start="Python", middle="is", end="great!"))
