# /Users/jsoto2/Documents/Udacity_DAND/02_Intro_to_Python/some_file.txt

f = open('/Users/jsoto2/Documents/Udacity_DAND/02_Intro_to_Python/some_file.txt', 'r')
file_data = f.read()
f.close()

print(file_data)

f = open('/Users/jsoto2/Documents/Udacity_DAND/02_Intro_to_Python/some_file.txt', 'w')
f.write("Hello there again!")
f.close()

print(file_data)
