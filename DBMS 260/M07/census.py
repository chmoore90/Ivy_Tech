# %% [markdown]
# ## M07 Using Python for Data Analysis

# %% [markdown]
# ### Part 2

# %% [markdown]
# Question 5: Which state had the most counties in it?

# %%
import pandas as pd

census_df = pd.read_csv("M07\census.csv")
print(census_df.head())


def answer_five():
    counties_df = census_df[census_df["SUMLEV"] == 50]
    x = counties_df.groupby("STNAME").count()["SUMLEV"]
    ans = x.idxmax()
    return ans


print(answer_five())

# %% [markdown]
# Question 6: Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)?

# %%
def answer_six():
    counties_df = census_df[census_df["SUMLEV"] == 50]
    top_counties_df = (
        counties_df.sort_values(by=["STNAME", "CENSUS2010POP"], ascending=False)
        .groupby("STNAME")
        .head(3)
    )
    ans = (
        top_counties_df.groupby("STNAME")
        .sum()
        .sort_values(by="CENSUS2010POP")
        .head(3)
        .index.tolist()
    )
    return ans


print(answer_six())

# %% [markdown]
# Question 7: In this datafile, the United States is broken up into four regions using the "REGION" column.
# Create a script that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.

# %%
def answer_seven():
    counties_df = census_df[census_df["SUMLEV"] == 50]
    ans = counties_df[
        ((counties_df["REGION"] == 1) | (counties_df["REGION"] == 2))
        & (counties_df["CTYNAME"] == "Washington County")
        & (counties_df["POPESTIMATE2015"] > counties_df["POPESTIMATE2014"])
    ][["STNAME", "CTYNAME"]]
    return ans


print(answer_seven())
