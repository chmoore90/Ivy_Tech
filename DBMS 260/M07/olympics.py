# %% [markdown]
# ## M07 Using Python for Data Analysis

# %% [markdown]
# ### Part 1

# %%
import pandas as pd

df = pd.read_csv("M07\olympics.csv", index_col=0, skiprows=1)
for col in df.columns:
    if col[:2] == "01":
        df.rename(columns={col: "Gold" + col[4:]}, inplace=True)
    if col[:2] == "02":
        df.rename(columns={col: "Silver" + col[4:]}, inplace=True)
    if col[:2] == "03":
        df.rename(columns={col: "Bronze" + col[4:]}, inplace=True)
    if col[:1] == "№":
        df.rename(columns={col: "#" + col[1:]}, inplace=True)
names_ids = df.index.str.split("\s\(")  # split the index by '('
df.index = names_ids.str[0]  # the [0] element is the country name (new index)
df["ID"] = names_ids.str[1].str[
    :3
]  # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop("Totals")
print(df.head())

# %% [markdown]
# Question 1: Which country has won the most gold metals in summer olympics?

# %%
def answer_one():
    x = max(df['Gold'])
    ans = df[df['Gold'] == x].index.tolist()
    return ans[0]

print(answer_one())

# %% [markdown]
# Question 2: Which country had the biggest difference between theit summer and winter gold medal counts?

# %%
def answer_two():
    x = max(df['Gold'] - df['Gold.1'])
    ans = df[(df['Gold'] - df['Gold.1']) == x].index.tolist()
    return ans[0]

print(answer_two())

# %% [markdown]
# Question 3: Which country has the biggest difference between their summer and winter gold medal counts relative to their total gold medal count? Only include countries that have won at least 1 gold in both summer and winter.

# %%
def answer_three():
    df_gold = df[(df['Gold']>0) & (df['Gold.1']>0)]
    df_max_diff = (abs(df_gold['Gold']-df_gold['Gold.1'])/df_gold['Gold.2'])
    return df_max_diff.idxmax()

print(answer_three())
