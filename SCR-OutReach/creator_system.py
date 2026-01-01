# File description
# Author: BlackLove4u

"""
CREATOR BUSINESS SYSTEM — MASTER FILE
====================================

WHAT THIS SCRIPT DOES:
- Creates a structured multi-sheet Excel (.xlsx) database
- Acts as a coded version of your creator business framework
- Is designed to be EXPANDED every time we add new systems

REQUIREMENTS:
- Python 3.9+
- openpyxl library

HOW TO RUN (SUMMARY):
1. Install Python
2. Install openpyxl
3. Run: python creator_system.py
4. Open the generated Excel file

DO NOT DELETE THIS FILE.
This is your long-term operating system.
"""

from openpyxl import Workbook


# -----------------------------
# CORE UTILITY FUNCTIONS
# -----------------------------

def create_workbook():
    """Initializes the Excel workbook."""
    wb = Workbook()
    default = wb.active
    wb.remove(default)
    return wb


def add_sheet(wb, title, rows):
    """
    Adds a new sheet with rows.
    - wb: workbook object
    - title: sheet name
    - rows: list of lists (each list = one row)
    """
    ws = wb.create_sheet(title=title)
    for row in rows:
        ws.append(row)


# -----------------------------
# SYSTEM MODULES (DATABASES)
# -----------------------------

def source_context_module(wb):
    add_sheet(wb, "Source_Video_Context", [
        ["Field", "Value"],
        ["Primary Source", "How Creators Actually Make Money"],
        ["YouTube Link", "https://m.youtube.com/watch?v=VN_0zJXBO6E"],
        ["Core Insight", "Millions of views ≠ millions of dollars"],
        ["Positioning Rule", "Niche + buyer intent > entertainment"],
        ["Target Advantage", "Small, high-trust audiences monetize better"],
    ])


def income_streams_module(wb):
    add_sheet(wb, "Income_Streams_Map", [
        ["Stream", "Barrier", "Month 1", "Month 3", "Month 6", "Notes"],
        ["Sponsored Posts", "Low", "Yes", "Yes", "Yes", "Pitch aligned brands"],
        ["Local Brand Collabs", "Very Low", "Yes", "Yes", "Yes", "Cash + savings"],
        ["UGC Creation", "Low", "Yes", "Yes", "Yes", "No audience needed"],
        ["Affiliate Marketing", "Low", "Seed", "Grow", "Compound", "Scales well"],
        ["Creator Services", "Low", "Yes", "Yes", "Yes", "Behind-the-scenes"],
        ["Digital Products", "Medium", "Plan", "Launch", "Scale", "High margin"],
        ["Memberships", "Medium", "Seed", "Launch", "Stabilize", "Recurring"],
        ["Ad Revenue", "Medium", "Build", "Qualify", "Compound", "Evergreen"],
        ["Venture Capital", "High", "Prep", "Signals", "Pitch", "Future stage"],
    ])


def month_1_module(wb):
    add_sheet(wb, "Month_1_Foundation", [
        ["Focus", "Action", "Output", "Income Range"],
        ["Niche Lock-in", "Define buyer-focused niche", "Clarity", "$0"],
        ["Content Setup", "Create 15–30 short videos", "Portfolio", "$0"],
        ["UGC Portfolio", "Mock ads w/ owned products", "UGC page", "$500–$2,000"],
        ["Local Outreach", "Pitch 20 local businesses", "Deals", "$300–$800"],
        ["Affiliate Seeding", "Join 3–5 programs", "Links", "$50–$300"],
        ["Service Offer", "List 1 skill", "Clients", "$500–$1,500"],
    ])


def month_3_module(wb):
    add_sheet(wb, "Month_3_Growth", [
        ["Focus", "Action", "Output", "Income Range"],
        ["Brand Pitching", "Email CMOs", "Sponsors", "$1,500–$5,000"],
        ["UGC Scaling", "Join platforms", "Repeat clients", "$2,000–$6,000"],
        ["Ads Testing", "Low-budget tests", "Leads", "ROI-positive"],
        ["Affiliate Focus", "High-ticket content", "Sales", "$500–$3,000"],
        ["Digital Product", "Launch mini-offer", "Sales page", "$1,000–$4,000"],
    ])


def month_6_module(wb):
    add_sheet(wb, "Month_6_Scale", [
        ["Focus", "Action", "Output", "Income Range"],
        ["Authority", "Publish case studies", "Trust", "$0"],
        ["Sponsors", "Retainer deals", "Predictable income", "$5k–$15k"],
        ["UGC Packages", "Bundles + licensing", "Higher AOV", "$4k–$10k"],
        ["Membership", "Launch Patreon", "MRR", "$2k–$8k"],
        ["Products", "Courses/templates", "Scalable sales", "$5k–$25k"],
    ])


def brand_trust_module(wb):
    add_sheet(wb, "Brand_Trust_Framework", [
        ["Signal", "How to Demonstrate"],
        ["Clarity", "Clear niche & audience"],
        ["Proof", "Stats, testimonials"],
        ["Consistency", "Weekly posting"],
        ["Ease", "Professional communication"],
        ["ROI Thinking", "Conversion-focused ideas"],
    ])


def finance_module(wb):
    add_sheet(wb, "Financial_Trajectory", [
        ["Phase", "Revenue", "Expenses", "Net"],
        ["Month 1", "$1k–$3k", "$200–$500", "Positive"],
        ["Month 3", "$5k–$12k", "$1k–$3k", "Strong"],
        ["Month 6", "$15k–$40k", "$5k–$10k", "Scalable"],
    ])


def mindset_module(wb):
    add_sheet(wb, "Founder_Mindset_Ops", [
        ["Area", "Principle"],
        ["Mindset", "Think like a media company"],
        ["Workload", "Systems before scale"],
        ["Development", "Test → Measure → Iterate"],
        ["Negotiation", "Value over followers"],
        ["Future", "Assets > virality"],
    ])


# -----------------------------
# MAIN EXECUTION
# -----------------------------

def main():
    wb = create_workbook()

    # Core system build
    source_context_module(wb)
    income_streams_module(wb)
    month_1_module(wb)
    month_3_module(wb)
    month_6_module(wb)
    brand_trust_module(wb)
    finance_module(wb)
    mindset_module(wb)

    # Save output
    file_name = "Creator_Business_System.xlsx"
    wb.save(file_name)

    print(f"SUCCESS: {file_name} created.")


if __name__ == "__main__":
    main()