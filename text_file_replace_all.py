import re

word_swap = re.compile('story')

#opening got.txt and creating got2.txt with swapped text
with open('got.txt', 'r') as got:
  with open('got2.txt', 'w') as got2:
    for word in got:
      got2.write(word_swap.sub('fluffy',word))
