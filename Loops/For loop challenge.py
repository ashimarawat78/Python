files=[' Report.csv ', 'DATA .txt ', 'Final .TXT']
for file in files:
              file=file.strip().lower().replace ('.txt ','.csv')
              print(f"Processing {file}")     
