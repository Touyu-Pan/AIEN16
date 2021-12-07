import re

text = 'Heneghan and colleagues\'    systematic review, funded by WHO, published in March, 2021, as a preprint, states: “The lack of recoverable   viral culture     samples of SARS-CoV-2 prevents          firm conclusions    to be drawn about airborne transmission”.1 This conclusion, and the wide circulation of                 the review\'s findings, is     concerning because of the public health implications.'
print(text)

print('----------')

text = re.sub(r'\s+', ' ', text)
print(text)