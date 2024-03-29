import io 
import pdfrw
from reportlab.pdfgen import canvas

def run():
    canvas_data = get_overlay_canvas()
    form = merge(canvas_data, template_path='./template.pdf')
    save(form, filename='merged.pdf')
    def get_overlay_canvas() -> io.BytesIO:
        data = io.BytesIO()
        pdf = canvas.Canvas(data)
        pdf.drawString(x=33, y=550, text='Willis')
        pdf.drawString(x=148, y=550, text='John')
        pdf.save()
        data.seek(0)
        return data
    def merge(overlay_canvas: io.BytesIO, template_path: str) -> io.BytesIO:
        template_pdf = pdfrw.PdfReader(template_path)
        overlay_pdf = pdfrw.PdfReader(overlay_canvas)
        for page, data in zip(template_pdf.pages, overlay_pdf.pages):
            overlay = pdfrw.PageMerge().add(data)[0]
            pdfrw.PageMerge(page).add(overlay).render()
            form = io.BytesIO()
            pdfrw.PdfWriter().write(form, template_pdf)
        form.seek(0)
        return form

    def save(form: io.BytesIO, filename: str):
        with open(filename, 'wb') as f:
            f.write(form.read())
            
run()