import pandas as pd
df = pd.read_csv('./sms_spam_ham.csv')
df.columns = ["label", "text"]
print(df.head(10))

neg_count = 0
pos_count = 0
max_pos_count = 75478
train = []
for _,row in df.iterrows():
    if row["label"] == 1:
        neg_count+=1
        if neg_count>max_pos_count:
            continue
    else:
        pos_count+=1
        if pos_count>max_pos_count:
            continue
    train.append([row["label"], row["text"]])

new_df = pd.DataFrame(train)

print(len(new_df))
new_df.to_csv('./sms_spam_ham_sample.csv', index=None)
