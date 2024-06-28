from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(trends):
    c = canvas.Canvas("trends_report.pdf", pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 14)
    c.drawString(30, height - 40, "Trending Topics Report")

    c.setFont("Helvetica", 12)
    y = height - 60
    for trend in trends:
        c.drawString(30, y, f"{trend['name']}: {trend['url']}")
        y -= 20
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()
