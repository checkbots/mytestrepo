"""Sekhar: This module has simple no boiler plate test cases for
   timeobject module. You can run these tests with py.test"""

from timeobject import Time, int_to_time


# Test time_to_int and int_to_time
def test_time_to_int():
    i1 = 5000
    t = int_to_time(i1)
    i2 = t.time_to_int()
    assert i1 == i2


# Check adding two times.
def test_add_time():
    start = Time(9, 45)
    duration = Time(1, 35)
    end = start + duration
    assert end == Time(11, 20)


# Check adding a time and an integer
def test_add_time_and_int():
    start = Time(9, 45)
    duration = 100
    end = start + duration
    print "Deliberate failure to demonstrate failed test reporting.."
    assert end == Time(11, 15)


# Check valid_time method with different input
def test_valid_time():
    valid = ((8, 45, 20), (12, 3, 55), (15, 5, 0), (1, 0, 0))
    invalid = ((8, 45, 60), (9, 61, 0), (10, -1, 5), (-10, 1, 1))

    for ttuple in valid:
        t = Time(*ttuple)
        assert t.valid_time()

    for ttuple in invalid:
        t = Time(*ttuple)
        assert not t.valid_time()
