import base64
import os

def get_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Highly optimized template with multiple PDF export options
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Project Report - Minimalist Notes Application</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <!-- PDF Libraries -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    
    <style>
        @font-face {{
            font-family: 'Aptos';
            src: local('Aptos'), local('Segoe UI'), local('Inter'), local('system-ui');
        }}

        :root {{
            --primary-blue: #2563eb;
            --text-main: #1e293b;
            --text-muted: #64748b;
        }}

        body {{
            background-color: #f1f5f9;
            font-family: 'Aptos', 'Segoe UI', 'Inter', sans-serif;
            font-size: 11pt;
            color: var(--text-main);
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }}

        #reportContent {{
            background: white;
            width: 210mm;
            margin: 0 auto;
            padding: 30mm 20mm;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }}

        section {{ margin-bottom: 40px; }}
        h2 {{ font-size: 1.8rem; color: #0f172a; border-bottom: 2px solid var(--primary-blue); padding-bottom: 10px; margin-top: 50px; margin-bottom: 25px; }}
        h2:first-of-type {{ margin-top: 0; }}

        #controls {{
            position: fixed;
            top: 20px;
            right: 20px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            z-index: 1000;
        }}

        .btn-status {{
            background: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 0.85rem;
            border-left: 4px solid var(--primary-blue);
            margin-bottom: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }}

        .btn-action {{
            padding: 14px 24px;
            border-radius: 50px;
            font-weight: 600;
            border: none;
            cursor: pointer;
            transition: all 0.3s;
            text-decoration: none;
            text-align: center;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }}

        .btn-overleaf {{ background-color: #059669; color: white; }}
        .btn-fast {{ background-color: var(--primary-blue); color: white; }}
        
        .btn-action:hover {{
            transform: translateY(-2px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            opacity: 0.95;
            color: white;
        }}

        .figure {{ text-align: center; margin: 30px 0; }}
        .screenshot {{ width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; }}

        @media print {{
            #controls {{ display: none !important; }}
            #reportContent {{ width: 100%; margin: 0; padding: 0; box-shadow: none; }}
            h2 {{ page-break-before: always; }}
        }}
    </style>
</head>
<body>

    <div id="controls" class="no-print">
        <div class="btn-status">
            <strong>Lab Submission Mode:</strong> Use Overleaf for the absolute highest quality PDF.
        </div>
        
        <!-- Overleaf "Direct Open" Button -->
        <a href="https://www.overleaf.com/docs?snip_uri=https://raw.githubusercontent.com/AtharvaMaik/DjangoNotes/jazzyfucnts/report.tex" 
           target="_blank" class="btn-action btn-overleaf">
            1. Open in Overleaf (High Quality PDF)
        </a>

        <!-- Fast Internal Export (JS Fix) -->
        <button id="dlBtn" onclick="generatePDF()" class="btn-action btn-fast">
            2. Fast Export PDF (Internal Fix)
        </button>

        <p style="font-size: 10px; color: var(--text-muted); text-align: center; margin-top: 10px;">
           *Note: In Overleaf, simply upload your 3 screenshots<br>to the project to finish the build.
        </p>
    </div>

    <div id="reportContent">
        <div style="text-align: center; height: 1000px; display: flex; flex-direction: column; justify-content: center; padding-bottom: 200px;">
            <h1 style="font-family: 'Playfair Display', serif; font-size: 4rem; margin-bottom: 10px;">Minimalist Notes App</h1>
            <p style="text-transform: uppercase; letter-spacing: 2px; color: #64748b; margin-bottom: 60px;">Final Project Report | Web Programming Lab</p>
            
            <img src="data:image/png;base64,{main_app_b64}" alt="Hero Image" style="width: 80%; max-width: 500px; margin: 0 auto 60px auto; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
            
            <div style="border-top: 1px solid #e2e8f0; padding-top: 40px; font-size: 1.2rem;">
                <p>SUBMITTED BY:</p>
                <p style="font-weight: 600; color: var(--primary-blue); margin: 5px 0;">Atharva Maikhuri (235816206)</p>
                <p style="font-weight: 600; color: var(--primary-blue); margin: 5px 0;">Harshita Gaurav (235816036)</p>
            </div>
            
            <div style="margin-top: 100px; color: #64748b;">
                <p>APRIL 14, 2026</p>
                <p style="font-size: 0.9rem;">DEPARTMENT OF COMPUTER APPLICATIONS</p>
            </div>
        </div>

        <section>
            <h2>1. Project Objective and Scope</h2>
            <p>The core objective of this project is to develop a lightweight, user-friendly, and highly interactive Note-Taking web application. It serves as a comprehensive demonstration of Full-Stack development concepts.</p>
        </section>

        <!-- (All sections from before) -->
        <section>
            <h2>2. Scalability and Efficiency</h2>
            <div class="figure">
                <img src="data:image/png;base64,{main_app_b64}" class="screenshot" alt="Main Dashboard">
                <p style="font-style: italic; font-size: 0.9rem; margin-top: 10px;">Figure 1.0: All metrics are updated in real-time via background AJAX tasks.</p>
            </div>
        </section>

        <section>
            <h2>3. Security and Input Integrity</h2>
            <div class="figure">
                <img src="data:image/png;base64,{validation_b64}" class="screenshot" alt="Validation Error">
                <p style="font-style: italic; font-size: 0.9rem; margin-top: 10px;">Figure 2.0: Integrated validation logic preventing invalid entries.</p>
            </div>
        </section>

        <section>
            <h2>4. Dynamic Modals & Maintenance</h2>
            <div class="figure">
                <img src="data:image/png;base64,{edit_modal_b64}" class="screenshot" alt="Edit Modal">
                <p style="font-style: italic; font-size: 0.9rem; margin-top: 10px;">Figure 3.0: High-focus editing environment powered by Bootstrap 5.</p>
            </div>
        </section>

        <section id="conclusion">
            <h2>Conclusion</h2>
            <p>The Minimalist Notes Application successfully fulfills all requirements. By bridging Python strengths with JavaScript agility, we have produced a functional, high-end web application.</p>
        </section>
    </div>

    <script>
        function generatePDF() {{
            const btn = document.getElementById('dlBtn');
            const element = document.getElementById('reportContent');
            
            btn.disabled = true;
            btn.innerText = 'Initializing...';

            const opt = {{
                margin: [10, 0, 10, 0],
                filename: 'Notes_App_Report_Final.pdf',
                image: {{ type: 'jpeg', quality: 0.98 }},
                html2canvas: {{ scale: 2, useCORS: true }},
                jsPDF: {{ unit: 'mm', format: 'a4', orientation: 'portrait' }},
                pagebreak: {{ mode: ['css', 'legacy'] }}
            }};

            // Ensure H2s start on new pages
            element.querySelectorAll('h2').forEach((h, i) => {{
                if (i > 0) h.style.pageBreakBefore = 'always';
            }});

            // Explicitly force blob download as PDF
            html2pdf().set(opt).from(element).toPdf().get('pdf').then(function (pdf) {{
                const totalPages = pdf.internal.getNumberOfPages();
                console.log("PDF Created with " + totalPages + " pages.");
                
                // Final save trigger to ensure browser understands it's a PDF
                pdf.save('Final_Project_Report.pdf');
                
                btn.disabled = false;
                btn.innerText = 'Fast Export PDF (Internal Fix)';
            }});
        }}
    </script>
</body>
</html>
"""

# Embed images
main_app = get_base64("c:/AISH20/WP PROJECT/main_app.png")
edit_modal = get_base64("c:/AISH20/WP PROJECT/edit_modal.png")
validation = get_base64("c:/AISH20/WP PROJECT/validation_error.png")

final_html = html_template.format(
    main_app_b64=main_app,
    edit_modal_b64=edit_modal,
    validation_b64=validation
)

with open("c:/AISH20/WP PROJECT/report.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Report updated with Overleaf 1-Click integration!")
