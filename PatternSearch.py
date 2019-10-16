import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#searches for any non-alphanumeric character in the lorem_ipsum sentence and prints out
#number of non-alphanumeric characters.
pattern = 'sit[^a-zA-Z0-9]amet'
occurrance_sit_amet = re.findall(pattern, lorem_ipsum)
print(len(occurrance_sit_amet))

#replaces any word that has something between sit and amet with only a space between the 
#words sit and amet.
second_pattern = 'sit[-:]amet'
substitution = "sit amet"
replace_results = re.sub(second_pattern, substitution, lorem_ipsum)

#prints out the number of a times sit amet appears in the updated lorem_ipsum that uses the substitution above.
occurrence_sit_amet = re.findall(substitution, replace_results)
print(len(occurrence_sit_amet))