import pandas as pd
from datetime import datetime 

file_path = "iaea_dataset.xlsx"

df = pd.read_excel(file_path)

def process_col(name):
    return " ".join([word.capitalize() for word in name.split("_")]) 

df = (
    df.drop(['Unnamed: 0'], axis=1)
    .query('name != "unauthorized"')
    .rename(process_col, axis="columns")
    .rename(columns={
        "Design Net Capacity": "Design Net Capacity (MWe)",
        "Electricity Supplied": "Electricity Supplied (TWh)",
        "Reference Unit Power": "Reference Unit Power (MWe)",
        "Gross Capacity": "Gross Capacity (MWe)",
        "Thermal Capacity": "Thermal Capacity (MWt)",
        "First Grid Connection": "First Grid Connection Date"
    })
    .applymap(lambda x: "None" if x == "Missing ID" or pd.isna(x) or x == "NC" else x)
)

df["Electricity Supplied (TWh)"] = df["Electricity Supplied (TWh)"].map(lambda x: "None" if x == "None" else x.split(" ")[0])

def process_percentage(value):
    return "None" if value == "None" else float(value.split(" ")[0])/100

df["Load Factor"] = df["Load Factor"].map(process_percentage)
df["Operation Factor"] = df["Operation Factor"].map(process_percentage)
df["Energy Availability Factor"] = df["Energy Availability Factor"].map(process_percentage)

def process_date(date):
    return date if date == "None" else datetime.strptime(date, "%d %b, %Y")

df["Construction Start Date"] = df["Construction Start Date"].map(process_date)
df["First Criticality Date"] = df["First Criticality Date"].map(process_date)
df["First Grid Connection Date"] = df["First Grid Connection Date"].map(process_date)
df["Longterm Shutdown Date"] = df["Longterm Shutdown Date"].map(process_date)
df["Restart Date"] = df["Restart Date"].map(process_date)
df["Permanent Shutdown Date"] = df["Permanent Shutdown Date"].map(process_date)
df["Commercial Operation Date"] = df["Commercial Operation Date"].map(process_date)

df.to_csv("iaea_dataset_processed.csv")