from openpyxl import Workbook
from openpyxl.styles import Font, Border, Side
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

# Save to the same file path (overwrites if it exists)
workbook.save(file_path)

print("Excel file 'sample_excel.xlsx' created successfully.")
