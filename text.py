# -*- encoding: utf-8 -*-
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def text(args):
  try:
    f_ = open(args.file, 'rb')
    f_.close()
  except:
    print(f'can\'t open file \'{args.file}\'.')
  output_string = StringIO()
  with open(args.file, 'rb') as in_file:
      parser = PDFParser(in_file)
      doc = PDFDocument(parser)
      rsrcmgr = PDFResourceManager()
      device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
      interpreter = PDFPageInterpreter(rsrcmgr, device)
      for page in PDFPage.create_pages(doc):
          interpreter.process_page(page)
  text = output_string.getvalue()

  text = text.replace('-\n', '')
  text = text.replace('.\n', 'tmp__tmp')
  text = text.replace('\n', '')
  text = text.replace('tmp__tmp', '.\n')
  text = text.replace('\u2013', '-')
  text = text.replace('\u2010', '-')
  text = text.replace('\u0130', 'i')
  
  Information, _ = text.split('Abstract')
  Abstract, _ = _.split('. Introduction')
  Mehod, _ = _.split('. Conclusion')
  Conclusion, Reference = _.split('. Reference')

  f = open("Information.txt",'a')
  f.write(Information)
  f.close()

  f = open("Abstract.txt",'a')
  f.write(Abstract)
  f.close()

  f = open("Method.txt",'a', encoding='UTF-8')
  f.write(Mehod)
  f.close()

  f = open("Conclusion.txt",'a')
  f.write(Conclusion)
  f.close()

  f = open("Reference.txt",'a')
  f.write(Reference)
  f.close()
