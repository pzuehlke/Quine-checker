f = lambda: """def g(w):
    lambda_part = "f = lambda: "
    triple_quotes = "000".replace('0', '"')
    print(lambda_part + triple_quotes + w + triple_quotes)
    print(w)
    print("g(f())")"""
def g(w):
    lambda_part = "f = lambda: "
    triple_quotes = "000".replace('0', '"')
    print(lambda_part + triple_quotes + w + triple_quotes)
    print(w)
    print("g(f())")
g(f())
