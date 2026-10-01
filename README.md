# 📅 Science Days Reminder Bot

A simple Python bot that sends email reminders about upcoming science/educational special days for teachers.

## Files
- `scientific_reminder.py` - Main reminder script
- `scientific_reminder.env.example` - Template for environment configuration

## Setup Instructions

### 1. Install Python dependencies
```bash
pip install python-dotenv
```

### 2. Configure email credentials
1. Rename `.env.example` to `.env`:
   ```bash
   copy scientific_reminder.env.example .env
   ```

2. Edit `.env` with your details:
   - **SMTP_USER**: Your Gmail address (or use another email provider)
   - **SMTP_PASS**: Gmail App Password (NOT your regular password)
   - **TO_EMAIL**: Email address to receive reminders

**How to create Gmail App Password:**
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" app
3. Select "Other" for device and name it "Science Reminder Bot"
4. Copy the generated 16-character password

### 3. Update the special days
Edit `scientific_reminder.py` and add/modify events in the `SPECIAL_DAYS` list.

### 4. Run the script manually (to test)
```bash
python scientific_reminder.py
```

### 5. Set up daily scheduling

**Windows Task Scheduler:**
1. Open "Task Scheduler"
2. Create Basic Task → Name: "Science Reminder Bot"
3. Trigger: Daily, set time to 6:00 AM
4. Action: Start a program → Program: `python.exe`
5. Arguments: `C:\Users\ASUS\scientific_reminder.py`
6. Start in: `C:\Users\ASUS`

Or use **Windows Task Scheduler CLI**:
```cmd
schtasks /create /tn "Science Reminder Bot" /tr "python C:\Users\ASUS\scientific_reminder.py" /sc daily /st 06:00
```

## Current Special Days Included (80+ Events - 2026-2027)

**January 2026**
- World Braille Day (Jan 4) - Accessibility through science
- International Day of Education (Jan 24)
- International Day of Clean Energy (Jan 26)
- World Neglected Tropical Diseases Day (Jan 30)
- Homi J. Bhabha Birth Anniversary (Oct 30, 2026 - moved to correct date)

**February 2026**
- World Wetlands Day (Feb 2)
- International Day of Women and Girls in Science (Feb 11)
- Darwin Day (Feb 12)
- World Radio Day (Feb 13)
- National Science Day – C. V. Raman (Feb 28)

**March 2026**
- World Wildlife Day (Mar 3)
- World Engineering Day (Mar 4)
- Pi Day / International Day of Mathematics (Mar 14)
- World Sparrow Day (Mar 20)
- International Day of Forests (Mar 21)
- World Water Day (Mar 22)
- World Meteorological Day (Mar 23)
- World TB Day (Mar 24)

**April 2026**
- World Health Day (Apr 7)
- Aryabhata Satellite Launch Anniversary (Apr 19) - ISRO's first satellite
- World Creativity and Innovation Day (Apr 21)
- Earth Day (Apr 22)
- World Malaria Day (Apr 25)
- DNA Day (Apr 25)
- World Intellectual Property Day (Apr 26)

**May 2026**
- National Technology Day (May 11) ★ - Pokhran-II tests
- International Day of Women in Mathematics (May 12)
- International Day of Light (May 16)
- World Bee Day (May 20)
- International Day for Biological Diversity (May 22)
- World No Tobacco Day (May 31)

**June 2026**
- World Environment Day (Jun 5) ★
- World Food Safety Day (Jun 7)
- World Oceans Day (Jun 8)
- Global Wind Day (Jun 15)
- World Day to Combat Desertification and Drought (Jun 17)
- International Day of Yoga (Jun 21)
- International Asteroid Day (Jun 30)

**July 2026**
- World Population Day (Jul 11)
- Rohini/RS-1 launch anniversary (Jul 18) ★ - ISRO
- Chandrayaan-2 Launch Anniversary (Jul 22) ★ - ISRO
- World Drowning Prevention Day (Jul 25)
- World Hepatitis Day (Jul 28)
- International Tiger Day (Jul 29)

**August 2026**
- Rohini Technology Payload Anniversary (Aug 10) ★ - ISRO
- Vikram Sarabhai Birth Anniversary (Aug 12) ★ - Father of Indian Space Program
- International Youth Day (Aug 12)
- Akshay Urja Diwas (Aug 20) - Renewable Energy
- National Space Day – Chandrayaan-3 (Aug 23) ★★★ - Successful landing
- INSAT-1B Launch Anniversary (Aug 30) ★ - ISRO

**September 2026**
- Aditya-L1 Launch Anniversary (Sep 2) ★ - ISRO solar observatory
- Teachers' Day (Sep 5)
- International Day of Clean Air for Blue Skies (Sep 7)
- World Ozone Day (Sep 16) ★
- World Patient Safety Day (Sep 17)
- Satish Dhawan Birth Anniversary (Sep 25) ★ - ISRO leader
- AstroSat Launch Anniversary (Sep 28) ★ - ISRO
- World Rabies Day (Sep 28)
- World Heart Day (Sep 29)

**October 2026**
- World Space Week Begins (Oct 4) ★★★ - Oct 4-10
- Meghnad Saha Birth Anniversary (Oct 6) - Astrophysics
- World Mental Health Day (Oct 10)
- International Day of the Girl Child (Oct 11)
- International E-Waste Day (Oct 14)
- APJ Abdul Kalam Birth Anniversary (Oct 15) ★★★ - Missile Man
- PSLV First Successful Flight Anniversary (Oct 15) ★ - ISRO
- World Food Day (Oct 16)
- World Development Information Day (Oct 24)
- Homi J. Bhabha Birth Anniversary (Oct 30) ★★★ - Nuclear Scientist

**November 2026**
- Mars Orbiter Mission / Mangalyaan Launch Anniversary (Nov 5) ★★★ - ISRO
- C. V. Raman Birth Anniversary (Nov 7)
- World Science Day for Peace and Development (Nov 10) ★
- Children's Day / Science Activities (Nov 14)
- World AMR Awareness Week Begins (Nov 18)
- Jagadish Chandra Bose Birth Anniversary (Nov 30) ★ - Radio Science

**December 2026**
- World AIDS Day (Dec 1)
- National Pollution Control Day (Dec 2)
- World Soil Day (Dec 5) ★
- Human Rights Day (Dec 10)
- International Mountain Day (Dec 11)
- National Energy Conservation Day (Dec 14)
- National Mathematics Day – Srinivasa Ramanujan (Dec 22) ★★★
- International Day of Epidemic Preparedness (Dec 27)

**January 2027**
- XPoSat Launch Anniversary (Jan 1, 2027) ★ - ISRO polarimetry mission
- International Day of Education (Jan 24)

**February 2027**
- Darwin Day (Feb 12)
- National Science Day – C. V. Raman (Feb 28)

★ = Indian scientists/science days added
★★★ = ISRO/space mission anniversaries

## Adding More Events
The `SPECIAL_DAYS` list in `scientific_reminder.py` is easy to extend:

```python
{
    "name": "Event Name",
    "date": "2025-12-25",  # YYYY-MM-DD format
    "description": "Brief description for assembly talk",
    "subjects": ["Biology", "Chemistry"]  # Related subjects
}
```