"""
Generic function to read any CSV file and return contents of CSV file 
in form of list of dictionary 

"""

def parse_headers(header_line):
    """
    Takes a line as input and returns a list of column headers.
    """
    return header_line.strip().split(',')

def parse_values(data_line):
    """
    Takes a line containing data from CSV and returns a list of floating-point numbers.
    """
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            values.append(float(item))
    return values

def create_item_dict(values, headers):
    """
    Takes a list of values and a list of headers as inputs and 
    returns a dictionary with the values associated with their respective headers as keys.
    
    Arguments:
        values - Data line from CSV file
        headers - Data line from CSV file with headers, i.e. 0th line in CSV
    """
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result

def read_csv(path):
    """Reads any CSV file.
    
    Arguments:
        path - CSV file path
    """
    result = []
    # Open the file in read mode
    with open(path, 'r') as f:
        # Get a list of lines
        lines = f.readlines()
        # Parse the header
        headers = parse_headers(lines[0])
        # Loop over the remaining lines
        for data_line in lines[1:]:
            # Parse the values
            values = parse_values(data_line)
            # Create a dictionary using values & headers
            item_dict = create_item_dict(values, headers)
            # Add the dictionary to the result
            result.append(item_dict)
    return result
