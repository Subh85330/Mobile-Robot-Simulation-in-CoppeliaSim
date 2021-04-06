#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys

# reading first 4 lines
with open(sys.argv[1], 'r') as input_file:
    # with open ( 'D:\IITJ\Semster-1\AI-1\Assignment\input.txt' , 'r') as input_file:
    lines = input_file.read()
lines = lines.split("\n")
g = lines[0]
x = lines[1]
y = lines[2]
l = lines[3]

p = int(g)
s = int(x)
t = int(y)
z = int(l)
N = p * s * t
m = p * t
goodness = 0  # define global variable

# In[2]:


# extracting matrix
f = open(sys.argv[1], 'r')
l = []
l = [line.split() for line in f]

del l[0:4]
D = [[float(x) for x in list] for list in l]  # disimilarity matrix


# In[3]:


# finding similarity sum of recently obtained session
def sim_of_sess(S_new):
    sim_of_sess = 0

    for i in S_new:
        for j in S_new:
            if i != j:
                sim_of_sess = sim_of_sess + S[i][j]
    return (sim_of_sess)


# In[4]:


# Goodness factor a given presentation with respect to the presentations in existing sessions(i.e hueristic)
def GF_of_pre(nextpre_in_sess):
    dis_pre = 0
    for i in Sess:
        dis_pre = dis_pre + D[i][nextpre_in_sess]

    GF_of_pre = goodness + z * dis_pre
    return (GF_of_pre)


# In[5]:


# finding the next best session
def next_session(left):
    new_dict = {new_list: [] for new_list in left}
    for j in left:
        new_dict.update({j: GF_of_pre(j)})
    X = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)

    S_new = []
    for key in X:
        S_new.append(key[0])
    S_new = S_new[:m]
    S_new = sorted(S_new, reverse=False)

    left = [x for x in left if x not in S_new]

    return (S_new, left)


# In[6]:


def GF(goodness, S_new):
    simsess = 0  # calculate overall GF as soon as new session is obtained
    simsess = sim_of_sess(S_new)
    dis_of_sess = 0
    for i in S_new:
        for j in Sess:
            dis_of_sess = dis_of_sess + D[i][j]

    goodness = goodness + simsess + dis_of_sess
    return (goodness)


# In[7]:


import numpy

n = p * t * s
T = [0] * n
for x in range(n):
    T[x] = [1] * n

S = numpy.subtract(T, D)  # similarity matrix

# In[8]:


# finding the first session
import numpy

k = numpy.argsort(S[0])  # sort the values in ascending order and return index
k = k[::-1]  # reverses the string (i.e decending order)
# print(k)
m = p * t
S_new = k[:m]
S_new = sorted(S_new, reverse=False)
# print(S_new)


# In[9]:


# empty=[]
# Sess=empty.extend(S_new)
Sess = S_new  # initializing list of sessions
l = [x for x in k if x not in S_new]
left = sorted(l, reverse=False)  # Remaining presentations after getting session1
# print(Sess)


# In[10]:


goodness = sim_of_sess(S_new)

# In[11]:


for i in range(1, s):
    S_new = next_session(left)[0]  # find the new session
    left = next_session(left)[1]  # remaining presentations
    goodness = GF(goodness, S_new)  # goodness till now
    Sess.extend(S_new)  # update the Sess which are already selected

# In[12]:


# print(goodness)
# print(Sess)


# In[52]:


# A=[0, 1, 4, 5, 8, 9, 2, 3, 6, 7, 10, 11]
B = []
c = []
q = 0
for i in range(s):
    for j in range(t):
        for k in range(p):
            B.append(Sess[q])
            # B.append(A[q])
            B.append(" ")
            q = q + 1
        if (j < t - 1):
            B.append("|")

    # print("\n")
    # print(B)
    c.append(B)
    B = []
# print(c)


# In[53]:


outputfile = open(sys.argv[2], "w+")

# In[54]:


for i in range(len(c)):
    for j in range(len(c[i])):
        # print(c[i][j], end=" ")
        outputfile.write(str(c[i][j]))
    outputfile.write("\n")

outputfile.close();

# In[ ]: