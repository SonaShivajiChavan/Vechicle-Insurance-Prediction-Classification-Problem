"""
usage: python remove_output.py notebook.ipynb [ > without_output.ipynb ]
"""
import sys
import io
from IPython.nbformat import current


def remove_outputs(nb):
    """remove the outputs from a notebook"""
    for ws in nb.worksheets:
        for cell in ws.cells:
            if cell.cell_type == 'code':
                cell.outputs = []

if __name__ == '__main__':
    fname = sys.argv[1]
    with io.open(fname, 'r') as f:
        nb = current.read(f, 'json')
    remove_outputs(nb)
    print current.writes(nb, 'json')
ghost commented on 20 Mar 2013
purge only binary display blobs, and renumber prompts
to eliminate diff noise. more invasive.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import json
import codecs

def jload(fname):
        return json.load(codecs.open(fname))
def jstore(s,fname,indent=2):
        with codecs.open(fname,"wb",encoding="utf-8") as f:
                json.dump(s,f,indent=indent)

def purge_nb(s):
    def should_keep(o):
        return o.get('output_type') != 'display_data'
    i=0
    for ws in s['worksheets']:
        for cell in ws['cells']:
            if cell.get('prompt_number'):
                cell['prompt_number']=i
                i+=1
            os = cell.get('outputs',[])
            os = [o for o in os if should_keep(o)]
            if os:
                cell['outputs'] = os
            else:
                cell.pop('outputs',None)


def main():
    assert len(sys.argv)>=2
    print( sys.argv[1])
    fname =  sys.argv[1]

    s=jload(fname)
    purge_nb(s)
    jstore(s,sys.argv[2],1)

if __name__ == "__main__":
    sys.exit(main())
