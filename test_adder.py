import pytest
import os
from adder import add, process_data

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -4) == -5

def test_add_mixed_numbers():
    assert add(5, -2) == 3

def test_add_zero():
    assert add(0, 7) == 7

def test_process_data_positive_numbers(tmpdir):  # Use tmpdir for temporary files
    input_file = tmpdir.join("input.txt")
    output_file = tmpdir.join("output.txt")
    input_file.write("7,2")  # Write to temporary file
    process_data(str(input_file), str(output_file))
    with open(str(output_file), 'r') as f:
        result = f.readline().strip()
    assert result == "9"

def test_process_data_invalid_input(tmpdir):
     input_file = tmpdir.join("input.txt")
     output_file = tmpdir.join("output.txt")
     input_file.write("a,b")
     process_data(str(input_file), str(output_file))
     # Check that process data is silent and doesn't raise an exception.
     # In a production environment, you might want to assert that a log file or
     #  a database has been updated with the error message.
     assert True

def test_process_data_file_not_found(tmpdir):
    output_file = tmpdir.join("output.txt")
    process_data("nonexistent_file.txt", str(output_file))
    # Check that process data is silent and doesn't raise an exception.
    # In a production environment, you might want to assert that a log file or
    #  a database has been updated with the error message.
    assert True