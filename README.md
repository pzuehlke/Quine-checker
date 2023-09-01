# Python quine checker

This repository consists mainly of two Python scripts. The first is a
self-replicating program, often termed a _quine_, in honor of the American
logician W. Quine (1908-2000). The second is a module for checking whether
a given Python script is a quine.

## Description of the quine

The `quine.py` script prints its own source code when executed and returns
`None`. It consists of the composition of two functions, called `g` and `f`.

The function `g` accepts an arbitrary string `w` as an argument and performs the
following steps:
  1. Prints the definition of another function, having no parameters, that
     returns `w` when called. (Explicitly, the latter is just `lambda: w`.)
  2. Prints the string `w`.
  3. Prints the string `"g(f())"`.

In turn, the function `f` is a particular case of the function described in
step 1 where `w` is taken to be the full definition of `g`. Thus, `f` is a
function of no parameters which simply returns the source code of `g` as a string.

When the call `g(f())` is run, `f` provides the source code of `g` as the
argument of `g`, which triggers the printing of the definitions of `f` and `g`,
along with with the expression `"g(f())"`, which collectively make up the
script's own source code.

## Description of the quine checker

The `quine_checker.py` module contains utility functions for reading the contents
of another script, capturing its output, comparing the two, and finally reporting
whether that script is a quine.

The program `run_quine_check` simply calls `quine_checker` on the candidate
whose filename is provided as its argument.

## Usage

Place the Python script you want to check, say, `quine_candidate.py`, in the
directory where the files in the repository are stored.  Then run the
the following command in the terminal:
```
python3 run_quine_check.py quine_candidate.py
```
This will output a report on whether the script is a quine, along with other
relevant information.

## Contributions

Contributions are welcome. Please feel free to submit a pull request.