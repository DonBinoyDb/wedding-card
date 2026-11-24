# 💍 Royal Luxury Interactive Wedding Invitation Template

A cinematic, interactive, and mobile-optimized digital wedding invitation card website template featuring a curtain-reveal video intro, background music, scratch-to-reveal engagement card, couple story timeline, venue details, live countdown timer, and personalized RSVP.

---

## 📁 Template Folder Structure

```text
wedding-card-template/
├── index.html          # Main interactive invitation page (HTML, CSS, JS)
├── wedding.ics         # Calendar invite file ("Add to Calendar" button)
├── README.md           # Customization & deployment guide
├── fonts/              # Offline local fonts (Antic Didone, Cormorant, Cinzel, etc.)
└── media/              # Images, video, audio, logos, and graphics
    ├── film-ruby2.mp4       # Intro curtain dance video
    ├── thousandyears.mp3    # Background song
    ├── intro.jpg            # Cover poster before tapping
    ├── Sanjo_Dhiya.svg      # Couple calligraphy names
    ├── logo-sd.png          # Couple monogram
    ├── church.png           # Ceremony venue illustration
    ├── reception.png        # Reception venue illustration
    ├── reveal-photo.png     # Couple photo hidden under the scratch card
    └── ...
```

---

## ✨ Features Included

1. **Tap-to-Unveil Hero Video Intro**:
   - Velvet curtain opening animation and couple dance video (`film-ruby2.mp4`).
   - Bible verse quotation and couple calligraphy names.
   - Glassmorphic golden oval scroll indicator.
2. **Background Audio**:
   - Floating circular golden music player with play/pause animations.
   - Pre-configured to avoid browser autoplay restrictions.
3. **Personalized Guest Links**:
   - Share personalized links with guests: `https://your-domain.com/?g=GuestName`
   - Dynamically personalizes:
     - *"Dear GuestName,"*
     - *"GuestName, your invitation is under the glitter"*
     - Pre-fills the RSVP guest name field.
4. **Interactive Scratch-to-Reveal Card**:
   - Interactive gold foil scratch card that reveals the couple's photo and *"Forever Begins"* message.
   - Works with touch on mobile and mouse on desktop.
5. **Love Story Timeline**:
   - Elegant illustrated story milestones from first meeting to engagement.
6. **Venue Details & Navigation**:
   - Church ceremony and reception venue cards with timings and Google Maps directions.
7. **Live Wedding Countdown**:
   - Real-time countdown to the wedding ceremony date (Days, Hours, Minutes).
8. **RSVP & Add to Calendar**:
   - RSVP attendance form with confirmation screen.
   - One-click `.ics` calendar file download for Google Calendar, Apple Calendar, and Outlook.

---

## 🛠️ How to Customize This Template

### 1. Couple Information & Event Times
Open [index.html](file:///index.html) in any text or code editor (e.g. VS Code, Notepad) and find the `EVENT` configuration around line **2950**:

```javascript
var EVENT = {
  start: '2027-01-10T15:00:00',   // Ceremony start time (YYYY-MM-DDTHH:mm:ss)
  end: '2027-01-10T23:00:00',     // Reception end time
  title: 'Sanjo & Dhiya Wedding', // Event title in calendar
  place: 'St. Joseph Church Mankavu & Capkon City Pantheerankavu',
  map: 'St.+Joseph+Church+Mankavu', // Search query for Google Maps link
  namesAt: 2.2                    // Second of intro video when names appear
};
```

### 2. Replace Couple Names & Monogram
- **Calligraphy Name SVG**: Replace `media/Sanjo_Dhiya.svg` with your own vector names or SVG text.
- **Monogram Logo**: Replace `media/logo-sd.png` with your own monogram or initials.

### 3. Replace Photos, Video & Music
- **Intro Video**: Place your MP4 video at `media/film-ruby2.mp4` (recommended: H.264 MP4, ~2–4MB for fast mobile loading).
- **Background Song**: Replace `media/thousandyears.mp3` with your favorite song.
- **Intro Poster**: Replace `media/intro.jpg` with the first frame of your video or cover photo.
- **Scratch Card Photo**: Replace `media/reveal-photo.png` with your couple photo.
- **Venue Images**: Replace `media/church.png` and `media/reception.png` with your venue illustrations or photos.

### 4. Calendar File (`wedding.ics`)
Open `wedding.ics` and update the date, time, location, and description:
```ics
DTSTART:20270110T093000Z
DTEND:20270110T173000Z
SUMMARY:Sanjo & Dhiya Wedding
LOCATION:St. Joseph Church Mankavu
```

---

## 🚀 How to Host & Share Online (100% Free)

You can host this static template for free on any of these platforms:

### Option A: GitHub Pages (Recommended)
1. Create a free repository on [GitHub](https://github.com).
2. Upload the contents of this template folder into the repository.
3. In repository **Settings** → **Pages**, select branch `main` and root `/`, then click **Save**.
4. Your invitation will be live in 1 minute at `https://your-username.github.io/your-repo/`.

### Option B: Netlify / Vercel (Drag-and-Drop)
1. Go to [Netlify Drop](https://app.netlify.com/drop).
2. Drag and drop the `wedding-card-template` folder into your browser.
3. Your site is instantly live with a free SSL certificate!

---

## 💌 Sending Personalized Links
To address an invitation directly to a guest, append `?g=GuestName` to your live website URL:

- `https://your-domain.com/?g=Uncle+John`
- `https://your-domain.com/?g=Sarah+and+David`
- `https://your-domain.com/?g=The+Mathew+Family`
