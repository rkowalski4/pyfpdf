"""png_image_test.py"""

import unittest
import sys
import os
sys.path.insert(0,
  os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    os.path.join('..', '..', '..')
  )
)

import fpdf
import test
from test.utilities import relative_path_to, \
                           set_doc_date_0, \
                           calculate_hash_of_file

from PIL import Image
import io

class InsertPNGSuite(unittest.TestCase):
  def test_insert_png_memory(self):
    pdf = fpdf.FPDF(unit = 'pt')
    pdf.compress = False

    images = [relative_path_to(f) for f
              in os.listdir(relative_path_to('.'))
              if f.endswith(".png")]

    for image in images:
      pdf.add_page()
      i = Image.open(image)
      # print image#, i.size

      temp_i_storage = io.BytesIO()
      i.save(temp_i_storage, format = 'png')
      pdf.image(image, x = 0, y = 0, w = i.size[0], h = i.size[1],
                type = '', link = None, file = temp_i_storage)

    # imagename = relative_path_to('insert_images_insert_jpg.jpg')
    # pdf.image(imagename, x = 15, y = 15, h = 140)

    set_doc_date_0(pdf)
    outfile = relative_path_to('insert_images_png_test.pdf')
    pdf.output(outfile, 'F')
    # print(calculate_hash_of_file(outfile))

    test_hash = calculate_hash_of_file(outfile)
    self.assertEqual(test_hash, "5d11f7a3235d154c3a7001d3b8551d6e")
    os.unlink(outfile)

if __name__ == '__main__':
  unittest.main()

## Code used to create test:
