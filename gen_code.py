import os
import base64


def get_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


with open(get_file("test_cases.py"), "rb") as file:
    with open(get_file("load.py"), "w") as f:
        f.write(
            f'exec(__import__("base64").b64decode({base64.b64encode(file.read())}))'
        )
        f.write("\n\n\n")
        f.write(
            """#Edit the arguments for each question
def solution():
    #Your code goes here
    pass

test(interactive_debug(), x)
"""
        )
