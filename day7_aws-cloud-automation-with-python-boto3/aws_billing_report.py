import boto3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime, timedelta

# AWS Configuration
AWS_REGION = "us-east-1"  # Change as needed
COST_EXPLORER_CLIENT = boto3.client("ce", region_name=AWS_REGION)

# Time Range (Last 7 Days)
END_DATE = datetime.utcnow().date()
START_DATE = END_DATE - timedelta(days=7)

def get_billing_data():
    """Fetch AWS billing data from Cost Explorer."""
    print("📊 Fetching AWS cost data...")

    try:
        response = COST_EXPLORER_CLIENT.get_cost_and_usage(
            TimePeriod={"Start": START_DATE.strftime("%Y-%m-%d"), "End": END_DATE.strftime("%Y-%m-%d")},
            Granularity="DAILY",
            Metrics=["UnblendedCost"]
        )
        cost_data = response["ResultsByTime"]
        return cost_data

    except Exception as e:
        print(f"❌ Failed to fetch billing data: {e}")
        return []

def generate_pdf_report(cost_data):
    """Generates a PDF report from billing data."""
    report_filename = f"AWS_Cost_Report_{END_DATE}.pdf"
    print(f"📄 Generating PDF report: {report_filename}")

    c = canvas.Canvas(report_filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "AWS Billing Report")
    c.setFont("Helvetica", 12)
    c.drawString(200, 730, f"Time Period: {START_DATE} - {END_DATE}")

    y_position = 700
    total_cost = 0

    for entry in cost_data:
        date = entry["TimePeriod"]["Start"]
        cost = float(entry["Total"]["UnblendedCost"]["Amount"])
        total_cost += cost
        c.drawString(100, y_position, f"{date}: ${cost:.2f}")
        y_position -= 20

    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, y_position - 20, f"Total AWS Cost: ${total_cost:.2f}")

    c.save()
    print(f"✅ PDF report saved as {report_filename}")

if __name__ == "__main__":
    cost_data = get_billing_data()
    if cost_data:
        generate_pdf_report(cost_data)