
# Do NOT edit this file. Instead, just call it from the command line,
# using the instructions in the assignment notebook.

import sys
questions = sys.argv[1:]


valid_ids = ['q1', 'q2', 'q3', 'q4', 'q5']
break_flag = False
invalid_ids = []
for question in questions:
    if question != 'all' and question not in valid_ids:
        invalid_ids.append(question)

if len(invalid_ids) > 0:
    print(str(invalid_ids) + ' is/are not a valid question number(s). The possible question numbers are ' + str(valid_ids) + '.')
    sys.exit()

# Initialize Otter
import otter
grader = otter.Notebook("project.ipynb")

# %load_ext autoreload
# %autoreload 2

import pandas as pd
import numpy as np
from pathlib import Path
import re
import requests
import time

from project import *

# don't change this cell, but do run it -- it is needed for the tests
beowulf = get_book('https://www.gutenberg.org/ebooks/16328.txt.utf-8')

if 'q1' in questions or questions == [] or 'all' in questions:
    print(grader.check("q1"))

# don't change this cell, but do run it -- it is needed for the tests
import time
start = time.time()
shakes = tokenize(open(Path('data') / 'shakespeare.txt').read())
elapsed = time.time() - start
elapsed # Should be (much) under 5

if 'q2' in questions or questions == [] or 'all' in questions:
    print(grader.check("q2"))

# don't change this cell, but do run it -- it is needed for the tests
tokens = tuple('one one two three one two four'.split())
unif = UniformLM(tokens)
unif.sample(100)

if 'q3' in questions or questions == [] or 'all' in questions:
    print(grader.check("q3"))

# don't change this cell, but do run it -- it is needed for the tests
tokens = tuple('one one two three one two four'.split())
unigram = UnigramLM(tokens)
unigram.sample(100)

if 'q4' in questions or questions == [] or 'all' in questions:
    print(grader.check("q4"))

# Uncomment and run – should take less than 10 seconds
# shakes_uniform = UniformLM(shakes)
# shakes_unigram = UnigramLM(shakes)

# Uncomment and run
# shakes_uniform.sample(10)

# Uncomment and run
# shakes_unigram.sample(10)

# don't change this cell, but do run it -- it is needed for the tests
tokens = tuple('\x02 one two three one four \x03'.split())
bigrams = NGramLM(2, tokens)
out = bigrams.create_ngrams(tokens)

# don't change this cell, but do run it -- it is needed for the tests
tokens = "\x02 Humpty Dumpty sat on a wall , Humpty Dumpty had a great fall . \x03 \x02 All the king ' s horses and all the king ' s men couldn ' t put Humpty together again . \x03".split()
tokens = tuple(tokens)
ngram = NGramLM(2, tokens)
out_5a1 = ngram.create_ngrams(tokens)
out_5b1 = ngram.mdl
out_5c1 = ngram
out_5d1 = ngram.sample(500) 

if 'q5' in questions or questions == [] or 'all' in questions:
    print(grader.check("q5"))

# Uncomment and run
# shakes_bigram = NGramLM(2, shakes)
# shakes_bigram.sample(50)

homer_tokens = tuple(open(Path('data') / 'homertokens.txt').read().split(' '))

# NGramLM(5, homer_tokens)

