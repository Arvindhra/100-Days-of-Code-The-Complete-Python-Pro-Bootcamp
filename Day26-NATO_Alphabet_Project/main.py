import pandas as pd

df_nato_alp = pd.read_csv('nato_phonetic_alphabet.csv')

df_nato_dict = {row["letter"]:row["code"] for (index,row) in df_nato_alp.iterrows()}
word_input = input("Enter a word: ").upper()
output_list = [df_nato_dict[letter] for letter in word_input]
print(output_list)

