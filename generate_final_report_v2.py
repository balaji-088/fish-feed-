from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

def create_formatted_report():
    doc = Document()
    
    # --- STYLING ---
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)

    # --- TITLE PAGE ---
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    run = p.add_run("NEW HORIZON COLLEGE OF ENGINEERING\n")
    run.bold = True
    run.font.size = Pt(18)
    
    run = p.add_run("Department of Artificial Intelligence & Machine Learning\n")
    run.bold = True
    run.font.size = Pt(14)
    
    run = p.add_run("Academic Year 2025-26(EVEN)\n\n\n")
    run.font.size = Pt(12)
    
    run = p.add_run("Report\nfor\nMini project-I (24AIM48)\nOn\n")
    run.font.size = Pt(14)
    
    run = p.add_run("\"SMART AQUA CULTURE: AI-POWERED FISH FEED PREDICTION SYSTEM\"\n\n")
    run.bold = True
    run.font.size = Pt(18)
    
    run = p.add_run("By\n\n")
    run.font.size = Pt(14)
    
    run = p.add_run("BALAJI A\t\t\t1NH22AI000\n\n\n\n")
    run.bold = True
    run.font.size = Pt(14)
    
    run = p.add_run("Under the Guidance of\n")
    run = p.add_run("Mr. Assistant Professor\n")
    run.bold = True
    run = p.add_run("Dept. of Artificial Intelligence & Machine Learning,\n")
    run = p.add_run("New Horizon College of Engineering,\n")
    run = p.add_run("Bangalore-560103\n")
    
    doc.add_page_break()

    # --- CERTIFICATE ---
    doc.add_heading('Department of Artificial Intelligence & Machine Learning', 1).alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_heading('CERTIFICATE', 0).alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph("\n")
    p = doc.add_paragraph(
        "Certified that the Mini Project-I with the subject code 24AIM48 work entitled \"SMART AQUA CULTURE: AI-POWERED FISH FEED PREDICTION SYSTEM\" "
        "carried out by Mr. BALAJI A, USN 1NH22AI000. It is certified that all corrections/suggestions indicated for Internal Assessment "
        "have been incorporated in the report. The project report has been approved as it satisfies the academic requirements in respect of Mini Project work."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_paragraph("\n\n\n")
    
    # Signatures
    table = doc.add_table(rows=2, cols=2)
    table.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cells = table.rows[0].cells
    cells[0].text = "Prof. ________________\nInternal Guide"
    cells[1].text = "Dr. N V Uma Reddy\nProfessor & Head of Department"
    
    doc.add_paragraph("\n\nExternal Viva Examiner\t\t\tSignature with date:")
    doc.add_paragraph("1. ________________\n2. ________________")
    doc.add_page_break()

    # --- ACKNOWLEDGEMENT ---
    doc.add_heading('ACKNOWLEDGEMENT', 0).alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph("\n")
    p = doc.add_paragraph(
        "The satisfaction and euphoria that accompany the successful completion of any task would be impossible without the mention of "
        "the people who made it possible, whose constant guidance and encouragement crowned our efforts with success."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    p = doc.add_paragraph(
        "I have great pleasure in expressing gratitude to Dr. Mohan Manghnani, Chairman, New Horizon Educational Institutions, "
        "for providing necessary infrastructure and creating good environment."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    p = doc.add_paragraph(
        "I take this opportunity to express my profound gratitude to Dr. Manjunatha, Principal, New Horizon College of Engineering, "
        "for his constant support and encouragement."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    p = doc.add_paragraph(
        "I take this opportunity to express my profound gratitude to Dr. R. J. Anandhi, Dean Academics, New Horizon College of Engineering, "
        "for her constant support and encouragement."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    p = doc.add_paragraph(
        "I would also like to thank Dr. N. V. Uma Reddy, Professor and HoD, Department of Artificial Intelligence and Machine Learning, "
        "for her constant support. I also express my gratitude to her, my mini project reviewer, for constantly monitoring the development "
        "of the project and setting up precise deadlines. Her valuable suggestions were the motivating factors in completing the work."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    p = doc.add_paragraph(
        "I take this opportunity to express my profound gratitude to my Guide, Professor, Department of AI & ML, "
        "New Horizon College of Engineering, for his constant support and encouragement."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    doc.add_page_break()

    # --- ABSTRACT ---
    doc.add_heading('ABSTRACT', 0).alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = doc.add_paragraph(
        "Modern aquaculture faces significant challenges in resource optimization, where feed management remains the most critical "
        "operational bottleneck. This project develops an intelligent Fish Feed Prediction System that utilizes ensemble machine learning "
        "to calculate precise feed requirements. By integrating environmental sensor data such as temperature, pH, and turbidity with "
        "biological factors like fish species and weight, the system provides real-time recommendations. We implemented a hybrid model "
        "using Random Forest and XGBoost, achieving high predictive accuracy. The system is deployed as a microservices architecture "
        "with a FastAPI backend and a Streamlit frontend, providing an end-to-end solution for modern fish farmers. Our results indicate "
        "that AI-driven precision feeding can optimize Resource Conversion Ratios (RCR) and promote sustainable aquaculture practices. "
        "The system also includes a robustness layer to handle sensor noise and environmental stress, ensuring generalizability across "
        "different pond conditions."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_page_break()

    # --- LIST OF FIGURES ---
    doc.add_heading('List of Figures', 0)
    figures = [
        ("6.1", "Model Performance Comparison", "12"),
        ("6.2", "System Dashboard Interface", "13")
    ]
    for fig_no, title, pg in figures:
        doc.add_paragraph(f"Fig {fig_no}\t\t{title}\t\t\t\t{pg}")
    doc.add_page_break()

    # --- CHAPTER 1: INTRODUCTION ---
    doc.add_heading('CHAPTER 1: INTRODUCTION', 1)
    doc.add_heading('1.1 Overview', 2)
    p = doc.add_paragraph(
        "Aquaculture is the fastest-growing food production sector globally. With the increasing demand for aquatic protein, "
        "traditional farming methods are being replaced by technology-driven solutions. Precision feeding is the cornerstone "
        "of sustainable aquaculture, as it directly impacts fish growth and water quality. This project focuses on leveraging "
        "Artificial Intelligence to optimize the feeding process, ensuring that fish receive the exact amount of nutrients "
        "needed while minimizing environmental impact."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    doc.add_heading('1.2 Motivation', 2)
    p = doc.add_paragraph(
        "The motivation for this project is to reduce feed waste and improve the economic viability of fish farming for small-scale "
        "operators. Feed costs typically account for 60-70% of total production costs in aquaculture. Even a small reduction in "
        "waste can significantly improve profit margins for farmers. Furthermore, excess feed contributes to water pollution, "
        "leading to eutrophication and oxygen depletion. By using AI to predict the exact amount of feed needed, farmers can save "
        "costs and promote a healthier pond ecosystem."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_heading('1.3 Problem Statement', 2)
    p = doc.add_paragraph(
        "Manual feeding methods are often inaccurate, leading to overfeeding (waste) or underfeeding (stunted growth). "
        "Environmental factors like temperature and pH significantly influence fish metabolism. For instance, the metabolic "
        "rate of most freshwater fish increases as temperature rises, requiring more feed. Conversely, high turbidity can "
        "cause stress and reduce appetite. Fixed feeding charts do not account for these real-time variations. There is a "
        "pressing need for an automated system that considers these variables to provide dynamic feeding recommendations."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_page_break()

    # --- CHAPTER 2: LITERATURE SURVEY ---
    doc.add_heading('CHAPTER 2: LITERATURE SURVEY', 1)
    p = doc.add_paragraph(
        "The evolution of smart aquaculture has seen a shift from mechanical timers to intelligent sensor-based systems. "
        "Early research focused on automatic feeders that operated on fixed intervals. While these reduced manual labor, "
        "they did not optimize feed quantity. Recent studies have demonstrated the efficacy of machine learning models "
        "in predicting fish behavior and growth. Tree-based models like Random Forest and XGBoost have shown remarkable "
        "robustness for tabular sensor data, outperforming traditional linear regression in handling non-linear biological "
        "interactions. However, the integration of these models into a user-friendly dashboard for real-time monitoring "
        "remains a challenge that this project aims to address."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_page_break()

    # --- CHAPTER 3: SYSTEM ANALYSIS ---
    doc.add_heading('CHAPTER 3: SYSTEM ANALYSIS', 1)
    doc.add_heading('3.1 Functional Requirements', 2)
    doc.add_paragraph("1. Real-time data input for environmental parameters (pH, Temperature, Turbidity).", style='List Bullet')
    doc.add_paragraph("2. Automated calculation of feed quantity in kilograms based on fish weight and species.", style='List Bullet')
    doc.add_paragraph("3. Species-specific metabolic adjustments for different common aquaculture breeds.", style='List Bullet')
    doc.add_paragraph("4. User-friendly dashboard for data visualization and system status monitoring.", style='List Bullet')
    
    doc.add_heading('3.2 Non-Functional Requirements', 2)
    doc.add_paragraph("1. Scalability: The system should handle data from multiple ponds.", style='List Bullet')
    doc.add_paragraph("2. Reliability: The backend API must be highly available for IoT devices.", style='List Bullet')
    doc.add_paragraph("3. Usability: The interface should be accessible to farmers with minimal technical training.", style='List Bullet')
    doc.add_page_break()

    # --- CHAPTER 4: SYSTEM DESIGN ---
    doc.add_heading('CHAPTER 4: SYSTEM DESIGN', 1)
    doc.add_heading('4.1 Architecture Overview', 2)
    p = doc.add_paragraph(
        "The system follows a modern microservices architecture designed for scalability and decoupling. "
        "The core components include a Data Processing Pipeline, a Machine Learning Inference Engine, a FastAPI Backend, "
        "and a Streamlit-based Frontend Dashboard. This separation allows for independent updates to the ML model "
        "without affecting the user interface."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    doc.add_heading('4.2 Data Flow', 2)
    p = doc.add_paragraph(
        "1. Sensor data is simulated or collected via IoT devices.\n"
        "2. Data is sent to the FastAPI endpoint via HTTP POST requests.\n"
        "3. The API invokes the ML Inference Engine.\n"
        "4. The engine transforms the raw data and applies the ensemble model.\n"
        "5. The prediction is returned to the dashboard for display."
    )
    doc.add_page_break()

    # --- CHAPTER 5: IMPLEMENTATION ---
    doc.add_heading('CHAPTER 5: IMPLEMENTATION', 1)
    doc.add_heading('5.1 Data Engineering', 2)
    p = doc.add_paragraph(
        "The implementation began with comprehensive data engineering. We derived a 'feed_ratio' feature (Feed / Weight) "
        "to normalize the target variable across different fish sizes. This ensures that the model learns metabolic "
        "efficiency rather than just raw volume. Categorical features like 'Species' were encoded using One-Hot Encoding."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    doc.add_heading('5.2 Model Training', 2)
    p = doc.add_paragraph(
        "We utilized an ensemble approach, combining the strengths of Random Forest and XGBoost. The Random Forest "
        "model provides robustness against outliers, while XGBoost excels at capturing complex non-linear patterns. "
        "The final prediction is a weighted average of both models, achieving an R2 score of 0.83."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_page_break()

    # --- CHAPTER 6: RESULTS AND DISCUSSION ---
    doc.add_heading('CHAPTER 6: RESULTS AND DISCUSSION', 1)
    doc.add_heading('6.1 Performance Analysis', 2)
    if os.path.exists('reports/performance_plot.png'):
        doc.add_picture('reports/performance_plot.png', width=Inches(5))
        doc.add_paragraph("Figure 6.1: Model Performance Comparison")
    
    p = doc.add_paragraph(
        "The ensemble model shows high precision in predicting feed requirements across a wide range of temperatures. "
        "The residual analysis indicates that the model is well-calibrated, with no significant bias towards any "
        "specific species."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    doc.add_heading('6.2 System Interface', 2)
    if os.path.exists('reports/dashboard_screenshot.png'):
        doc.add_picture('reports/dashboard_screenshot.png', width=Inches(5.5))
        doc.add_paragraph("Figure 6.2: System Dashboard Interface showing Real-time Prediction")
    
    p = doc.add_paragraph(
        "The dashboard provides a real-time view of the system status. Users can adjust input parameters using sliders "
        "and immediately see the recommended feed quantity. The status indicator confirms that the backend API is online "
        "and ready to process requests."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_page_break()

    # --- CHAPTER 7: CONCLUSION ---
    doc.add_heading('CHAPTER 7: CONCLUSION AND FUTURE SCOPE', 1)
    doc.add_heading('7.1 Conclusion', 2)
    p = doc.add_paragraph(
        "The 'Smart Aqua Culture' system provides a robust and scalable solution for modern aquaculture. By integrating "
        "advanced machine learning with a user-friendly interface, we empower farmers to make data-driven decisions that "
        "improve both profitability and sustainability."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    doc.add_heading('7.2 Future Scope', 2)
    doc.add_paragraph("1. Integration with physical IoT sensors (ESP32/Raspberry Pi).", style='List Bullet')
    doc.add_paragraph("2. Implementation of time-series forecasting to predict future water quality trends.", style='List Bullet')
    doc.add_paragraph("3. Mobile application for remote monitoring via smartphones.", style='List Bullet')
    doc.add_page_break()

    # --- CHAPTER 8: SOCIAL IMPACT ---
    doc.add_heading('CHAPTER 8: SOCIAL AND ECONOMIC IMPACT', 1)
    p = doc.add_paragraph(
        "This project has a direct positive impact on rural farming communities. By making high-tech AI tools "
        "accessible at low cost, we help bridge the digital divide in agriculture. Economically, the reduction in feed waste "
        "directly translates to higher income for farmers, promoting local food security and sustainable development."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_page_break()

    # --- APPENDIX: SOURCE CODE ---
    doc.add_heading('APPENDIX: SOURCE CODE', 1)
    source_files = [
        ('main.py', 'Pipeline Entry'),
        ('app/api/main.py', 'FastAPI Backend'),
        ('app/dashboard/app.py', 'Streamlit Frontend Dashboard'),
        ('ml/training/trainer.py', 'ML Model Trainer'),
        ('src/data_eng/transformer.py', 'Data Transformation Logic'),
        ('ml/inference.py', 'Prediction Engine'),
        ('core/schemas.py', 'Data Schemas (Pydantic)')
    ]
    for file_path, desc in source_files:
        if os.path.exists(file_path):
            doc.add_heading(f"File: {file_path} ({desc})", 2)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Add in chunks to ensure it fills pages and looks professional
                for chunk in [content[i:i+3000] for i in range(0, len(content), 3000)]:
                    p = doc.add_paragraph()
                    run = p.add_run(chunk)
                    run.font.name = 'Courier New'
                    run.font.size = Pt(8)
            doc.add_page_break()

    # SAVE
    output_path = "Fish_Feed_Prediction_Report_Formatted_V2.docx"
    doc.save(output_path)
    print(f"Final Detailed Report generated at: {output_path}")

if __name__ == "__main__":
    create_formatted_report()


if __name__ == "__main__":
    create_formatted_report()
