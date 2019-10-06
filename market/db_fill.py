from market.models import Generator
import pandas as pd
import csv
import os


# def df_filler():
#     df = pd.read_csv("/home/roman/WebstormProjects/wua_proba/data/all_gen_wyear.csv",
#                      dtype={'EDRPOU': object, 'KOATUU': object})
#     for ind, row in df.iterrows():
#         Generator.objects.get_or_create(edrpou=row['EDRPOU'], name=row['Name'], koatuu=row['KOATUU'],
#                                         tonnes_total=row['Згенеровано відходів в тоннах'],
#                                         tonnes_total=row['Відходів в одиницях Пзув'], tonnes_1=row['Відходи I класу'],
#                                         tonnes_2=row['Відходи II класу'], tonnes_3=row['Відходи III класу'],
#                                         tonnes_4=row['Відходи IV класу'])
#

def db_filler2():
    # with open( os.path.join(os.path.dirname(os.path.dirname(__file__)),'media/documents/GDRAT.xls'), 'r') as inf:
    with open("/home/roman/PycharmProjects/wua_proba/static/data/all_gen_wyear.csv", "r") as infile:
        reader = csv.reader(infile)

        cols = next(reader, None)  # skip the headers
    #     # writer = csv.writer(outfile)
        for row in reader:
            # Generator.objects.get_or_create(row)
            # print(len(cols), cols)
            # print(len(row), row)
            Generator.objects.get_or_create(
                edrpou=row[0],
                name=row[1],
                address=row[2],
                contacts=row[3],
                koatuu=row[4],
                pzuv_total=row[5],
                tonnes_total=row[6],
                tonnes_1=row[7],
                tonnes_2=row[8],
                tonnes_3=row[9],
                tonnes_4=row[10],
                pzuv_total_2015=row[11],
                tonnes_total_2015=row[12],
                tonnes_1_2015=row[13],
                tonnes_2_2015=row[14],
                tonnes_3_2015=row[15],
                tonnes_4_2015=row[16],
                pzuv_total_2016=row[17],
                tonnes_total_2016=row[18],
                tonnes_1_2016=row[19],
                tonnes_2_2016=row[20],
                tonnes_3_2016=row[21],
                tonnes_4_2016=row[22],
                pzuv_total_2017=row[23],
                tonnes_total_2017=row[24],
                tonnes_1_2017=row[25],
                tonnes_2_2017=row[26],
                tonnes_3_2017=row[27],
                tonnes_4_2017=row[28],
                pzuv_total_2018=row[29],
                tonnes_total_2018=row[30],
                tonnes_1_2018=row[31],
                tonnes_2_2018=row[32],
                tonnes_3_2018=row[33],
                tonnes_4_2018=row[34],
                pzuv_total_2019=row[35],
                tonnes_total_2019=row[36],
                tonnes_1_2019=row[37],
                tonnes_2_2019=row[38],
                tonnes_3_2019=row[39],
                tonnes_4_2019=row[40]
            )
