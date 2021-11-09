# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 09:19:47 2021

Takes Outlook junk email export (name as test.txt),
and tidies it up to contain domains (output file as out.txt)

"""

# if font/encoding issue encountered
# copy exported junk email addresses and
# paste into Word docx as plain text
# then copy and paste again into test.txt 

with open('test.txt') as f:
    raw_list = f.readlines()

out_list = []
for e in raw_list:
    # Check if already in domain form
    if (e[0] == '@') or ('@' not in e):
        if e not in out_list: out_list.append(e)
    # Exclude some domains
    elif ('gmail.com' in e) or ('yahoo.com' in e) or ('outlook.com' in e):
        if e not in out_list: out_list.append(e)
    # Simple text manipulation to edit to domain only
    else:
        ee = '@' + e.split('@')[-1]
        if ee not in out_list: out_list.append(ee)

with open('out.txt', 'wt', encoding='latin-1') as f:
    for e in out_list:
        f.write(e)
