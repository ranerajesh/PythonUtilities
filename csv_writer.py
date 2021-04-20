def write_csv(items, path):
  """
  Takes a list of dictionaries and writes it to a file in CSV format. 
  Include the column headers in the first line.
  """
    # Open the file in write mode
    with open(path, 'w') as f:
        # Return if there's nothing to write
        if len(items) == 0:
            return
        
        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')
        
        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")
