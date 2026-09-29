import pandas as pd

df = pd.read_csv('Credit-Card-Financial-Dashboard\credit_card.csv')
df['Week_Start_Date'] = pd.to_datetime(df['Week_Start_Date'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')
df.to_csv('Credit-Card-Financial-Dashboard\credit_card_fixed.csv', index=False)


