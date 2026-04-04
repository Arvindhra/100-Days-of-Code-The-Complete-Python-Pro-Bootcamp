# Read the starting letter
with open('./Input/Letters/starting_letter.txt') as starting_file:
    starting_file_contents = starting_file.read()

with open('./Input/Names/invited_names.txt') as names_file:
    names_list = names_file.readlines()

new_names = []
output_text_file = []

for name in names_list:
    new_name = name.rstrip()
    new_names.append(new_name)
    new_output_file_text = starting_file_contents.replace('[name]',new_name)
    output_text_file.append(new_output_file_text)

for name,text_file in zip(new_names,output_text_file):
    with open(f'./Output/ReadyToSend/{name}.txt','w') as output_file:
        output_file.write(text_file)








