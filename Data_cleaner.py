'''
Name: Data Cleaner for HW2 of FE 595
Intro: This file should load the class' data from theyfightcrime.org, clean it, and save the males in one file and the females in
another.
Author: William Long
Date : 09/22/2019
'''

import pandas as pd
import numpy as np

#Frist, we need to load the data.

m_full = pd.read_csv('Char Data\Male_data.csv', names=("index", "male")).drop(columns="index")
f_full = pd.read_csv('Char Data\Female_data.csv', names=("index", "female")).drop(columns="index")
m_full = m_full.drop(0)
f_full = f_full.drop(0)

m_full = m_full.append(pd.read_csv('Char Data\male.txt', names=["male"], sep='\t'), ignore_index=True)
m_full = m_full.append(pd.read_csv('Char Data\malefile.txt', names=["male"], sep='\t'), ignore_index=True)
m_full = m_full.append(pd.read_csv('Char Data\his.txt', names=["male"], sep='\t'), ignore_index=True)
m_full = m_full.append(pd.read_csv('Char Data\A\male.txt', names=["male"], sep='\t'), ignore_index=True)
m_full = m_full.append(pd.read_csv('Char Data\C\male.txt', names=["male"], sep='\t'), ignore_index=True)
m_full = m_full.append(pd.read_csv('Char Data\Characters\Male_Characters.txt', names=["male"], sep='\t'), ignore_index=True)
m_full = m_full.append(pd.read_csv('Char Data\E\male.txt', names=["male"], sep='\t'), ignore_index=True)
m_full = m_full.append(pd.read_csv('Char Data\FE595_Characters\he.txt', names=["male"], sep='\t'), ignore_index=True)
m_full = m_full.append(pd.read_csv('Char Data\FE595_H2\male.txt', names=["male"], sep='\t'), ignore_index=True)
m_full = m_full.append(pd.read_csv('Char Data\B\male.txt', names=["male"], sep=':'), ignore_index=True)
m_full = m_full.append(pd.read_csv('Char Data\hes.txt', names=["male"], sep='\t'), ignore_index=True)



m_a = pd.read_csv('Char Data\D\hesfile.txt', names=["male"], sep='\t')
m_a["male"] = m_a["male"].str.replace('\\', '', regex=False)
m_full = m_full.append(m_a, ignore_index=True)

f_full = f_full.append(pd.read_csv('Char Data\Female.txt', names=["female"], sep='\t'), ignore_index=True)
f_full = f_full.append(pd.read_csv('Char Data\Femalefile.txt', names=["female"], sep='\t'), ignore_index=True)
f_full = f_full.append(pd.read_csv('Char Data\her.txt', names=["female"], sep='\t'), ignore_index=True)
f_full = f_full.append(pd.read_csv('Char Data\shes.txt', names=["female"], sep='\t'), ignore_index=True)
f_full = f_full.append(pd.read_csv('Char Data\A\Female.txt', names=["female"], sep='\t'), ignore_index=True)
f_full = f_full.append(pd.read_csv('Char Data\C\Female.txt', names=["female"], sep='\t'), ignore_index=True)
f_full = f_full.append(pd.read_csv('Char Data\Characters\Female_Characters.txt', names=["female"], sep='\t'), ignore_index=True)
f_full = f_full.append(pd.read_csv('Char Data\E\Female.txt', names=["female"], sep='\t'), ignore_index=True)
f_full = f_full.append(pd.read_csv('Char Data\FE595_Characters\she.txt', names=["female"], sep='\t'), ignore_index=True)
f_full = f_full.append(pd.read_csv('Char Data\FE595_H2\Female.txt', names=["female"], sep='\t'), ignore_index=True)
f_full = f_full.append(pd.read_csv('Char Data\B\Female.txt', names=["female"], sep=':'), ignore_index=True)

f_a = pd.read_csv('Char Data\D\shesfile.txt', names=["female"], sep='\t')
f_a["female"] = f_a["female"].str.replace('\\', '', regex=False)
f_full = f_full.append(f_a, ignore_index=True)

m_full.to_csv(r'Male_full.txt', header=None, index=None, sep=' ', mode='a')
f_full.to_csv(r'Female_full.txt', header=None, index=None, sep=' ', mode='a')
