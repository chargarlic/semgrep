def test_sanitized():
    x = input("Enter value: ")
    assert x.isdigit(), "Must be a number"
    # ok: taint-sanitizer-by-side-effect
    sink(x)

def test_unsanitized():
    x = input("Enter value: ")
    # ruleid: taint-sanitizer-by-side-effect
    sink(x)

def test_different_var_not_sanitized():
    x = input("Enter value: ")
    y = input("Enter another: ")
    assert x.isdigit()
    # ok: taint-sanitizer-by-side-effect
    sink(x)
    # ruleid: taint-sanitizer-by-side-effect
    sink(y)

def test_sanitized_used_twice():
    x = input("Enter value: ")
    assert x.isdigit()
    # ok: taint-sanitizer-by-side-effect
    sink(x)
    # ok: taint-sanitizer-by-side-effect
    sink(x)
