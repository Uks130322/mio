import mio

mio.capture_output(file='myfile.txt')
print('checking output text\nhello world!')
mio.restore_output()
print('from file:\n')
mio.print_file(file='myfile.txt')
