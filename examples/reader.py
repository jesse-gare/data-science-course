file_name = 'EOD-KO.csv'
in_file = open(file_name, 'r')
headers = in_file.readline()
data = [dict(zip(headers.split(','),line.split(','))) for line in in_file]
print(data[0]['Open'])
