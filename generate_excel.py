from openpyxl import Workbook
from datetime import datetime

# Create a workbook and worksheet
wb = Workbook()
ws = wb.active
ws.title = "MasterData"

# Header columns
headers = [
    "Asset ID", "Asset Name", "Asset Type", "Model", "Serial Number",
    "Installation Date", "Working Condition", "Installation Status",
    "Location", "Warranty Expiry", "Vendor", "Last Updated", "Updated By",
    "Location Image URL", "Remarks"
]

ws.append(headers)

# Optional: sample row
sample_row = [
    "ASSET001", "Router", "Networking", "RTX100", "SN123456789",
    "2023-01-15", "Working", "Installed", "Chennai ICCC Room 3",
    "2026-01-14", "Cisco", datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "admin@kpl.com", "images/router_room3.jpg", "Initial setup complete"
]

ws.append(sample_row)

# Save file
wb.save("master_data.xlsx")
print("master_data.xlsx created successfully.")
