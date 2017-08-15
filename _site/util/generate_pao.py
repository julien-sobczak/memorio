#!/usr/bin/env python

"""
Generate a sample JSON document from a PAO dataset.
The input document should be in CSV format and should begin
with a header line containing the column names.
The program expects two columns to be defined: 'full-name' and 'action-object'.

Running:

$ python3 generate_pao.py 'datasets/PAO Complete List.csv' > data/pao.json
"""

import sys
import json

suits = list('CDHS')
ranks = [str(i) for i in range(2, 11)] + list('JQKA')
cards = [r + s for r in ranks
               for s in suits]
pao = []

with open(sys.argv[1]) as f:
    lines = f.readlines()
    columns = lines[0].strip().split(';')
    number = 0
    for l in lines[1:]:
        l = l.strip()
        number += 1
        if not l:
            # Ignore blank lines
            continue
        fields = l.split(';')
        person = fields[columns.index('full-name')]
        action, obj = fields[columns.index('action-object')].split(' ... ')
        item = {
            'person': person,
            'action': action,
            'object': obj,
            'number': "%02d" % number
        }
        if number < len(cards):
            item['card'] = cards[number]
        pao.append(item)

document = {
    'items': pao
}

print(json.dumps(document, indent=4, separators=(',', ': ')))
