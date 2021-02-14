#
# Basic example:
# - Stores multiple types on Redis and
# get them back.
#

from redis_pal import RedisPal


def example():

    rp = RedisPal()
    key = "test"

    # Integers
    inp = 1
    rp.set(key, inp)
    ans = rp.get(key)
    print("Inp is {} of type {}, ans is {} of type {}".format(
        inp, type(inp), ans, type(ans)))

    # Floating points
    inp = 1.23
    rp.set(key, inp)
    ans = rp.get(key)
    print("Inp is {} of type {}, ans is {} of type {}".format(
        inp, type(inp), ans, type(ans)))

    # Strings
    inp = "Test"
    rp.set(key, inp)
    ans = rp.get(key)
    print("Inp is {} of type {}, ans is {} of type {}".format(
        inp, type(inp), ans, type(ans)))

    # Functions
    def echo(arg):
        return arg
    inp = echo
    rp.set(key, inp)
    ans = rp.get(key)
    print("Inp is {} of type {}, ans is {} of type {}".format(
        inp, type(inp), ans, type(ans)))

    # Numpy arrays
    import numpy as np
    inp = np.array([0, 1, 2, 3, 4])
    rp.set(key, inp)
    ans = rp.get(key)
    print("Inp is {} of type {}, ans is {} of type {}".format(
        inp, type(inp), ans, type(ans)))


if __name__ == "__main__":
    example()
