from flask import Flask, jsonify,render_template
from models import *
import os
import fitz
from flask import send_file,abort


PDF_DIR = "pdfs"
CACHE_DIR = "page_cache"
PREFETCH_PAGES = 3
DPI = 150

def render_page(pdf_path, output_path, page_no):
    print("pdf_path value:", pdf_path)
    print("Is absolute?", os.path.isabs(pdf_path))
    print("Exists?", os.path.exists(pdf_path))
    doc = fitz.open(pdf_path)
    if page_no < 1 or page_no > len(doc):
        return False

    page = doc[page_no - 1]
    pix = page.get_pixmap(dpi=DPI)
    pix.save(output_path)
    return True


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/api/pdf/<doc_id>/page/<int:page_no>")
def serve_page(doc_id,page_no):
    pdf=PDF.query.filter_by(id=doc_id).first()
    print(pdf.file_path)
    if not pdf:
        abort(404, description="PDF not found")
        print("PDF not found")
    pdf_path = os.path.join(PDF_DIR, pdf.file_path)
    if not pdf_path :
        abort(404,description="PDF file not found on server")
        print("PDF file not found on server")
    doc_cache_dir=os.path.join(CACHE_DIR,str(doc_id))
    os.makedirs(doc_cache_dir,exist_ok=True)
    page_img=os.path.join(doc_cache_dir,f"page_{page_no}.png")
    
    if os.path.exists(page_img):
        return send_file(page_img,mimetype="image/png")
    
    ok=render_page(pdf_path,page_img,page_no)
    if not ok:
        abort(404,description="Page number out of range")   
        print("Page number out of range")
    for i in range(1,PREFETCH_PAGES+1):
        next_page=page_no+i
        next_img=os.path.join(doc_cache_dir,f"page_{next_page}.png")
        if not os.path.exists(next_img):
            render_page(pdf_path,next_img,next_page)
    return send_file(page_img,mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)

    
    