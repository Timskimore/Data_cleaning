# Personal Loans Marketing Data Cleaning

A Python CLI script to clean and restructure bank marketing data for PostgreSQL ingestion.

## Table of Contents

- [Problem Statement](#problem-statement)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Data Cleaning Details](#data-cleaning-details)
- [Output Files](#output-files)
- [Contributing](#contributing)
- [License](#license)

## Problem Statement

Personal loans generate significant interest revenue. This script cleans `bank_marketing.csv` and splits it into three tables conforming to specified schemas.

## Project Structure
```plaintext
bank_marketing_cleaning\
├── data\
│   └── bank_marketing.csv
├── output\
│   ├── client.csv
│   ├── campaign.csv
│   └── economics.csv
├── bank_mark.py
├── README.md
└── requirements.txt
```

## Setup

1. **Clone repository**  
2. **Create a virtual environment**  
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
## Usage
```bash
python bankmark.py
```

## 🧹 Data Cleaning Details
## 🧹 Data Cleaning Details

### 📁 `client.csv`
- **Standardize Text Fields**:  
  - Replace `.` with `_` in `job` and `education`.  
- **Handle Missing Values**:  
  - Convert `"unknown"` in `education` to `NaN`.  
- **Convert to Boolean**:  
  - Map `"yes"/"no"/"unknown"` → `True`/`False` in `credit_default` & `mortgage`.

### 📁 `campaign.csv`
- **Convert Outcomes to Boolean**:  
  - Map `campaign_outcome` (`"yes"→True`, `"no"→False`) and  
    `previous_outcome` (`"success"→True`, `"failure"/"nonexistent"→False`).  
- **Construct `last_contact_date`**:  
  - Combine `day`, `month`, and fixed `year=2022` into a `YYYY-MM-DD` datetime.  
- **Clean Up**:  
  - Drop the now-redundant `month`, `day`, and `year` columns.

### 📁 `economics.csv`
- **Extract Economic Indicators**:  
  - Select `cons_price_idx` and `euribor_three_months` without modification.

## Output
Located in the output\ directory.

## Contributing
We welcome contributions to improve data cleaning, add new features, or fix bugs. Please follow the steps below:

1. Filing Issues
🔍 Search existing issues before opening a new one to avoid duplicates.

📝 Use templates: Provide a clear title, detailed description, example input/output, and your environment setup (OS, Python version).

🚩 Label appropriately: Tag your issue as bug, enhancement, or question.

2. Proposing Changes (Pull Requests)
-   Fork the repository and create a feature branch
-   Install dependencies and run tests locally
-   Add tests or examples for new functionality under a tests\ or examples\ folder
-   Use Commit messages
3. Review Process
-   We aim to review PRs within 3 business days.
-   A minimum of one approval is required before merging.
-   We may request changes—please address feedback promptly.

4. Code of Conduct
By participating, you agree to abide by our Code of Conduct. Be respectful, constructive, and collaborative.

5. Contact
For quick questions, reach out to the maintainer at olanipekuntimileyin@gmail.com or open an issue labeled question.
## License
This project is licensed under MIT. See LICENSE.