from pdf import create_pdf
from jinja2 import Environment, FileSystemLoader
import os

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def html_doc(variables):
    # Create the jinja2 environment. Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)
    return j2_env.get_template('album.html.j2').render(
        variables=variables
    )


pdf_data = html_doc({
  'photos': [
    'https://s3.eu-central-1.amazonaws.com/153412-kkanclerz/photos/009d30b3d9a143a5937fbab9a50a4009/empty_image.jpg',
    'https://s3.eu-central-1.amazonaws.com/153412-kkanclerz/photos/009d30b3d9a143a5937fbab9a50a4009/empty_image.jpg'
   ]
})
pdf = create_pdf(pdf_data)

file_ = open('album.pdf', 'w')
file_.write(pdf.getvalue())
file_.close()
