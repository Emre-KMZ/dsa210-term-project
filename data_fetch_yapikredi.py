
""" 
since yapikredi webapp does not provide (it actually should but its not working properly right now) provide a formatted data export,
I will download my data as PDF and extract the data from the PDF file then save it as a csv file.
"""


import pdfplumber
import re
import os
import csv

months = {
    "Ocak": 0,
    "Şubat": 31,
    "Mart": 59,
    "Nisan": 90,
    "Mayıs": 120,
    "Haziran": 151,
    "Temmuz": 181,
    "Ağustos": 212,
    "Eylül": 243,
    "Ekim": 273,
    "Kasım": 304,
    "Aralık": 334
}

def extract_spending_data(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages)

    # normalize the text (removing extra spaces, fixing formatting)
    text = re.sub(r"\\s+", " ", text) 

    # print(text)

    # regex pattern to extract the spending data: format is "dd MMMM yyyy description amount"
    # spending_pattern = r"\b\d{1,2}\s+(?:Ocak|Şubat|Mart|Nisan|Mayıs|Haziran|Temmuz|Ağustos|Eylül|Ekim|Kasım|Aralık)\s+\d{4}\s+[A-Za-zÇŞĞİÖÜçşğıöü\s]+\s+\d+,\d{2}\b"
    spending_pattern = r"(\d{1,2})\s+(Ocak|Şubat|Mart|Nisan|Mayıs|Haziran|Temmuz|Ağustos|Eylül|Ekim|Kasım|Aralık)\s+(\d{4})\s+([A-Za-zİıĞğÜüŞşÖöÇç0-9\s\.-]+)\s+TR\s+(\d{1,3}(?:\.\d{3})*,\d{2})"

    matches = re.findall(spending_pattern, text)

    spending_data = []
    for match in matches:
        day = match[0]
        month = match[1]
        year = match[2]
        description = match[3]
        amount = match[4]
        no_day_of_2024 = months[month] + int(day)

        


        spending_data.append({
            "date": no_day_of_2024,
            "description": description,
            "amount": float(amount.replace(".", "").replace(",", "."))
        })

    

    return spending_data

def clean_data(data):
    # remove the data if name contains "V.D." since those are my taxes :)
    # remove the data if name contains "AJET" since those are flight tickets, that are not relevant for the analysis and also refunded
    data = [item for item in data if "V.D." not in item["description"] and "AJET" not in item["description"]]

    return data


if __name__ == "__main__":

    # for every file in the ./data/yapıkredi folder, extract the spending data, and save all the data in a single csv file
    data_folder = "./data/yapikredi_unformatted"
    output_folder = "./data/yapikredi_formatted"

    data = []


    for file in os.listdir(data_folder): # for each file in the data folder
        pdf_path = os.path.join(data_folder, file)
        spending_data = extract_spending_data(pdf_path) # extract the spending data from the pdf file
        data.extend(spending_data)

    data = sorted(data, key=lambda x: x["date"]) # sort the data by date for easier analysis

    data = clean_data(data)

    output_path = os.path.join(output_folder, "yapikredi_spending_data.csv")

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "description", "amount"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Extracted {len(data)} spending entries from {len(os.listdir(data_folder))} PDF files.")

