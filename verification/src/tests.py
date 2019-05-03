"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": (8, [1, 3, 5]),
            "answer": 2,
            "explanation": "Outer Leftopian shillings"
        },
        {
            "input": (12, [1, 4, 5]),
            "answer": 3,
            "explanation": "East Frombazian pesos"
        }
    ],
    "Extra": [
        {
            "input": (1, [3, 4, 5]),
            "answer": None,
            "explanation": "New Oldhemian dollars"
        },
        {
            "input": (4, [3, 5]),
            "answer": None,
            "explanation": "Democratic Turnlandian grommits"
        },
        {
            "input": (123456, [1, 6, 7, 456, 678]),
            "answer": 187,
            "explanation": "South Northcambrian pounds"
        }
    ]
}
