# Code: 
# import module
import pandas as pd
 
# assign dataset
df = pd.read_csv("country_code.csv")
 
# display
print("Type-", type(df))
print(df)



# Type- <class 'pandas.core.frame.DataFrame'>
#         name   age        marks    hobbies
# Anjali    25  85.5      Reading  Traveling
# Teena     22  78.0     Painting     Hiking
# Smart     30  92.3  Photography    Cooking
# Yami      28  89.7       Sports      Music