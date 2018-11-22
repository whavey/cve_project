import csv

cve_file_path = r'C:\Users\whavey\Desktop\School\cve_fluff_removed.csv'
with open(cve_file_path) as cve_csv:
    reader = csv.reader(cve_csv, delimiter=',')
    line_count = 0
    for row in reader:
            print(f'CVE: {row[0]}\nStatus: {row[1]}\nDescription: {row[2]}\nReferences: {row[3]}\nPhase: {row[4]}\n')
            print('='*30)
            line_count += 1
    print(f'Processed {line_count} lines.')
