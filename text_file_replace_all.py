#text_file_replace_all.py: Creates edited file with a swapped word

import re

word_swap = re.compile('story')

#opening got.txt and creating got2.txt with swapped text
with open('got.txt','r') as got,open('got2.txt','w') as got2:
    [got2.write(word_swap.sub('fluffy',word)) for word in got]
