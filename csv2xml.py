import csv              
f = open('Abilene_All_20210104-20210110.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
   data.append(row)
f.close()

def convert_line(line):
    return """<prediction>
    <forecast_time>"%s"</forecast_time>
    <at>"%s"</at>
    <td>"%s"</td>
    <ws>"%s"</ws>
    <cc>'%s"</cc>
    <sn>"%s"</sn>
    <ra>"%s"</ra>
    <ap>"%s"</ap>
    </prediction>""" %(
        line[1], line[7], line[8], line[11], 0, 0, line[6], line[5]
    )

print ('\n'.join([convert_line(row) for row in data[1:]]))
