from datetime import datetime
import sys, requests, codecs, csv

def get_date(date=''):
    if date=='':
        date = datetime.now()
    else:
        try:
            date = datetime.strptime(date, "%d/%m/%Y")
        except:
            return ''
    return date.strftime('%Y-%m-%dT%H:%M:%S')


def get_hk_dh_data(date=''):
    # Data URL refers to https://data.gov.hk/en-data/dataset/hk-dh-chpsebcddr-novel-infectious-agent/resource/05e8a593-1469-4348-937d-2746afd11442
    data_url = 'http://www.chp.gov.hk/files/misc/enhanced_sur_pneumonia_wuhan_eng.csv'
    last_date = ''
    confirmed = 0
    deaths = 0
    recovered = 0
    r = requests.get(data_url, stream=True)
    text = codecs.iterdecode(r.iter_lines(), 'utf-8')
    reader = csv.reader(text, delimiter=',')
    for row in reader:
        try:
            int(row[0])
        except ValueError:
            continue
        if last_date != row[1]:
            if last_date != '' and date != '':
                if date == datetime.strptime(last_date, "%d/%m/%Y") or date == 'ALL':
                    print_data(get_date(last_date), confirmed, deaths, recovered)
            last_date = row[1]
        confirmed += 1
        if row[6] == 'Discharged':
            recovered += 1
        elif row[6] == 'Deceased':
            deaths += 1
    if date == '' or date == 'ALL':
        print_data(get_date(), confirmed, deaths, recovered)

def print_data(date, confirmed, deaths, recovered):
    print('Hong Kong,Hong Kong,%s,%s,%s,%s,22.3000,114.2000' % (date, confirmed, deaths, recovered))

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        try:
            if sys.argv[1] == 'ALL':
                req_date = 'ALL'
            else: 
                req_date = datetime.strptime(sys.argv[1], "%Y%m%d")
        except:
            print('USAGE: %s {optional date like 20190721 or ALL for each days}' % sys.argv[0])
            sys.exit(1)
    else:
        req_date=''
    get_hk_dh_data(req_date)
