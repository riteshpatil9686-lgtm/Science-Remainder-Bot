// Google Apps Script - FREE Science Reminder Bot
// Runs on Google's servers - no laptop needed!

function sendScienceReminder() {
  // List of science events for tomorrow
  var events = [
    {
      name: "TEST EVENT - Tomorrow's Check",
      date: "2026-10-02",
      talk: "This is a test reminder. If received, the bot works correctly!",
      subjects: "Physics, Chemistry, Biology"
    }
  ];

  // Send email
  var tomorrow = new Date();
  tomorrow.setDate(tomorrow.getDate() + 1);
  var tomorrowStr = Utilities.formatDate(tomorrow, Session.getScriptTimeZone(), "yyyy-MM-dd");

  // Filter events for tomorrow
  var reminders = events.filter(function(e) { return e.date === tomorrowStr; });

  if (reminders.length > 0) {
    var body = "Dear Teacher,\n\nScience reminder for tomorrow:\n\n";
    reminders.forEach(function(r) {
      body += "📌 " + r.name + " (Tomorrow)\n";
      body += "   Talking points: " + r.talk + "\n";
      body += "   Subjects: " + r.subjects + "\n\n";
    });
    body += "Wishing you a great assembly!\n— Your Science Reminder Bot";

    MailApp.sendEmail({
      to: "YOUR-MOMS-EMAIL@gmail.com",  // CHANGE THIS
      subject: "📅 Tomorrow's Science Special Day Reminder",
      body: body
    });
  }
}
