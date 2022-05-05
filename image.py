import fitz

def image(args):
  try:
    f_ = open(args.file, 'rb')
    f_.close()
  except:
    print(f'can\'t open file \'{args.file}\'.')
  doc = fitz.open(args.file)
  for i in range(len(doc)):
      for img in doc.getPageImageList(i):
          xref = img[0]
          pix = fitz.Pixmap(doc, xref)
          if  not pix.is_unicolor:  
            if pix.n < 5:       # this is GRAY or RGB
                pix.writePNG("p%s-%s.png" % (i, xref))
            else:               # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.writePNG("p%s-%s.png" % (i, xref))
                pix1 = None
            pix = None
