input = open("stol.txt", 'r')

dictionary = {
    'Name': [],
    'Year': [],
    'Source': [],
    'Orig.': [],
    'Method': [],
    'Reference': []
    }

while 1:
	line = input.readline()
	if not line:
		break
	if line[0] == "#":
		index = line[2:-1]
	elif line == "\n":
		pass
	else:
		dictionary[index].append(line[:-1])


# Handling references

reference_dict = {}
complete_reference_dict = {}

for reference in dictionary['Reference']:
	# looking for first author
	ref_words = reference.split()
	first_author = ref_words[1][:-1]
	if first_author == "de":
		first_author = ref_words[1] + ref_words[2][:-1]
	# looking for first word
	ref = reference.split(':')
	first_word = ref[1].split()[0][1:]
	if len(first_word) < 4:
		first_word = ref[1][1:].split()[1]

	key = first_author + "-" + first_word
	key = key.lower()

	reference_dict[ref_words[0]] = '<a name="bib:' + key.lower() + '"></a>"'
	complete_reference_dict[ref_words[0]] = '<a name="bib:' + key.lower() + '"></a>"' + ' '.join(ref_words[1:]).replace("'", "").replace(":", "")


# Printing table

print "| Name     | Year |  Orig | Method | Source |"
print "| -------- |:----:|:-----:|:------:| ------:|"

for value in range(len(dictionary['Name'])):
	print '|', dictionary['Name'][value], '|',
	print dictionary['Year'][value], '|',
	print dictionary['Orig.'][value], '|',
	print dictionary['Method'][value], '|',
	if ',' in dictionary['Source'][value]:
		(value1, value2) = dictionary['Source'][value].split(',')
		print reference_dict[value1 + ']'], ','
		print reference_dict['[' + value2], '|'		
	else:
		print reference_dict[dictionary['Source'][value]], '|'


print
print
print

for key in complete_reference_dict:
	print complete_reference_dict[key]
	print
