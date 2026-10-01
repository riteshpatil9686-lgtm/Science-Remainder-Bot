# FREE Google Apps Script Setup (No Laptop Needed!)

## Step 1: Open Google Apps Script
- Go to: https://script.google.com
- Click "New Project"

## Step 2: Copy the Code
- Delete the default `myFunction()`
- Copy the code from `google_apps_script.js` in this folder
- Change `YOUR-MOMS-EMAIL@gmail.com` to your mom's email

## Step 3: Save the Project
- Click "Save" (disk icon) or press Ctrl+S
- Name it: `Science Reminder Bot`

## Step 4: Authorize It
- Click the "Run" button (play icon ▶)
- First time: Click "Review Permissions"
- Choose your Google account → Click "Advanced" → "Go to..." → Click "Allow"

## Step 5: Add Daily Trigger (Automatic!)
- Click the clock icon ⏰ (Triggers) on the left
- Click "+ Add Trigger"
- Choose function: `sendScienceReminder`
- Event source: `Time-driven`
- Type: `Day timer`
- Time: `6:00 PM to 7:00 PM` (or pick any hour)
- Click "Save"

## Done!
The bot now runs EVERY DAY at your chosen time on Google's servers — even when laptop is OFF.

## To Add Events
Edit the `events` array in the code:
```javascript
{
  name: "Event Name",
  date: "2026-10-02",  // YYYY-MM-DD
  talk: "What your mom should say in assembly",
  subjects: "Physics, Chemistry, Biology"
}
```

## To Check If It Works
- In Google Apps Script, click "Run" manually
- Check your mom's email
