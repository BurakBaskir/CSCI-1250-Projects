# Domain Security Check Project
A Python project created as part of the **CSCI 1250 course**. This program analyzes email domains for potential security risks, calculates a numeric risk score, determines actions based on user security preferences, and generates a detailed security report.

## Features
- Load predefined high-risk, medium-risk, and marketing domains.
- Calculate a numeric risk score for each domain based on direct matches, keywords, and subdomain patterns.
- Determine actions (BLOCK, QUARANTINE, ALLOW) based on risk score and user security level.
- Process multiple email domains at once.
- Generate a comprehensive report including blocked, quarantined, and allowed domains.
- Highlight known high-risk and medium-risk domains as well as unknown potential threats.

## Installation
- Clone the main repository:
  git clone https://github.com/BurakBaskir/CSCI-1250-Projects.git
- Navigate to this project folder inside the repo:
  cd CSCI-1250-Projects/Domain-Security-Check-Project
- Run the program (requires Python 3.x):
  python Domain_Checker.py

## Usage
- The program will prompt you to choose a security level: strict, moderate, or relaxed.
- It will then process a batch of incoming email domains and display the results.
- Example output:
  📊 PROCESSING SUMMARY:
     Total emails processed: 8
     🚫 Blocked: 3 (37.5%)
     ⚠️  Quarantined: 1 (12.5%)
     ✅ Allowed: 4 (50.0%)

  🔍 THREAT ANALYSIS:
     Known high-risk domains blocked: 1
     Known medium-risk domains blocked: 2
     🆕 New potential threats discovered: 1

## Reference / Inspiration
This project was inspired by the [CSCI 1250 class resources](https://github.com/CSCI-1250/class_resources_public) provided by Professor Ryan Haas.

## Author
**Burak Baskir**  
[GitHub Profile](https://github.com/BurakBaskir)
