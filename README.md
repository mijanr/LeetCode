# LeetCode programming problems and solutions in Python
This repository contains my solutions to LeetCode problems in Python. I am using this repository to keep track of my progress and to share my solutions with others. Cool stuff, huh!

## How to test the solutions (doctest)
Doctest is a module that comes with Python. It allows you to test your code by running examples embedded in the documentation and verifying that they produce the expected results. It works by parsing the help text to find examples, running them, then comparing the output text against the expected value. 
For example, suppose you have a function called `factorial` that takes an integer and computes the factorial of that integer. You can write doctests for it like this:
```python
def factorial(n):
    """Computes factorial of n.

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
```

Most of the solutions in this repository have doctests integrated into them.

## Running inside Docker container
The repository contains a Dockerfile that can be used to run the repository inside a Docker container. `VSCode` Dev Container extension allows using a Docker container as a full-featured development environment. This means you can open any folder or repository inside a container and take advantage of Visual Studio Code’s full feature set. 

## Requirements
All the solutions should work with Python 3.8 or higher. I am using Python 3.11. If something changes, I will update this section.
