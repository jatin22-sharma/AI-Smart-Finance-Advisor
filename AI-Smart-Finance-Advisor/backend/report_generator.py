from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.pagesizes import letter

import os

# ==========================================
# GENERATE PDF REPORT
# ==========================================

def generate_financial_report(

    income,
    total_expense,
    savings,
    savings_rate,
    suggestions

):

    # Create reports folder if missing

    os.makedirs(
        "reports",
        exist_ok=True
    )

    # PDF path

    pdf_path = "reports/financial_report.pdf"

    # Create document

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # ==========================================
    # TITLE
    # ==========================================

    title = Paragraph(
        "AI Smart Finance Advisor Report",
        styles['Title']
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    # ==========================================
    # FINANCIAL SUMMARY
    # ==========================================

    summary = f"""
    <b>Monthly Income:</b> ₹{income:,.2f}<br/><br/>

    <b>Total Expense:</b> ₹{total_expense:,.2f}<br/><br/>

    <b>Total Savings:</b> ₹{savings:,.2f}<br/><br/>

    <b>Savings Rate:</b> {savings_rate:.2f}%<br/><br/>
    """

    elements.append(
        Paragraph(summary, styles['BodyText'])
    )

    elements.append(
        Spacer(1, 20)
    )

    # ==========================================
    # AI SUGGESTIONS
    # ==========================================

    suggestion_title = Paragraph(
        "AI Financial Suggestions",
        styles['Heading2']
    )

    elements.append(
        suggestion_title
    )

    elements.append(
        Spacer(1, 10)
    )

    for s in suggestions:

        elements.append(
            Paragraph(f"• {s}", styles['BodyText'])
        )

        elements.append(
            Spacer(1, 5)
        )

    # ==========================================
    # BUILD PDF
    # ==========================================

    doc.build(elements)

    return pdf_path