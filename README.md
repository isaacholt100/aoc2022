Solutions for [Advent of Code 2022](https://adventofcode.com/2022).

Each file in the `src/solutions` folder exports three items:
1. A `part1_solution` function which gives the correct answer for the given puzzle input.
2. A `part2_solution` function which gives the correct answer for the given puzzle input.
3. A `tests` dictionary for testing the previous two functions against given test cases.

To print the answers for a given day, run the `src/main.py` file:

```shell
$ python src/main.py
```

and enter the day as a two-digit number. This automatically runs the tests from the `tests` dictionary in that day's solution file, as mentioned above.