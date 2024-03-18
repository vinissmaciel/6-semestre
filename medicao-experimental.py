#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from time import time
from matplotlib import pyplot as plt

T = []
N = range(10000,1000000,10000)

for n in N:
    tic = time()

    for i in range(n):
        a = 1

    toc = time()
    T.append(toc - tic)
    print(T[-1])

plt.plot(N,T,'k.')
plt.show()


# In[17]:


from time import time

n = 10**6
N = range(n)

tic = time()
for i in N:
    a = 1

toc = time()

print(toc - tic)


# In[40]:


#Adicionando repetições r
import numpy as np
from time import time
from matplotlib import pyplot as plt

n = 10**6          # numero de operações
N = range(n)       # 
T = [] 
r = 1000           # numero de repetições
R = range(r)

for j in R:
    tic = time()
    for i in N:
        a = 1
    toc = time()
    
    #print(toc - tic)
    T.append(toc - tic)


# In[41]:


plt.bar(R, T)
plt.show()


# In[42]:


plt.plot(T)
#plt.bar(R, T)
plt.show()


# In[43]:


plt.hist(T, 20)
plt.show()


# In[44]:


S = np.std(T)
M = np.mean(T)
variabilidade = S/M
print("Variabilidade: ", variabilidade)


# In[49]:


#Calculando variabilidade cada cada repetição
import numpy as np
from time import time
from matplotlib import pyplot as plt

n = 10**6          # numero de operações
N = range(n)       # 
T = [] 
r = 1000           # numero de repetições
R = range(r)
V = []             # vetor de variabilidade

for j in R:
    tic = time()
    for i in N:
        a = 1
    toc = time()
    
    #print(toc - tic)
    T.append(toc - tic)
    
    S = np.std(T)
    M = np.mean(T)
    variabilidade = S/M
    V.append(variabilidade)


# In[50]:


plt.plot(V)
plt.show()


# In[51]:


#Calculando variabilidade cada cada repetição
import numpy as np
from time import time
from matplotlib import pyplot as plt

n = 10**6          # numero de operações
N = range(n)       # 
T = [] 
r = 1000           # numero de repetições
R = range(r)
V = []             # vetor de variabilidade
S = []             # vetor de desvio padrao
M = []             # vetor de media

for j in R:
    tic = time()
    for i in N:
        a = 1
    toc = time()
    
    #print(toc - tic)
    T.append(toc - tic)
    
    S.append(np.std(T))
    M.append(np.mean(T))


# In[52]:


plt.plot(M)
plt.plot(S)
plt.grid()
plt.legend(["Média", "Desvio padrão"])
plt.show()

