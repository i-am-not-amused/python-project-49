
# brain-games

[![Actions Status](https://github.com/i-am-not-amused/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/i-am-not-amused/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/c76071a5f7eef7aed4ba/maintainability)](https://codeclimate.com/github/i-am-not-amused/python-project-49/maintainability)

A collection of small math games.

+ `brain-even` — determine, if number is odd.
+ `brain-calc` — check your skills with a series of simple arithmetic problems.
+ `brain-gcd` — find a general common denominator.
+ `brain-progression` — find missing number in arithmetic progression.
+ `brain-prime` — determine if number is prime.

Each game gives player 3 questions. If user answers them correctly, he wins and receives a personal congratulation. If answer for any question is incorrect, game finishes and considered to be lost.

## How to install

### Prerequisites

+ `make`
+ `python 3.10+`
+ `poetry ~=1.8`

### Installation

1. Install build dependencies
2. Clone the project and `cd` into it
3. Run `make package-install` to install games as a Python package. 

```bash
  git clone https://github.com/i-am-not-amused/python-project-49 brain-games
  cd brain-games
  make package-install
```
[![asciicast](https://asciinema.org/a/SVRqKdmzV7ps3C5XF8egXC427.svg)](https://asciinema.org/a/SVRqKdmzV7ps3C5XF8egXC427)

These commands create a new Python virtualenv, build the package and install it.
## Demos

### brain-games

Asks user for a name and greets them.

### brain-even

Generates a series of numbers, and user has to answer if they are odd or even.
If given number is even, user is expected to enter "yes", and "no" otherwise.

[![asciicast](https://asciinema.org/a/Cc6r44coHDbI5h7W4ZvlVtL6X.svg)](https://asciinema.org/a/Cc6r44coHDbI5h7W4ZvlVtL6X)

### brain-calc

User has to correctly answer a series of arithmetic problems.

[![asciicast](https://asciinema.org/a/4sqQ46HqwOwJCZqjw5X1W3zX7.svg)](https://asciinema.org/a/4sqQ46HqwOwJCZqjw5X1W3zX7)

### brain-gcd

Generates pairs of numbers, and user has to find Greatest Common Denominator for each pair.

[![asciicast](https://asciinema.org/a/xzyoaiTHXmIO5vmPwCwZV8PTv.svg)](https://asciinema.org/a/xzyoaiTHXmIO5vmPwCwZV8PTv)

### brain-progression

Generates different arithmetic progression with one element missing. User has to answer that number.

[![asciicast](https://asciinema.org/a/GejIDvfyXX4NzyQoratOYFyvD.svg)](https://asciinema.org/a/GejIDvfyXX4NzyQoratOYFyvD)

### brain-prime

Generates a series of numbers, and user has to answer if they are prime numberes.
If given number is a prime number, user is expected to enter "yes", and "no" otherwise.

[![asciicast](https://asciinema.org/a/hNlrAngjox7RzREOdFc0EEXjB.svg)](https://asciinema.org/a/hNlrAngjox7RzREOdFc0EEXjB)

