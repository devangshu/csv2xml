import csv              
from datetime import date

f = open('Abilene_All_20210104-20210110.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
   data.append(row)
f.close()

today = date.today()

def convert_line(line):
    return """
    \t\t<prediction>
    \t\t\t<forecast_time>%s</forecast_time>
    \t\t\t<at>%s</at>
    \t\t\t<td>%s</td>
    \t\t\t<ws>%s</ws>
    \t\t\t<cc>%s</cc>
    \t\t\t<sn>%s</sn>
    \t\t\t<ra>%s</ra>
    \t\t\t<ap>%s</ap>
    \t\t</prediction>""" %(
        line[1], line[7], line[8], line[11], 0, 0, line[6], line[5]
    )

def print_header():
    return """
    <forecast>
    \t<header>
    \t\t<production_date>%s</production_date>
    \t\t<version>1.1</version>
    \t\t<filetype>forecast</filetype>
    \t\t<station_id>ofr</station>
    \t</header>
    \t<prediction-list>"""%(today.strftime("%m/%d/%Y"))

def print_footer():
    return """
    \t</prediction-list>
    </forecast>"""

print (print_header())
print ('\n'.join([convert_line(row) for row in data[1:]]))
print (print_footer())
