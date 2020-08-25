import csv
import re

with open('breitbart new.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        title = row[2]
        text = row[3]
        fname = " ".join(re.findall("[a-zA-Z]+", str(title)))
        fname = str(fname).replace(' ', "_")
        puretitle =  str(fname) + ".txt"
        print(puretitle)
        f=open(puretitle,'w', encoding='utf-8')
        for ele in text:
            f.write(ele)

        f.close()
        print("done")