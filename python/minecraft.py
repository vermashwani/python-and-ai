from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(30, 30, 100)
        self.cell(0, 10, "📘 Class 10 CBSE Study Tracker", ln=True, align="C")
        self.set_font("Helvetica", "I", 10)
        self.set_text_color(90, 90, 90)
        self.cell(0, 10, "“Success is the sum of small efforts, repeated day in and day out.”", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, "© 2025 CBSE Planner | Made by You", 0, 0, "C")

    def add_month(self, month, subjects):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, f"📅 {month}", ln=True)
        self.ln(2)

        for subject, topics in subjects.items():
            self.set_font("Helvetica", "B", 11)
            self.set_text_color(40, 70, 130)
            self.cell(0, 8, f"🔹 {subject}", ln=True)
            self.set_font("Helvetica", "", 10)
            self.set_text_color(0, 0, 0)
            for topic in topics:
                self.cell(5)
                self.cell(0, 6, f"[ ] {topic}", ln=True)
            self.ln(2)
        self.ln(3)

# Sample plan for 2 months
study_plan = {
    "JULY": {
        "Maths": ["Real Numbers", "Polynomials", "Linear Equations"],
        "Science": ["Physics: Light – Part 1", "Chemistry: Chemical Reactions", "Biology: Life Processes"],
        "Hindi B": ["पद", "राम-लक्ष्मण संवाद", "हरिहर काका"]
    },
    "AUGUST": {
        "Maths": ["Quadratic Equations", "AP", "Triangles"],
        "Science": ["Electricity", "Acids & Bases", "Control & Coordination"],
        "Hindi B": ["तत् समय...", "मीरा के पद", "सपनों के-से दिन"]
    }
}

pdf = PDF()
pdf.add_page()

for month, subjects in study_plan.items():
    pdf.add_month(month, subjects)

pdf.output("Class_10_CBSE_Study_Tracker.pdf")
print("✅ PDF successfully created!")
