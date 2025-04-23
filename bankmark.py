import pandas as pd
import numpy as np

def main():
    # 1. Read raw data
    bank_mark = pd.read_csv(r"data\bank_marketing.csv")

    # 2. Split into three tables
    
    # table 1: client.csv
    client = bank_mark[[
        "client_id", "age", "job", "marital",
        "education", "credit_default", "mortgage"
    ]].copy()

    # table 2: campaign.csv
    campaign = bank_mark[[
        "client_id", "number_contacts", "month", "day",
        "contact_duration", "previous_campaign_contacts",
        "previous_outcome", "campaign_outcome"
    ]].copy()

    # table 3: economics.csv
    economics = bank_mark[[
        "client_id", "cons_price_idx", "euribor_three_months"
    ]].copy()

    # 3. Clean client table
    # Clean education column
    client["education"] = (
        client["education"]
        .str.replace(r"\.", "_", regex=True)
        .replace("unknown", np.nan)
    )
    # Clean job column
    client["job"] = client["job"].str.replace(r"\.", "_", regex=True)

    # Clean and convert client columns to bool data type
    for col in ["credit_default", "mortgage"]:
        client[col] = (
            client[col]
            .map({"yes": 1, "no": 0, "unknown": 0})
            .astype(bool)
        )

    # 4. Clean campaign table
    # Change campaign_outcome to binary values
    campaign["campaign_outcome"] = campaign["campaign_outcome"].map({"yes": 1, "no": 0})
    
    # Convert previous_outcome to binary values
    campaign["previous_outcome"] = campaign["previous_outcome"].map({
        "success": 1, "failure": 0, "nonexistent": 0
    })
    
    # Add year column
    campaign["year"] = "2022"
    
    # Convert day to string
    campaign["day"] = campaign["day"].astype(str)
    
    # Add last_contact_date column and convert to datetime
    campaign["last_contact_date"] = pd.to_datetime(
        campaign["year"] + "-" + campaign["month"] + "-" + campaign["day"],
        format="%Y-%b-%d"
    )
    
    # Clean and convert outcome columns to bool
    for col in ["campaign_outcome", "previous_outcome"]:
        campaign[col] = campaign[col].astype(bool)
        
    # Drop unneccessary columns
    campaign.drop(columns=["month", "day", "year"], inplace=True)

    # 5. Save tables to individual csv files
    client.to_csv("output\client.csv", index=False)
    campaign.to_csv("output\campaign.csv", index=False)
    economics.to_csv("output\economics.csv", index=False)

    print("Cleaned files written to 'output/' directory.")

if __name__ == "__main__":
    main()
