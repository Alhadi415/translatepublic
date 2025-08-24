# moamolpdf.py
import os
from pdf2image import convert_from_path

def moamolpdf(pdf_path, output_folder=None, dpi=100):
    """
    تحويل ملف PDF إلى صور بحيث تكون كل صفحة صورة منفصلة، معالجة صفحة صفحة لتقليل استهلاك الذاكرة.
    
    :param pdf_path: مسار ملف PDF
    :param output_folder: المجلد الذي سيتم حفظ الصور فيه
    :param dpi: دقة الصورة (يمكن خفضها لتقليل حجم الصورة والرام)
    """
    if output_folder is None:
        filename = os.path.splitext(os.path.basename(pdf_path))[0]
        output_folder = os.path.join("images", filename)
    os.makedirs(output_folder, exist_ok=True)

    # احصل على عدد الصفحات فقط
    from pdf2image.pdf2image import pdfinfo_from_path
    info = pdfinfo_from_path(pdf_path)
    total_pages = info["Pages"]

    for i in range(1, total_pages + 1):
        # تحويل صفحة واحدة فقط في كل مرة
        pages = convert_from_path(pdf_path, dpi=dpi, first_page=i, last_page=i)
        page_path = os.path.join(output_folder, f"page_{i}.png")
        pages[0].save(page_path, "PNG")
        del pages  # تأكد من تحرير الذاكرة بعد كل صفحة

    print(f"✅ PDF successfully converted to {total_pages} images.")
