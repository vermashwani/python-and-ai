from openpyxl import Workbook
from openpyxl.styles import Font, Border, Side
from openpyxl.chart import BarChart, Reference
import os

file_path = "sample_excel.xlsx"

# Optional: Delete the existing file first (not strictly necessary)
if os.path.exists(file_path):
    os.remove(file_path)

# Create a new workbook and select the active worksheet
workbook = Workbook()
sheet = workbook.active

# Rename the sheet
sheet.title = "SampleData"

# Add some sample data
sheet['A1'] = "Name"
sheet['B1'] = "Age"
sheet['C1'] = "Gender"
sheet['A2'] = "Alice"
sheet['B2'] = 30
sheet['C2'] = "Female"
sheet['A3'] = "Bob"
sheet['B3'] = 25
sheet['C3'] = "Male"

# Apply bold and underline style
bold_underline_font = Font(bold=True, underline="single")
sheet['A1'].font = bold_underline_font
sheet['B1'].font = bold_underline_font
sheet['C1'].font = bold_underline_font

# Add borders to all cells in the range A1:C3
thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

for row in sheet['A1:C3']:
    for cell in row:
        cell.border = thin_border

# Add student marks and grades table in E1:G5
students = [
    ("John", 85, "A"),
    ("Sara", 78, "B"),
    ("Mike", 92, "A"),
    ("Lily", 67, "C"),
]

sheet['E1'] = "Student"
sheet['F1'] = "Marks"
sheet['G1'] = "Grade"
for col in ['E', 'F', 'G']:
    sheet[f"{col}1"].font = bold_underline_font
    sheet[f"{col}1"].border = thin_border

for i, (name, marks, grade) in enumerate(students, start=2):
    sheet[f"E{i}"] = name
    sheet[f"F{i}"] = marks
    sheet[f"G{i}"] = grade
    sheet[f"E{i}"].border = thin_border
    sheet[f"F{i}"].border = thin_border
    sheet[f"G{i}"].border = thin_border

# Create a bar chart for marks
chart = BarChart()
data = Reference(sheet, min_col=6, min_row=1, max_row=5)  # F1:F5
categories = Reference(sheet, min_col=5, min_row=2, max_row=5)  # E2:E5
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)
chart.title = "Student Marks"
chart.x_axis.title = "Student"
chart.y_axis.title = "Marks"

sheet.add_chart(chart, "E7")

# Save to the same file path (overwrites if it exists)
workbook.save(file_path)

print("Excel file 'sample_excel.xlsx' created successsully.")