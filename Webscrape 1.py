#!/usr/bin/env python
# coding: utf-8

# ## WebScrape Project 1
# #### Combining different pages on different battle royal games to compare player count over the past few years
# 

# These would be the preliminary steps which would involve importing the libraries required as well as adding the website pages required for the webscraping project

# In[1]:


#Importing the necessary libraries for the webscraping.
from bs4 import BeautifulSoup
import requests
import pandas as pd


# The next cell takes different pages from the same website. Activeplayer.io
# The BR games in question include: 
# - Apex Legends
# - Call of Duty Warzone
# - Overwatch 2
# - Fortnite
# - Player Unknown BattleGrounds(PUBG)`

# The website used for the webscraping is called "activeplayer.io" which focuses on various games with online capabilities and allows for the player base to be counted.

# In[2]:


#Here we have the various pages for each BR and the requests used to scrape the page of each.
apex = 'https://activeplayer.io/apex-legends/'
cod = 'https://activeplayer.io/call-of-duty-warzone/'
ovr2 = 'https://activeplayer.io/overwatch-2/'
fortnite = 'https://activeplayer.io/fortnite/'
pubg = 'https://activeplayer.io/pubg/'

apexpage = requests.get(apex)
codpage = requests.get(cod)
ovrpage = requests.get(ovr2)
ftpage = requests.get(fortnite)
pubgpage = requests.get(pubg)

apexsoup = BeautifulSoup(apexpage.text,'html')
codsoup = BeautifulSoup(codpage.text,'html')
ovrsoup = BeautifulSoup(ovrpage.text,'html')
ftsoup = BeautifulSoup(ftpage.text,'html')
pubgsoup = BeautifulSoup(pubgpage.text,'html')


# In[3]:


# Here we specify the exact table that would be used for the analysis.
apextable = apexsoup.find_all('table')[1]
codtable = codsoup.find_all('table')[1]
ovrtable = ovrsoup.find_all('table')[1]
fttable = ftsoup.find_all('table')[1]
pubgtable = pubgsoup.find_all('table')[1]


print(pubgtable)


# In[4]:


#Here we focus on the titles or column heads for the table or dataframe that is intended.
apex_titles = apexsoup.find_all('th')
cod_titles = codsoup.find_all('th')
ovr_titles = ovrsoup.find_all('th')
ft_titles = ftsoup.find_all('th')
pubg_titles = pubgsoup.find_all('th')

pubg_titles


# In[5]:


#Here we grab the titles or column heads for the table or dataframe that is intended.

apex_table_title = [title.text.strip() for title  in apex_titles]
cod_table_title = [title1.text.strip() for title1  in cod_titles]
ovr_table_title = [title2.text.strip() for title2  in ovr_titles]
ft_table_title = [title3.text.strip() for title3  in ft_titles]
pubg_table_title = [title4.text.strip() for title4 in ft_titles]

print(apex_table_title)
print(cod_table_title)
print(ovr_table_title)
print(ft_table_title)
print(pubg_table_title)


# At this point the dataframes will be created for each BR before inserting the data gathered from each webpage.

# In[6]:


apexdf = pd.DataFrame(columns = apex_table_title)
apexdf.drop(apexdf.columns[[0,1,2]], axis = 1, inplace = True)
apexdf


# In[7]:


coddf = pd.DataFrame(columns = cod_table_title)
coddf.drop(coddf.columns[[0,1]], axis = 1, inplace = True)
coddf


# In[8]:


ovrdf = pd.DataFrame(columns = ovr_table_title)
ovrdf.drop(ovrdf.columns[[0,1,2]], axis = 1, inplace = True)
ovrdf


# In[9]:


ftdf = pd.DataFrame(columns = ft_table_title)
ftdf.drop(ftdf.columns[[0,1,2]], axis = 1, inplace = True)
ftdf


# In[10]:


pubgdf = pd.DataFrame(columns = pubg_table_title)
pubgdf.drop(pubgdf.columns[[0,1,2]], axis = 1, inplace = True)
pubgdf


# For this next stage, the specified table containing the data from each webpage would be singled out and inserted into each of the dataframes that were earlier made.

# In[11]:


