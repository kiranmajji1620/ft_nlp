import pytest

def write_to_file(data, file_path):
    with open(file_path, 'w') as f:
        f.write(data)

def read_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def test_write_and_read_from_file(tmp_path):
    # Define test data
    test_data = "Hello, world!"
    
    # Create a temporary file path within the temporary directory
    temp_file_path = tmp_path / "test_file.txt"
    
    # Call the function under test to write data to the temporary file
    write_to_file(test_data, temp_file_path)
    
    # Assert that the file was created in the temporary directory
    assert temp_file_path.exists()
    
    # Call the function under test to read data from the temporary file
    data_read = read_from_file(temp_file_path)
    
    # Assert that the data read from the file matches the test data
    assert data_read == test_data