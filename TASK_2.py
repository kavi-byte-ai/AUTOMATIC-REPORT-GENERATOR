import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# Step 1: Read data
df = pd.read_csv("sales_data.csv")
df["Revenue"] = df["Units Sold"] * df["Price per Unit"]

# Step 2: Analysis
total_revenue = df["Revenue"].sum()
average_daily_sales = df.groupby("Date")["Revenue"].sum().mean()
top_product = df.groupby("Product")["Revenue"].sum().idxmax()

# Step 3: Plot Revenue by Product
product_revenue = df.groupby("Product")["Revenue"].sum()
plt.figure(figsize=(6,4))
product_revenue.plot(kind='bar', color='skyblue')
plt.title("Total Revenue by Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_chart.png")
plt.close()

# Step 4: Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Sales Analysis Report", ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.ln(10)
pdf.cell(200, 10, f"Date Generated: {datetime.now().strftime('%Y-%m-%d')}", ln=True)
pdf.ln(5)
pdf.cell(200, 10, f"Total Revenue: INR {total_revenue:,.2f}", ln=True)
pdf.cell(200, 10, f"Average Daily Sales: INR {average_daily_sales:,.2f}", ln=True)

pdf.cell(200, 10, f"Top Selling Product: {top_product}", ln=True)

# Add chart
pdf.ln(10)
pdf.image("revenue_chart.png", x=10, y=80, w=180)

# Save report
pdf.output("Sales_Report.pdf")

print("✅ Advanced PDF Sales Report created.")