apex_col_data = apexsoup.find_all('tr')
cod_col_data = codsoup.find_all('tr')
ovr_col_data = ovrsoup.find_all('tr')
ft_col_data = ftsoup.find_all('tr')
pubg_col_data = pubgsoup.find_all('tr')


# In[28]:


#For the Apex Legends BR
for row in apex_col_data[7:46]:
    apex_row_data = (row.find_all('td'))
    apex_individual_row_data = [data.text.strip() for data  in apex_row_data]
    print(apex_individual_row_data )
    
    length = len(apexdf)
    apexdf.loc[length] = apex_individual_row_data


# In[27]:


#For the Call of Duty Warzone BR
for row in cod_col_data[7:43]:
    cod_row_data = (row.find_all('td'))
    cod_indi_row_data = [data.text.strip() for data in cod_row_data]
    print(cod_indi_row_data)
    
    cod_length = len(coddf)
    coddf.loc[cod_length] = cod_indi_row_data


# In[24]:


#For the Overwatch 2 BR
for row in ovr_col_data[7:21]:
    ovr_row_data = (row.find_all('td'))
    ovr_indi_row_data = [data.text.strip() for data  in ovr_row_data]
    print(ovr_indi_row_data )
    
    length = len(ovrdf)
    ovrdf.loc[length] = ovr_indi_row_data


# In[29]:


#For the Fortnite BR
for row in ft_col_data[7:56]:
    ft_row_data = (row.find_all('td'))
    ft_indi_row_data = [data.text.strip() for data in ft_row_data]
    print(ft_indi_row_data)
    
    ft_length = len(ftdf)
    ftdf.loc[ft_length] = ft_indi_row_data


# In[30]:


#For the Pubg BR
for row in pubg_col_data[7:55]:
    pubg_row_data = (row.find_all('td'))
    pubg_indi_row_data = [data.text.strip() for data in pubg_row_data]
    print(pubg_indi_row_data)
    
    pubg_length = len(pubgdf)
    pubgdf.loc[pubg_length] = pubg_indi_row_data


# This next phase would involve checking each dataframe and more cleaning of the dataset as this would include removing commas and changing data types.

# In[31]:


apexdf


# In[32]:


apexdf = apexdf.replace(',','',regex = True)
apexdf = apexdf.astype({"Average Monthly Players":"int","Monthly Gain / Loss":"int",
                        "Monthly Gain / Loss %":'float',"All Time Peak":"int"})
apexdf


# In[33]:


coddf 


# In[34]:


coddf = coddf.replace(',','',regex = True)
coddf = coddf.astype({"Average Monthly Players":"int","Monthly Gain / Loss":"int",
                        "Monthly Gain / Loss %":'float',"Peak Players In a Day":"int"})
coddf


# In[35]:


ovrdf


# In[36]:


ovrdf = ovrdf.replace(',','',regex = True)
ovrdf = ovrdf.astype({"Average Monthly Players":"int","Monthly Gain / Loss":"int",
                        "Monthly Gain / Loss %":'float',"Average Daily Players":"int"})
ovrdf


# In[37]:


ftdf


# In[38]:


ftdf = ftdf.replace(',','',regex = True)
ftdf = ftdf.astype({"Average Monthly Players":"int","Monthly Gain / Loss":"int",
                        "Monthly Gain / Loss %":'float',"Peak Players In a Day":"int"})
ftdf


# In[39]:


pubgdf


# In[40]:


pubgdf = pubgdf.replace(',','',regex = True)
pubgdf = pubgdf.astype({"Average Monthly Players":"int","Monthly Gain / Loss":"int",
                        "Monthly Gain / Loss %":'float',"Peak Players In a Day":"int"})
pubgdf


# Finally each dataset would be saved as a csv file.

# In[41]:


apexdf.to_csv(r'D:\data\BR analysis\apexcount.csv')


# In[42]:


coddf.to_csv(r'D:\data\BR analysis\codcount.csv')


# In[43]:


ovrdf.to_csv(r'D:\data\BR analysis\ovrcount.csv')


# In[44]:


ftdf.to_csv(r'D:\data\BR analysis\ftcount.csv')


# In[37]:


pubgdf.to_csv(r'D:\data\BR analysis\pubgcount.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




