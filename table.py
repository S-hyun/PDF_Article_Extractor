import tabula # Read pdf into list of DataFrame 
import sys
import pandas as pd
import pdfplumber


def table(args):
  try:
    f_ = open(args.file, 'rb')
    f_.close()
  except:
    print(f'can\'t open file \'{args.file}\'.')
    return  
  pdf = pdfplumber.open(args.file)
  writer=pd.ExcelWriter(args.file.replace('pdf', 'xlsx'), engine='openpyxl') # Generate xlsx file
  table_num = 0
  for i in range(len(pdf.pages)):
    if "Table" in pdf.pages[i].extract_text():
      tables = pdf.pages[i].extract_tables()
      for table in tables:
        if len(table) > 2 and len(table[0]) > 1:      #After specifying the sheet name in the generated file, put the saved result value in the dataframe
          table_num = table_num+1
          table_p = pd.DataFrame(table)
          table_p.to_excel(writer, sheet_name='table'+str(table_num))
  # save the xlsx file
  writer.save()
