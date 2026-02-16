#prompts the user for their name and outputs a pdf using fpdf, a cs50 shirt called shirtificate.pdf
#orientation should be portrait
#The format of the PDF should be A4, which is 210mm wide by 297mm tall.
#The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
#The shirt’s image should be centered horizontally.
#The user’s name should be on top of the shirt, in white text.

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)
pdf.cell(100, 10, "Hello World!")
pdf.cell(100, 10, "Hello World!",new_x="LMARGIN",new_y="NEXT",align="C")
pdf.output("tuto1.pdf")

pdf = FPDF(orientation="P", unit="mm", format="A4")
#It is possible to set the PDF in landscape mode (L) or to use other page formats (such as Letter and Legal) and measure units (pt, cm, in).

#margins can changed with set_margins
#The other built-in fonts are Times, Courier, Symbol and ZapfDingbats.
#Cell is where you add the text and that can be modified
#pdf.cell(60, 10, 'Powered by FPDF.', new_x="LMARGIN", new_y="NEXT", align='C')

#Note that you can disable automatic page breaks, which might otherwise cause your PDF to overflow from one page to two, with set_auto_page_break, per py-pdf.github.io/fpdf2/Margins.html.
#Note that a cell’s height can be negative, to move it upward.