import re

word_swap = re.compile('story')

with open('got.txt', 'r') as got:
  with open('got2.txt', 'w') as got2:
    for i in got:
      got2.write(word_swap.sub('fluffy',i))
