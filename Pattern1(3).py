
# coding: utf-8

# In[15]:


print('Given String: \n')


# In[16]:


str='abcdefghijklmnop'


# In[17]:


print(str)


# In[18]:


print('Required Pattern \n')


# In[19]:


for i in range(0,16,3):
        j=i+4
        print(str[i:j])
        if i>=12: #to prevent 6th iteration
            break


# In[20]:


input("Press enter to exit ;)")


# In[9]:


#The approach used here:  generate a pattern for the indices where the splitting has to take place and generate a relation between i and j and iterate over i till 12(why? the answer is- just dry run the code)

