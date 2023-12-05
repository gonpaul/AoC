import puzzle1

count_floor = puzzle1.count_floor
def test_floor_count():
    # Test Case 1: Balanced parentheses
    assert count_floor("((()))") == 0

    # Test Case 2: More opening parentheses
    assert count_floor("((((") == 4

    # Test Case 3: More closing parentheses
    assert count_floor(")))") == -3

    # Test Case 4: Empty string
    assert count_floor("") == 0

    # Test Case 5: Mix of opening and closing parentheses
    assert count_floor("()(()())") == 0

    assert count_floor('((((())') == 3

    print("All tests passed!")



# Run the tests
test_floor_count()
