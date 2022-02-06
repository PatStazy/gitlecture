import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("1976-2020-president.csv")
df = pd.read_csv("C:\\Users\\patri\\1976-2020-president.csv")
print(df)

#Drops unnecessary columns from data set

df = df.drop(columns=["state_po", "state_fips", "state_cen", "state_ic", "writein", "version", "notes", "office",
                "party_simplified", "candidate"])
print(df)

#Drops unnecessary rows from data set, being rows with "party_detailed" being NO PARTY AFFILIATION and rows with
#"year" != 2016

df_2016 = df[df["year"]==2016]
df_2016 = df_2016.query("party_detailed != 'NO PARTY AFFILIATION'")
print(df_2016)

#Dropping all NaN values within data

df_2016 = df_2016.dropna()
df_2016

#Finding all parties in party_detailed and dropping the ones were candidatevotes > 100000

Sum_party_detailed = df_2016[["candidatevotes", "party_detailed"]].groupby(["party_detailed"]).sum()
Sum_party_detailed_drop = Sum_party_detailed.query('candidatevotes>100000')
Sum_party_detailed_drop

#Adding the sum of total candidate votes for all parties

df_2016.set_index("party_detailed", inplace = True)
Total_CON = df_2016.loc["CONSERVATIVE"]["candidatevotes"].sum()
Total_CP = df_2016.loc["CONSTITUTION PARTY"]["candidatevotes"].sum()
Total_DEM = df_2016.loc["DEMOCRAT"]["candidatevotes"].sum()
Total_GR = df_2016.loc["GREEN"]["candidatevotes"].sum()
Total_IND = df_2016.loc["INDEPENDENCE"]["candidatevotes"].sum()
Total_INDEP = df_2016.loc["INDEPENDENT"]["candidatevotes"].sum()
Total_LIB = df_2016.loc["LIBERTARIAN"]["candidatevotes"].sum()
Total_REP = df_2016.loc["REPUBLICAN"]["candidatevotes"].sum()
Total_WF = df_2016.loc["WORKING FAMILIES"]["candidatevotes"].sum()

#Aligning votes from parties to either REP or DEM based on Political spectrum and affiliation

Vote_Aligning_REP = Total_REP + Total_CON + Total_LIB + Total_CP + Total_INDEP
Vote_Aligning_DEM = Total_DEM + Total_GR + Total_IND + Total_WF
Third_party_align_REP = Total_CON + Total_LIB + Total_CP + Total_INDEP
Third_party_align_DEM = Total_GR + Total_IND + Total_WF
Third_party_align_REP

Third_party_align_DEM

#Y-axis is in tens of millions
#Adding Third_party_align_REP and Third_party_align_DEM to Total_REP and Total_DEM

Main_Parties = [Total_REP, Total_DEM]
Third_Parties_Combined = [Third_party_align_REP, Third_party_align_DEM]
index = ["Republican Total", "Democrat Total"]
axs = pd.DataFrame({"Main Parties": Main_Parties, "Third Parties": Third_Parties_Combined}, index=index)
# graph = axs.plot.bar(rot=0)
graph = axs.plot.bar(stacked=True)
graph.set_ylim([0,70000000])
graph




