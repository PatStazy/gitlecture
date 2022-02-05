import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("1976-2020-president.csv")
df = pd.read_csv("C:\\Users\\patri\\1976-2020-president.csv")
print(df)

#Drops unnecessary columns from data set

df = df.drop(columns=["state_po", "state_fips", "state_cen", "state_ic", "writein", "version", "notes", "office", "candidate",
                "party_detailed"])
print(df)

#Drops unnecessary rows from data set

df_2016 = df[df["year"]==2016]
print(df_2016)

#Sum_X_3 refers to the summary statistics of all three independent variables: Libertarian + Other, Republican, and
#Democrate voter data per state
#year not included as year data (Sum_X_3) = year data (df_2016)
#totalvotes not included as totalvotes data (Sum_X_3) = totalvotes data (df_2016)

Sum_X_3 = df_2016[["candidatevotes","party_simplified"]].groupby(["party_simplified"]).sum()
# Sum_X_3 = df_2016[["state","candidatevotes","party_simplified", "totalvotes"]].groupby(["state","party_simplified"]).sum()
Sum_X_3

#Adding the sum of total candidate votes for LIBERTARIAN and OTHER

df_2016.set_index("party_simplified", inplace = True)
Total_LIB = df_2016.loc["LIBERTARIAN"]["candidatevotes"].sum()
Total_OTH = df_2016.loc["OTHER"]["candidatevotes"].sum()
Total_Other_Party = Total_OTH + Total_LIB
Total_Other_Party

#Y-axis is in tens of millions

axs = Sum_X_3.plot.bar()
axs.set_ylim([0,70000000])




