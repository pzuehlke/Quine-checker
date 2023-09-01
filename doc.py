# This Python script is a self-replicating program, often termed a _quine_,
# in honor of the American logician W. Quine (1908-2000).

# The script prints its own source code when executed and returns `None`. It
# consists of the composition of two functions, called g and f.

# The function g accepts an arbitrary string w as an argument and performs the
# following steps:
#   1. Prints the definition of another function, having no parameters, that
#      returns w when called. (Explicitly, the latter is just `lambda: w`.)
#   2. Prints the string w.
#   3. Prints the string "g(f())".

# In turn, the function f is a particular case of the function described in
# step 1 where w is taken to be the full definition of g. Thus, f is a function
# of no parameters which simply returns the source code of g as a string.

# When the call g(f()) is run, f provides the source code of g as the argument
# of g, which triggers the printing of the definitions of f and g, along with
# with the expression "g(f())", which collectively make up the script's own
# source code.
