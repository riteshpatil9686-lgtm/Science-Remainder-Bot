#!/usr/bin/env python3
"""
Scientific Education Days Reminder Bot
Sends email reminders to science teachers about upcoming special days.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from datetime import date

# Load environment variables
load_dotenv()

# Science & Educational Special Days (dates for 2026-2027)
# Each event has: name, date (YYYY-MM-DD), description for assembly talk, subjects covered
SPECIAL_DAYS = [
    # January 2026
    {
        "name": "World Braille Day",
        "date": "2026-01-04",
        "description": "Accessibility through science: Braille as tactile writing system. Connect to neuroscience of touch, materials science of dots, and inclusive design.",
        "subjects": ["Biology", "Physics", "Engineering"]
    },
    {
        "name": "International Day of Education",
        "date": "2026-01-24",
        "description": "Science education for sustainable development. Discuss how STEM literacy empowers communities to solve local challenges.",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    {
        "name": "International Day of Clean Energy",
        "date": "2026-01-26",
        "description": "Renewable energy physics and chemistry: solar photovoltaics, wind turbine aerodynamics, battery storage chemistry, grid integration.",
        "subjects": ["Physics", "Chemistry", "Engineering"]
    },
    {
        "name": "World Neglected Tropical Diseases Day",
        "date": "2026-01-30",
        "description": "Diseases affecting 1+ billion people: dengue, chikungunya, leprosy. Talk about parasite biology, vaccine chemistry, diagnostic physics.",
        "subjects": ["Biology", "Chemistry", "Health Science"]
    },
    {
        "name": "Homi J. Bhabha Birth Anniversary",
        "date": "2026-10-30",  # Corrected: Born Oct 30, 1909 (not Jan 30)
        "description": "Father of Indian Nuclear Program. Tata Institute, BARC founding. Cosmic ray research, nuclear physics vision for India's atomic energy program.",
        "subjects": ["Physics", "Nuclear Science"]
    },
    # February 2026
    {
        "name": "World Wetlands Day",
        "date": "2026-02-02",
        "description": "Wetland ecosystems: biodiversity hotspots, carbon sinks, water filtration. Mangrove biology, peat soil chemistry, flood protection physics.",
        "subjects": ["Biology", "Chemistry", "Environmental Science"]
    },
    {
        "name": "International Day of Women and Girls in Science",
        "date": "2026-02-11",
        "description": "Celebrate women scientists: Marie Curie, Rosalind Franklin, Tessy Thomas (Agni missile), Gagandeep Kang (virology). Gender equity in STEM.",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    {
        "name": "Darwin Day",
        "date": "2026-02-12",
        "description": "Charles Darwin's birthday. Evolution by natural selection, common descent, evidence from fossils to DNA. Modern synthesis with genetics.",
        "subjects": ["Biology", "Genetics", "Evolution"]
    },
    {
        "name": "World Radio Day",
        "date": "2026-02-13",
        "description": "Physics of electromagnetic waves, modulation, antenna design. Marconi's invention, radio astronomy, MRI physics, wireless communication evolution.",
        "subjects": ["Physics", "Engineering"]
    },
    {
        "name": "National Science Day – C. V. Raman",
        "date": "2026-02-28",
        "description": "Sir CV Raman discovered Raman Effect (1928) - light scattering reveals molecular vibrations. Nobel Prize 1930. Foundation of spectroscopy in chemistry/physics.",
        "subjects": ["Physics", "Chemistry"]
    },
    # March 2026
    {
        "name": "World Wildlife Day",
        "date": "2026-03-03",
        "description": "Biodiversity conservation: species extinction rates, habitat loss, CITES treaty. Connect to genetics, ecology, conservation biology.",
        "subjects": ["Biology", "Environmental Science"]
    },
    {
        "name": "World Engineering Day",
        "date": "2026-03-04",
        "description": "Engineering applies science to solve problems: civil (bridges), mechanical (engines), chemical (processes), electrical (circuits). Design thinking.",
        "subjects": ["Physics", "Chemistry", "Engineering"]
    },
    {
        "name": "Pi Day / International Day of Mathematics",
        "date": "2026-03-14",
        "description": "Pi (π) in physics (wave mechanics, orbits), chemistry (quantum mechanics, molecular orbitals), biology (population growth, DNA structure).",
        "subjects": ["Physics", "Chemistry", "Biology", "Mathematics"]
    },
    {
        "name": "World Sparrow Day",
        "date": "2026-03-20",
        "description": "Urban biodiversity indicator. House sparrow decline due to pollution, lack of nesting sites, insect food sources. Citizen science monitoring.",
        "subjects": ["Biology", "Environmental Science"]
    },
    {
        "name": "International Day of Forests",
        "date": "2026-03-21",
        "description": "Forest ecosystems: carbon sequestration, biodiversity, water cycle regulation. Deforestation impacts, reforestation strategies, forest pharmacology.",
        "subjects": ["Biology", "Chemistry", "Environmental Science"]
    },
    {
        "name": "World Water Day",
        "date": "2026-03-22",
        "description": "Water's anomalous properties: hydrogen bonding, density maximum at 4°C, universal solvent. Hydrology, water chemistry, access challenges.",
        "subjects": ["Chemistry", "Biology", "Environmental Science"]
    },
    {
        "name": "World Meteorological Day",
        "date": "2026-03-23",
        "description": "Weather vs climate, atmospheric physics, climate modeling. Monsoon dynamics, El Niño/La Niña, extreme event attribution.",
        "subjects": ["Physics", "Earth Science"]
    },
    {
        "name": "World TB Day",
        "date": "2026-03-24",
        "description": "Tuberculosis: Mycobacterium tuberculosis biology, antibiotic resistance, BCG vaccine, diagnostics (GeneXpert), social determinants.",
        "subjects": ["Biology", "Chemistry", "Health Science"]
    },
    # April 2026
    {
        "name": "World Health Day",
        "date": "2026-04-07",
        "description": "Annual WHO theme. Discuss vaccines, antibiotics, disease prevention, health systems, and how biology/chemistry create medical breakthroughs.",
        "subjects": ["Biology", "Chemistry", "Health Science"]
    },
    {
        "name": "Aryabhata Satellite Launch Anniversary",
        "date": "2026-04-19",
        "description": "India's first satellite (1975): X-ray astronomy, aerospace engineering, telemetry systems. Beginning of ISRO's space journey.",
        "subjects": ["Physics", "Engineering", "Space Science"]
    },
    {
        "name": "World Creativity and Innovation Day",
        "date": "2026-04-21",
        "description": "Science thrives on creativity. Talk about accidental discoveries (penicillin, X-rays, microwave) and how curiosity drives innovation.",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    {
        "name": "Earth Day",
        "date": "2026-04-22",
        "description": "Planetary boundaries: climate change, biodiversity loss, biogeochemical cycles. Earth system science, sustainability challenges.",
        "subjects": ["Biology", "Chemistry", "Physics", "Environmental Science"]
    },
    {
        "name": "World Malaria Day",
        "date": "2026-04-25",
        "description": "Plasmodium parasite biology, mosquito vector control, artemisinin chemistry, bed net physics, vaccine RTS,S/AS01.",
        "subjects": ["Biology", "Chemistry", "Health Science"]
    },
    {
        "name": "DNA Day",
        "date": "2026-04-25",
        "description": "Double helix discovery (1953), Human Genome Project, CRISPR gene editing. Molecular basis of inheritance, biotechnology revolution.",
        "subjects": ["Biology", "Chemistry", "Genetics"]
    },
    {
        "name": "World Intellectual Property Day",
        "date": "2026-04-26",
        "description": "Patents, copyright, trademarks in science. Balancing innovation access with inventor rights. Open science vs proprietary research.",
        "subjects": ["Physics", "Chemistry", "Biology", "Engineering"]
    },
    # May 2026
    {
        "name": "National Technology Day",
        "date": "2026-05-11",
        "description": "Pokhran-II nuclear tests (1998): India's technological self-reliance. Nuclear physics, materials science, engineering. Dr. APJ Abdul Kalam's leadership.",
        "subjects": ["Physics", "Chemistry", "Engineering"]
    },
    {
        "name": "International Day of Women in Mathematics",
        "date": "2026-05-12",
        "description": "Celebrate women mathematicians: Emmy Noether (theorems), Katherine NASA trajectories, Maryam Mirzakhani (Fields Medal). Math in science.",
        "subjects": ["Mathematics", "Physics"]
    },
    {
        "name": "International Day of Light",
        "date": "2026-05-16",
        "description": "Light's dual nature: wave-particle duality, quantum electrodynamics. Applications: lasers (physics), spectroscopy (chemistry), photosynthesis (biology).",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    {
        "name": "World Bee Day",
        "date": "2026-05-20",
        "description": "Pollinator decline: colony collapse disorder, neonicotinoid pesticides. Bee biology, plant-pollinator coevolution, food security links.",
        "subjects": ["Biology", "Environmental Science", "Chemistry"]
    },
    {
        "name": "International Day for Biological Diversity",
        "date": "2026-05-22",
        "description": "Biodiversity loss crisis: extinction rates, ecosystem services. Genetic resources for medicine, agriculture, resilience. 30x30 conservation goal.",
        "subjects": ["Biology", "Environmental Science"]
    },
    {
        "name": "World No Tobacco Day",
        "date": "2026-05-31",
        "description": "Tobacco health impacts: nicotine addiction pharmacology, lung cancer biology, cardiovascular chemistry. Second-hand smoke physics.",
        "subjects": ["Biology", "Chemistry", "Health Science"]
    },
    # June 2026
    {
        "name": "World Environment Day",
        "date": "2026-06-05",
        "description": "Annual UNEP theme. Climate change science, carbon cycle, greenhouse gas physics/chemistry, renewable energy solutions.",
        "subjects": ["Chemistry", "Biology", "Physics", "Environmental Science"]
    },
    {
        "name": "World Food Safety Day",
        "date": "2026-06-07",
        "description": "Foodborne pathogens: biology of Salmonella, E. coli, Listeria. Food preservation chemistry, packaging physics, hygiene microbiology.",
        "subjects": ["Biology", "Chemistry", "Health Science"]
    },
    {
        "name": "World Oceans Day",
        "date": "2026-06-08",
        "description": "Ocean acidification (chemistry), marine biodiversity loss, overfishing biology, plastic pollution physics/chemistry, blue economy.",
        "subjects": ["Chemistry", "Biology", "Physics", "Environmental Science"]
    },
    {
        "name": "Global Wind Day",
        "date": "2026-06-15",
        "description": "Wind energy physics: Betz limit, blade aerodynamics, grid integration. Wind resource mapping, offshore wind farms, storage solutions.",
        "subjects": ["Physics", "Engineering"]
    },
    {
        "name": "World Day to Combat Desertification and Drought",
        "date": "2026-06-17",
        "description": "Land degradation biology, soil chemistry changes, water cycle disruption. Reforestation, sustainable agriculture, climate adaptation.",
        "subjects": ["Biology", "Chemistry", "Environmental Science"]
    },
    {
        "name": "International Day of Yoga",
        "date": "2026-06-21",
        "description": "Mind-body science: yoga's effects on nervous system, stress hormones (cortisol), flexibility physiology, cardiovascular health.",
        "subjects": ["Biology", "Health Science"]
    },
    {
        "name": "International Asteroid Day",
        "date": "2026-06-30",
        "description": "Near-Earth objects: impact physics (Chicxulub), deflection strategies (kinetic impactor, gravity tractor), asteroid mining chemistry.",
        "subjects": ["Physics", "Space Science"]
    },
    # July 2026
    {
        "name": "World Population Day",
        "date": "2026-07-11",
        "description": "Population biology: exponential growth, carrying capacity, demographic transition. Resource consumption, food security, urbanization challenges.",
        "subjects": ["Biology", "Chemistry", "Environmental Science"]
    },
    {
        "name": "Rohini/RS-1 launch anniversary",
        "date": "2026-07-18",
        "description": "India's first indigenous satellite launch (1980): RS-1 experimental satellite. Solid propellant chemistry, satellite telemetry physics.",
        "subjects": ["Physics", "Engineering", "Space Science"]
    },
    {
        "name": "Chandrayaan-2 Launch Anniversary",
        "date": "2026-07-22",
        "description": "India's second lunar mission (2019): orbiter, lander (Vikram), rover (Pragyan). Lunar surface chemistry, exosphere studies, south pole exploration.",
        "subjects": ["Physics", "Chemistry", "Space Science"]
    },
    {
        "name": "World Drowning Prevention Day",
        "date": "2026-07-25",
        "description": "Physics of drowning: hydrodynamics, cold shock response, laryngospasm. Prevention: swimming education, life jacket physics, rescue techniques.",
        "subjects": ["Physics", "Biology", "Health Science"]
    },
    {
        "name": "World Hepatitis Day",
        "date": "2026-07-28",
        "description": "Viral hepatitis biology: HBV, HCV, HAV viruses. Vaccine chemistry, antiviral drug development, liver pathology, transmission prevention.",
        "subjects": ["Biology", "Chemistry", "Health Science"]
    },
    {
        "name": "International Tiger Day",
        "date": "2026-07-29",
        "description": "Tiger conservation biology: Panthera tigris subspecies, genetic diversity, habitat corridors. Camera trap physics, prey-predator dynamics.",
        "subjects": ["Biology", "Environmental Science"]
    },
    # August 2026
    {
        "name": "Rohini Technology Payload Anniversary",
        "date": "2026-08-10",
        "description": "ISRO's Rohini Technology Payload (RTP) flights: experimental satellites for technology demonstration. Microgravity experiments, material science in space.",
        "subjects": ["Physics", "Engineering", "Space Science"]
    },
    {
        "name": "Vikram Sarabhai Birth Anniversary",
        "date": "2026-08-12",
        "description": "Father of Indian Space Program (born 1919). ISRO founding, satellite technology, space physics. Vision: 'We must be second to none in application of advanced technologies to real problems of man and society.'",
        "subjects": ["Physics", "Space Science"]
    },
    {
        "name": "International Youth Day",
        "date": "2026-08-12",
        "description": "Young scientists who changed the world: Marie Curie (teen research), Einstein (26, annus mirabilis), Malala (education advocacy). Inspire STEM pursuit.",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    {
        "name": "Akshay Urja Diwas",
        "date": "2026-08-20",
        "description": "Renewable Energy Day: solar, wind, hydro, biomass. Physics of photovoltaics, chemistry of biofuels, engineering of grid storage, policy frameworks.",
        "subjects": ["Physics", "Chemistry", "Engineering"]
    },
    {
        "name": "National Space Day – Chandrayaan-3",
        "date": "2026-08-23",
        "description": "Chandrayaan-3 successful landing (2023): Vikram lander and Pragyan rover. Lunar south pole regolith chemistry, temperature measurements, seismic data.",
        "subjects": ["Physics", "Chemistry", "Space Science"]
    },
    {
        "name": "INSAT-1B Launch Anniversary",
        "date": "2026-08-30",
        "description": "INSAT-1B: India's first operational domestic satellite system (1983). Meteorology, telecommunications, broadcasting. Geostationary orbit physics.",
        "subjects": ["Physics", "Engineering", "Space Science"]
    },
    # September 2026
    {
        "name": "Aditya-L1 Launch Anniversary",
        "date": "2026-09-02",
        "description": "India's first solar observatory mission (2023): Halo orbit at L1 point. Solar corona studies, solar wind physics, space weather prediction.",
        "subjects": ["Physics", "Space Science"]
    },
    {
        "name": "Teachers' Day",
        "date": "2026-09-05",
        "description": "Celebrate educators' role in society. Science teachers: inspiring curiosity, scientific method, evidence-based thinking, future innovators.",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    {
        "name": "International Day of Clean Air for Blue Skies",
        "date": "2026-09-07",
        "description": "Air pollution chemistry: PM2.5 formation, NOx/SOx chemistry, ozone troposphere. Health impacts (respiratory/cardiovascular), clean tech solutions.",
        "subjects": ["Chemistry", "Biology", "Physics"]
    },
    {
        "name": "World Ozone Day",
        "date": "2026-09-16",
        "description": "Montreal Protocol success: CFC phase-out, ozone layer healing. Stratospheric chemistry, UV radiation biology, climate co-benefits.",
        "subjects": ["Chemistry", "Physics", "Biology"]
    },
    {
        "name": "World Patient Safety Day",
        "date": "2026-09-17",
        "description": "Healthcare safety science: infection control biology, medication chemistry, device physics, systems engineering. Reducing preventable harm.",
        "subjects": ["Biology", "Chemistry", "Health Science", "Engineering"]
    },
    {
        "name": "Satish Dhawan Birth Anniversary",
        "date": "2026-09-25",
        "description": "ISRO's visionary leader (born 1920): guided India's space program through formative years. Aerodynamics, boundary layer theory, rocket propulsion.",
        "subjects": ["Physics", "Engineering", "Space Science"]
    },
    {
        "name": "AstroSat Launch Anniversary",
        "date": "2026-09-28",
        "description": "India's first multi-wavelength space observatory (2015): simultaneous UV, optical, X-ray studies. Celestial physics, high-energy astrophysics.",
        "subjects": ["Physics", "Space Science"]
    },
    {
        "name": "World Rabies Day",
        "date": "2026-09-28",
        "description": "Rabies virus biology: neurotropic lyssavirus, fatal encephalitis. Vaccine chemistry, post-exposure prophylaxis, One Health approach.",
        "subjects": ["Biology", "Chemistry", "Health Science"]
    },
    {
        "name": "World Heart Day",
        "date": "2026-09-29",
        "description": "Cardiovascular disease: atherosclerosis biology, hypertension physiology, cholesterol chemistry. Prevention: diet, exercise, smoking cessation.",
        "subjects": ["Biology", "Chemistry", "Health Science"]
    },
    # October 2026
    {
        "name": "World Space Week Begins",
        "date": "2026-10-04",
        "description": "Oct 4-10: Celebrates space science and technology. Theme varies yearly. Connect to satellite applications, exploration benefits, international cooperation.",
        "subjects": ["Physics", "Engineering", "Space Science"]
    },
    {
        "name": "Meghnad Saha Birth Anniversary",
        "date": "2026-10-06",
        "description": "Astrophysicist (born 1893): Saha ionization equation explains stellar spectra. Thermal equilibrium physics, connecting atomic physics to astronomy.",
        "subjects": ["Physics"]
    },
    {
        "name": "World Mental Health Day",
        "date": "2026-10-10",
        "description": "Mental health biology: neurotransmitter chemistry (serotonin, dopamine), neural circuitry, genetics-environment interactions. Destigmatization through science.",
        "subjects": ["Biology", "Chemistry", "Health Science"]
    },
    {
        "name": "International Day of the Girl Child",
        "date": "2026-10-11",
        "description": "Girls in STEM: address barriers, showcase role models (Tessy Thomas, Gagandeep Khan, etc.). Gender equity improves scientific innovation.",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    {
        "name": "International E-Waste Day",
        "date": "2026-10-14",
        "description": "Electronic waste chemistry: heavy metals (lead, mercury), rare earth recovery, recycling physics/engineering. Circular economy for technology.",
        "subjects": ["Chemistry", "Engineering", "Environmental Science"]
    },
    {
        "name": "APJ Abdul Kalam Birth Anniversary",
        "date": "2026-10-15",
        "description": "Missile Man of India (born 1931): Aerospace engineering, nuclear physics, IGMDP, science education advocacy. 'Dream, dream, dream' - transform thoughts into action.",
        "subjects": ["Physics", "Engineering", "Aerospace"]
    },
    {
        "name": "PSLV First Successful Flight Anniversary",
        "date": "2026-10-15",
        "description": "PSLV-D2/IRS-P2 (1994): First successful operational Polar Satellite Launch Vehicle flight. Reliable workhorse for Indian and international satellites.",
        "subjects": ["Physics", "Engineering", "Space Science"]
    },
    {
        "name": "World Food Day",
        "date": "2026-10-16",
        "description": "Food systems science: agricultural biology (photosynthesis, nitrogen fixation), food chemistry (nutrition, preservation), physics of processing. Zero hunger goal.",
        "subjects": ["Chemistry", "Biology", "Physics"]
    },
    {
        "name": "World Development Information Day",
        "date": "2026-10-24",
        "description": "Development statistics for policy: demographic trends, economic indicators, environmental metrics. Data collection physics/chemistry, indicator biology.",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    {
        "name": "Homi J. Bhabha Birth Anniversary",
        "date": "2026-10-30",
        "description": "Father of Indian Nuclear Program (born 1909): Tata Institute, BARC founding. Cosmic ray research, nuclear physics vision for India's peaceful atomic energy program.",
        "subjects": ["Physics", "Nuclear Science"]
    },
    # November 2026
    {
        "name": "Mars Orbiter Mission / Mangalyaan Launch Anniversary",
        "date": "2026-11-05",
        "description": "India's first interplanetary mission (2013): Mars orbiter study of surface, atmosphere, exosphere. Cost-effective interplanetary technology demonstration.",
        "subjects": ["Physics", "Chemistry", "Space Science"]
    },
    {
        "name": "C. V. Raman Birth Anniversary",
        "date": "2026-11-07",
        "description": "Sir CV Raman born (1888): Nobel physicist (1930) discovered Raman effect - inelastic scattering of light. Foundation for molecular spectroscopy.",
        "subjects": ["Physics", "Chemistry"]
    },
    {
        "name": "World Science Day for Peace and Development",
        "date": "2026-11-10",
        "description": "UNESCO day: Science as human right, open science, science diplomacy. International scientific cooperation for SDGs and peacebuilding.",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    {
        "name": "Children's Day / Science Activities",
        "date": "2026-11-14",
        "description": "Celebrate childhood through science: hands-on experiments, curiosity-driven learning, scientific method for young minds. Make science fun and accessible.",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    {
        "name": "World AMR Awareness Week Begins",
        "date": "2026-11-18",
        "description": "Antimicrobial resistance: evolution in action (biology), drug chemistry, diagnostic physics. One Health approach: human-animal-environment linkages.",
        "subjects": ["Biology", "Chemistry"]
    },
    {
        "name": "Jagadish Chandra Bose Birth Anniversary",
        "date": "2026-11-30",
        "description": "Father of Radio Science (born 1858): Plant physiology (crescograph), radio waves, microwave optics. First Indian to get a US patent.",
        "subjects": ["Physics", "Biology", "Plant Science"]
    },
    # December 2026
    {
        "name": "World AIDS Day",
        "date": "2026-12-01",
        "description": "HIV/AIDS biology: retrovirus life cycle, immune system destruction, antiretroviral chemistry. Prevention education, treatment as prevention.",
        "subjects": ["Biology", "Chemistry", "Health Science"]
    },
    {
        "name": "National Pollution Control Day",
        "date": "2026-12-02",
        "description": "Bhopal gas tragedy remembrance (1984): industrial safety chemistry, emergency response physics, environmental monitoring, corporate accountability.",
        "subjects": ["Chemistry", "Engineering", "Environmental Science"]
    },
    {
        "name": "World Soil Day",
        "date": "2026-12-05",
        "description": "Soil as living ecosystem: mineral chemistry, organic matter biology, soil physics (structure, water retention). Decomposer microbiome, nutrient cycling.",
        "subjects": ["Chemistry", "Biology", "Physics", "Environmental Science"]
    },
    {
        "name": "Human Rights Day",
        "date": "2026-12-10",
        "description": "Science in human rights: forensic biology (DNA), chemical weapons detection, satellite monitoring physics. Evidence-based advocacy.",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    {
        "name": "International Mountain Day",
        "date": "2026-12-11",
        "description": "Mountain ecosystems: biodiversity hotspots, water towers, cultural diversity. Climate change impacts: glacial melt, species shifts, slope stability physics.",
        "subjects": ["Biology", "Environmental Science", "Physics"]
    },
    {
        "name": "National Energy Conservation Day",
        "date": "2026-12-14",
        "description": "Energy efficiency physics: insulation, efficient appliances, industrial processes. Behavioral change, policy frameworks, renewable integration.",
        "subjects": ["Physics", "Engineering"]
    },
    {
        "name": "National Mathematics Day – Srinivasa Ramanujan",
        "date": "2026-12-22",
        "description": "Mathematical genius (born 1887): infinite series, number theory, partitions, mock theta functions. Hardy-Ramanujan number 1729. Self-taught brilliance.",
        "subjects": ["Mathematics", "Physics", "Chemistry"]
    },
    {
        "name": "International Day of Epidemic Preparedness",
        "date": "2026-12-27",
        "description": "Pandemic science: virology (biology), vaccine chemistry (mRNA), epidemiology modeling (physics/math), genomics surveillance. Lessons from COVID-19.",
        "subjects": ["Biology", "Chemistry", "Physics"]
    },
    {
        "name": "TEST EVENT - Tomorrow's Reminder Check",
        "date": "2026-10-02",
        "description": "This is a test reminder to verify the bot works. If you receive this email, the reminder system is working correctly.",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    # January 2027
    {
        "name": "International Day of Education",
        "date": "2027-01-24",
        "description": "Science education for sustainable development. Discuss how STEM literacy empowers communities to solve local challenges.",
        "subjects": ["Physics", "Chemistry", "Biology"]
    },
    {
        "name": "XPoSat Launch Anniversary",
        "date": "2027-01-01",
        "description": "India's first dedicated polarimetry mission (2024): studies X-ray polarization from cosmic sources. Emission mechanisms in black holes, neutron stars.",
        "subjects": ["Physics", "Space Science"]
    },
    # February 2027
    {
        "name": "Darwin Day",
        "date": "2027-02-12",
        "description": "Charles Darwin's birthday. Evolution by natural selection, common descent, evidence from fossils to DNA. Modern synthesis with genetics.",
        "subjects": ["Biology", "Genetics", "Evolution"]
    },
    {
        "name": "National Science Day – C. V. Raman",
        "date": "2027-02-28",
        "description": "Sir CV Raman discovered Raman Effect (1928) - light scattering reveals molecular vibrations. Nobel Prize 1930. Foundation of spectroscopy in chemistry/physics.",
        "subjects": ["Physics", "Chemistry"]
    }
]


def get_reminders_for_today(target_date):
    """Get all events happening tomorrow."""
    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    
    reminders = []
    for event in SPECIAL_DAYS:
        if event["date"] == tomorrow:
            reminders.append(event)
    
    return reminders

def send_email_reminder(to_email, events, smtp_user, smtp_pass):
    """Send email reminder about upcoming scientific events."""
    if not events:
        return
    
    subject = "📅 Upcoming Science Special Days - Reminder"
    
    # Build email body
    body = "Dear Teacher,\n\nHere are the upcoming science/educational special days for your assembly:\n\n"
    
    for event in events:
        body += f"📌 {event['name']} (Tomorrow)\n"
        body += f"   When: {event['date']}\n"
        body += f"   Suggested Talking Points:\n"
        body += f"   {event['description']}\n"
        body += f"   Relevant Subjects: {', '.join(event['subjects'])}\n\n"
    
    body += "Wishing you a successful assembly!\n\n— Your Daily Science Reminder Bot"
    
    # Create message
    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    # Send email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        text = msg.as_string()
        server.sendmail(smtp_user, to_email, text)
        server.quit()
        print(f"✓ Reminder sent to {to_email}")
        return True
    except Exception as e:
        print(f"✗ Failed to send email: {e}")
        return False

def main():
    """Main function to check and send reminders."""
    # Get credentials from environment
    smtp_user = os.getenv("SMTP_USER")  # Email address
    smtp_pass = os.getenv("SMTP_PASS")  # App password
    to_email = os.getenv("TO_EMAIL", smtp_user)  # Recipient email
    
    if not smtp_user or not smtp_pass:
        print("Error: Please set SMTP_USER and SMTP_PASS in .env file")
        return
    
    # Get events for tomorrow
    events = get_reminders_for_today(date.today())
    
    if events:
        print(f"Found {len(events)} event(s) for tomorrow:")
        for event in events:
            print(f"  - {event['name']}")
        send_email_reminder(to_email, events, smtp_user, smtp_pass)
    else:
        print("No events scheduled for tomorrow.")

if __name__ == "__main__":
    main()