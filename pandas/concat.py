import pandas as pd

df1 = pd.DataFrame({
    "Title": ["Titanic", "Inception"],
    "Rating": [8.0, 8.8]
})

df2 = pd.DataFrame({
    "Title": ["Avatar", "Interstellar"],
    "Rating": [7.9, 8.7]
})

print("DF1")
print(df1)

print("\nDF2")
print(df2)

print("\nConcatenated")
print(pd.concat([df1, df2], ignore_index=True))

print(pd.concat([df1, df2], axis=1)) #----> Sideways (add columns)
print(pd.concat([df1, df2], axis=0)) #----> Down (stack rows)