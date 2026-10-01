// Google Apps Script - PRIMARY FREE BOT
// Runs on Google's servers 24/7 - laptop off OK!

function sendScienceReminder() {
  // ALL EVENTS FROM PYTHON SCRIPT - 2026-2027
  var events = [
    // January 2026
    {name: "World Braille Day", date: "2026-01-04", talk: "Accessibility through science: Braille system, neuroscience of touch, materials science.", subjects: "Biology, Physics, Engineering"},
    {name: "International Day of Education", date: "2026-01-24", talk: "STEM literacy empowers communities to solve local challenges.", subjects: "Physics, Chemistry, Biology"},
    {name: "International Day of Clean Energy", date: "2026-01-26", talk: "Solar PV, wind turbine aerodynamics, battery storage chemistry, grid integration.", subjects: "Physics, Chemistry, Engineering"},
    {name: "World Neglected Tropical Diseases Day", date: "2026-01-30", talk: "Dengue, chikungunya, leprosy: parasite biology, vaccine chemistry, diagnostics.", subjects: "Biology, Chemistry, Health Science"},
    // February 2026
    {name: "World Wetlands Day", date: "2026-02-02", talk: "Wetland ecosystems: biodiversity, carbon sinks, mangrove biology, peat soil chemistry.", subjects: "Biology, Chemistry, Environmental"},
    {name: "International Day of Women & Girls in Science", date: "2026-02-11", talk: "Marie Curie, Tessy Thomas (Agni missile), Gagandeep Kang (virology). Gender equity.", subjects: "Physics, Chemistry, Biology"},
    {name: "Darwin Day", date: "2026-02-12", talk: "Evolution by natural selection, common descent, fossil to DNA evidence.", subjects: "Biology, Genetics, Evolution"},
    {name: "World Radio Day", date: "2026-02-13", talk: "EM waves, modulation, antenna design. Marconi, MRI physics, wireless evolution.", subjects: "Physics, Engineering"},
    {name: "National Science Day - C.V. Raman", date: "2026-02-28", talk: "Raman Effect (1928): light scattering reveals molecular vibrations. Nobel 1930. Spectroscopy.", subjects: "Physics, Chemistry"},
    // March 2026
    {name: "World Wildlife Day", date: "2026-03-03", talk: "Biodiversity conservation: extinction rates, CITES, genetics, ecology.", subjects: "Biology, Environmental"},
    {name: "World Engineering Day", date: "2026-03-04", talk: "Engineering applies science: bridges, engines, chemical processes, circuits.", subjects: "Physics, Chemistry, Engineering"},
    {name: "Pi Day / Math Day", date: "2026-03-14", talk: "Pi (π) in physics (waves), chemistry (orbitals), biology (DNA, population).", subjects: "Physics, Chemistry, Biology, Math"},
    {name: "World Water Day", date: "2026-03-22", talk: "Water's properties: hydrogen bonding, universal solvent, cycle, conservation.", subjects: "Chemistry, Biology, Environmental"},
    // April 2026
    {name: "World Health Day", date: "2026-04-07", talk: "Vaccines, antibiotics, disease prevention, health systems.", subjects: "Biology, Chemistry, Health"},
    {name: "Aryabhata Launch Anniversary", date: "2026-04-19", talk: "India's first satellite (1975): X-ray astronomy, aerospace, telemetry.", subjects: "Physics, Engineering, Space"},
    {name: "Earth Day", date: "2026-04-22", talk: "Planetary boundaries: climate, biodiversity, biogeochemical cycles.", subjects: "Biology, Chemistry, Physics, Environmental"},
    {name: "DNA Day", date: "2026-04-25", talk: "Double helix (1953), Human Genome Project, CRISPR, biotechnology.", subjects: "Biology, Chemistry, Genetics"},
    // May 2026
    {name: "National Technology Day", date: "2026-05-11", talk: "Pokhran-II (1998): India's nuclear self-reliance. Dr. Kalam's leadership.", subjects: "Physics, Chemistry, Engineering"},
    {name: "International Day of Light", date: "2026-05-16", talk: "Wave-particle duality, lasers, spectroscopy, photosynthesis.", subjects: "Physics, Chemistry, Biology"},
    {name: "International Day for Biological Diversity", date: "2026-05-22", talk: "Biodiversity loss, ecosystem services, 30x30 conservation goal.", subjects: "Biology, Environmental"},
    {name: "World No Tobacco Day", date: "2026-05-31", talk: "Nicotine addiction, lung cancer biology, cardiovascular chemistry.", subjects: "Biology, Chemistry, Health"},
    // June 2026
    {name: "World Environment Day", date: "2026-06-05", talk: "Climate science: carbon cycle, greenhouse gases, renewable energy.", subjects: "Chemistry, Biology, Physics, Environmental"},
    {name: "World Oceans Day", date: "2026-06-08", talk: "Ocean acidification, marine biodiversity, plastic pollution.", subjects: "Chemistry, Biology, Physics, Environmental"},
    // July 2026
    {name: "Chandrayaan-2 Launch Anniversary", date: "2026-07-22", talk: "India's lunar mission: orbiter, lander Vikram, rover Pragyan. Lunar chemistry.", subjects: "Physics, Chemistry, Space"},
    // August 2026
    {name: "Vikram Sarabhai Birth Anniversary", date: "2026-08-12", talk: "Father of Indian Space Program (born 1919). ISRO founding, satellite technology.", subjects: "Physics, Space Science"},
    {name: "National Space Day - Chandrayaan-3", date: "2026-08-23", talk: "Chandrayaan-3 landing (2023): Vikram lander, Pragyan rover, lunar regolith.", subjects: "Physics, Chemistry, Space"},
    // September 2026
    {name: "Aditya-L1 Launch Anniversary", date: "2026-09-02", talk: "India's first solar observatory: L1 orbit, solar corona, space weather.", subjects: "Physics, Space"},
    {name: "World Ozone Day", date: "2026-09-16", talk: "Montreal Protocol: CFC phase-out, ozone healing, UV radiation.", subjects: "Chemistry, Physics, Biology"},
    // October 2026
    {name: "World Space Week Begins", date: "2026-10-04", talk: "Oct 4-10: Space science, satellite applications, international cooperation.", subjects: "Physics, Engineering, Space"},
    {name: "APJ Abdul Kalam Birth Anniversary", date: "2026-10-15", talk: "Missile Man of India (born 1931): Aerospace, nuclear physics, science education.", subjects: "Physics, Engineering, Aerospace"},
    {name: "PSLV First Successful Flight", date: "2026-10-15", talk: "PSLV-D2 (1994): First operational flight. Indian satellite launch workhorse.", subjects: "Physics, Engineering, Space"},
    {name: "Homi Bhabha Birth Anniversary", date: "2026-10-30", talk: "Father of Indian Nuclear Program (born 1909): BARC, cosmic rays, nuclear vision.", subjects: "Physics, Nuclear Science"},
    // November 2026
    {name: "Mangalyaan Launch Anniversary", date: "2026-11-05", talk: "India's first Mars mission (2013): Orbiter study of Mars surface, atmosphere.", subjects: "Physics, Chemistry, Space"},
    {name: "C.V. Raman Birth Anniversary", date: "2026-11-07", talk: "Nobel physicist Raman (born 1888): Raman Effect - molecular spectroscopy foundation.", subjects: "Physics, Chemistry"},
    {name: "World Science Day", date: "2026-11-10", talk: "UNESCO: Science for peace, open science, international cooperation for SDGs.", subjects: "Physics, Chemistry, Biology"},
    // December 2026
    {name: "World Soil Day", date: "2026-12-05", talk: "Soil chemistry, microbiome, physics of erosion, nutrient cycling.", subjects: "Chemistry, Biology, Physics, Environmental"},
    {name: "National Mathematics Day - Ramanujan", date: "2026-12-22", talk: "Mathematical genius (born 1887): Infinite series, number theory, 1729 number.", subjects: "Mathematics, Physics, Chemistry"},
    // January 2027
    {name: "XPoSat Launch Anniversary", date: "2027-01-01", talk: "India's first polarimetry mission (2024): X-ray polarization from cosmic sources.", subjects: "Physics, Space"},
    // February 2027
    {name: "National Science Day - C.V. Raman", date: "2027-02-28", talk: "Raman Effect discovery (1928). Light scattering proves molecular vibrations.", subjects: "Physics, Chemistry"}
  ];

  // Check tomorrow's events
  var tomorrow = new Date();
  tomorrow.setDate(tomorrow.getDate() + 1);
  var tomorrowStr = Utilities.formatDate(tomorrow, Session.getScriptTimeZone(), "yyyy-MM-dd");

  var reminders = events.filter(function(e) {
    return e.date === tomorrowStr;
  });

  if (reminders.length > 0) {
    var body = "Dear Teacher,\n\nScience reminder for tomorrow (" + tomorrowStr + "):\n\n";
    reminders.forEach(function(r) {
      body += "📌 " + r.name + "\n";
      body += "   Talking points: " + r.talk + "\n";
      body += "   Relevant subjects: " + r.subjects + "\n\n";
    });
    body += "Wishing you a great assembly!\n— Your Science Reminder Bot (Free Google Version)";

    MailApp.sendEmail({
      to: "YOUR-MOMS-EMAIL@gmail.com",  // ⚡ CHANGE THIS TO MOM'S EMAIL
      subject: "📅 Tomorrow's Science Special Day Reminder",
      body: body
    });
  }
}
