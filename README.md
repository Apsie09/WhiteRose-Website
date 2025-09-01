# White Rose - The Energy Tree
## Django + Tailwind Website

### 🚀 Quick Start

1. **Activate the conda environment:**
   ```bash
   conda activate whiterose
   ```

2. **Start the development server:**
   ```bash
   cd /home/asen/WhiteRose
   python manage.py runserver
   ```

3. **Visit the site:**
   Open http://127.0.0.1:8000 in your browser

### 📁 Project Structure

```
WhiteRose/
├── whiterose_site/          # Django project settings
│   ├── settings.py          # Configuration with env variables
│   └── urls.py              # Main URL routing
├── pages/                   # Main app
│   ├── views.py             # Page views and contact form
│   ├── urls.py              # App URL routing
│   ├── forms.py             # Contact form
│   └── templates/           # All templates
│       ├── base.html        # Base template with Tailwind
│       ├── home.html        # Homepage with all content
│       ├── technology.html   # Technology overview
│       ├── applications.html # Use cases and applications
│       ├── partners.html    # Partnership information
│       ├── about.html       # Team and mission
│       ├── contact.html     # Contact form
│       ├── privacy.html     # Privacy policy
│       └── components/      # Reusable components
│           ├── navbar.html  # Navigation with mobile menu
│           ├── footer.html  # Footer with contact info
│           ├── card.html    # Card component
│           └── faq.html     # FAQ component
├── static/                  # Static files
│   ├── css/
│   │   └── site.css         # Custom CSS with color variables
│   ├── img/                 # Placeholder images
│   └── docs/                # PDF documents
└── .env                     # Environment variables
```

### 🎨 Features Implemented

✅ **Complete Django Setup**
- Python 3.12 + Django 5.2.5
- Environment variables with python-dotenv
- Production-ready settings structure

✅ **Responsive Design**
- Tailwind CSS via CDN
- Custom color palette (mint, leaf, teal, midnight, etc.)
- Mobile-first responsive design
- Inter font integration

✅ **Complete Website Pages**
- **Homepage**: Hero, value props, technology overview, gallery, use cases, impact, partners, FAQ
- **Technology**: Detailed tech features with recycled components info
- **Applications**: Use cases with scenarios (parks, campuses, residential)
- **Partners**: Business model, partnership types, value co-creation
- **About**: Team profiles, TU-Sofia affiliation, mission/vision
- **Contact**: Working contact form with validation
- **Privacy**: GDPR-compliant privacy policy

✅ **Navigation & Components**
- Responsive navbar with mobile hamburger menu
- Footer with team emails and TU-Sofia address
- Reusable card and FAQ components
- Smooth transitions and hover effects

✅ **Contact Form**
- Django forms with validation
- Email backend (console output for development)
- Success messages
- CSRF protection

✅ **SEO & Meta**
- Proper title tags and meta descriptions
- OpenGraph and Twitter Card meta tags
- Sitemap.xml and robots.txt endpoints
- Favicon placeholders

✅ **Content Integration**
- All provided project content integrated
- Team member information with roles
- Technical specifications and benefits
- Partnership and business model details
- FAQ section with key questions

### 🎯 Routes Available

- `/` - Homepage
- `/technology/` - Technology overview
- `/applications/` - Applications and use cases
- `/partners/` - Partnership information
- `/about/` - Team and company info
- `/contact/` - Contact form
- `/privacy/` - Privacy policy
- `/sitemap.xml` - XML sitemap
- `/robots.txt` - Robots file

### 🔧 Environment Variables

Edit `.env` file for configuration:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 📝 To-Do for Production

1. **Replace placeholder images** in `/static/img/`
2. **Add actual PDF resume** at `/static/docs/White Rose resume EN.pdf`
3. **Update environment variables** for production
4. **Configure email backend** for contact form
5. **Add partner logos** in partners page
6. **Optimize images** and add proper alt texts
7. **Set up SSL** and security headers
8. **Configure static file serving** for production

### 💻 Development Commands

```bash
# Activate environment
conda activate whiterose

# Run development server
python manage.py runserver

# Check for issues
python manage.py check

# Create migrations (if needed)
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files (for production)
python manage.py collectstatic
```

### 📧 Contact Form Testing

The contact form prints submissions to the console when running the development server. Check the terminal output after form submissions.

### 🎨 Color Palette

- **Mint**: #DDF4E7 (light green backgrounds)
- **Leaf**: #67C090 (primary green buttons)
- **Teal**: #26667F (accent color)
- **Midnight**: #124170 (dark blue headings)
- **Paper**: #FFFFFF (white backgrounds)
- **Ink**: #0B1020 (dark text)
- **Soft**: #EEF3F1 (light backgrounds)

The site is fully functional and ready for content updates and deployment!
