 # Solution
bank_df["Annual Interest"] = bank_df["Account Balance"] * 0.03
bins = [0, 1000, 3000, 5000]
labels = ["Low", "Medium", "High"]
bank_df["Balance Category"] = pd.cut(bank_df["Account Balance"], bins=bins, labels=labels)
bank_df["Normalized Balance"] = (bank_df["Account Balance"]   bank_df["Account Balance"].min()) /  (bank_df["Account Balance"].max()- bank_df["Account Balance"].min())
print(bank_df)