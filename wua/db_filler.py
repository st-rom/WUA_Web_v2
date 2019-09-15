import pandas as pd
# from market.models import Generator


df = pd.read_csv("/home/roman/WebstormProjects/wua_proba/data/all_gen_wyear.csv", dtype={'EDRPOU': object, 'KOATUU': object})
# print(Generator.objects.all())
# print(df.loc[0])
for ind, row in df.iterrows():
    print(row['EDRPOU'])
    break
