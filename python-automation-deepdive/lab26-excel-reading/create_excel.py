import openpyxl

# Create workbook
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Data"

# Add headers
sheet["A1"] = "Name"
sheet["B1"] = "Score"
sheet["C1"] = "City"

# Add data
data = [
    ["Ali", 85, "Karachi"],
    ["Sara", 90, "Lahore"],
    ["Ahmed", 75, "Islamabad"],
    ["Zara", 88, "Peshawar"]
]

for row in data:
    sheet.append(row)

# Save file
wb.save("sample.xlsx")

print("sample.xlsx created successfully")
