# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
df = fb_messages

df = df.groupby('user1').sum().reset_index()

df = df.drop('id' ,axis =1)

df =df.sort_values('msg_count' , ascending = False)

df = df.head(10)

