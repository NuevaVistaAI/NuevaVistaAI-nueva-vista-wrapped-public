# Nueva Vista Wrapped

**Find your Hours with AI and your AI Engagement Score locally, privately.**

Nueva Vista Wrapped is a privacy-first analytics toolkit for ChatGPT users.  
It gives you two key insights from your ChatGPT export:

- **Hours with AI** Your total collaboration time (viral badge for sharing)
- **AI Engagement Score** A private metric that measures quality & impact

Everything runs **locally** on your machine. Your data never leaves your computer.

---

## 🚀 Quick Start

1. **Export your data from ChatGPT**
   - Go to Settings → Data Controls → Export Data
   - Download the ZIP from your email and extract it
   - Find the `conversations.json` file

2. **Clone this repo**
   ```bash
   git clone https://github.com/NuevaVistaAI/nueva-vista-wrapped.git
   cd nueva-vista-wrapped
   ```

3. **Install dependencies**
   ```bash
   pip install -r apps/cli/requirements.txt
   ```

4. **Get your hours badge (free)**
   ```bash
   python apps/cli/nv_quick_hours.py /path/to/conversations.json
   ```

5. **Get your engagement score (free)**
   ```bash
   python apps/cli/nv_engagement_score.py /path/to/conversations.json
   ```

---

## 📊 Example Output

```
🏆 AI Pioneer (100+ hours)
Hours with AI: 694.1 hrs (range 517.5–936.6)
Messages you wrote: 6,417
AI replies read: 11,228

⚡ AI Engagement Score: 53.5/100
🎯 Quality Explorer
```

---

## ✨ Features

### **Hours Badge** (Free & Viral)
- **Quick calculation** Get your hours in seconds
- **Shareable format** Perfect for social media
- **Confidence ranges** Account for reading/writing speeds
- **Badge levels** AI Legend, Pioneer, Explorer, etc.

### **Engagement Score** (Free & Private)
- **Topic Diversity** How many different areas you explore
- **Interaction Depth** Quality of your conversations
- **Creation Output** Tangible deliverables generated
- **Efficiency Ratio** Balance of speed vs. depth

---

## 🏗️ Repository Structure

```
nueva-vista-wrapped/
├── apps/
│   └── cli/                      # Command-line tools (free)
│       ├── nv_quick_hours.py     # Quick hours badge
│       ├── nv_engagement_score.py # Engagement scoring
│       └── requirements.txt      # Dependencies
├── docs/
│   ├── PRIVACY.md               # Privacy commitments
│   ├── TRANSPARENCY.md          # How we calculate
│   └── ROADMAP.md              # Future plans
├── tests/
│   └── sample_conversations.json # Test data
└── scripts/
    └── helpers.py              # Utility functions
```

---

## 🔒 Privacy First

- **100% local processing** Your data never leaves your computer
- **No uploads** All calculations happen on your machine
- **No tracking** No analytics or telemetry
- **Open source** Review every line of code

See [PRIVACY.md](docs/PRIVACY.md) for complete details.

---

## 📚 Documentation

- **[PRIVACY.md](docs/PRIVACY.md)** Privacy commitments
- **[TRANSPARENCY.md](docs/TRANSPARENCY.md)** Data & assumptions
- **[ROADMAP.md](docs/ROADMAP.md)** Future features

---

## 🎯 Use Cases

### **For Individuals**
- **Share your AI journey** Viral hours badge
- **Understand your patterns** Private engagement insights
- **Track your growth** Year-over-year improvement

### **For Teams** (Future)
- **Benchmark AI adoption** Team engagement metrics
- **Identify power users** High-impact collaborators
- **Training insights** AI usage patterns

---

## 🚀 Campaign: #NuevaVistaWrapped

### Share Your Hours
```
🏆 AI Legend (500+ hours)

I've spent 694.1 hours building with AI!

📊 Key Stats:
• 6,417 messages written
• 11,228 AI replies read
• 794K words written
• 2.1M words read

#NuevaVistaWrapped
```

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
```bash
git clone https://github.com/NuevaVistaAI/nueva-vista-wrapped.git
cd nueva-vista-wrapped
pip install -r apps/cli/requirements.txt
python apps/cli/nv_quick_hours.py --help
```

### Testing
```bash
# Test with sample data
python apps/cli/nv_quick_hours.py tests/sample_conversations.json
python apps/cli/nv_engagement_score.py tests/sample_conversations.json
```

---

## 📝 License

- **Core code**: Apache-2.0 License
- **Branding**: Nueva Vista trademarks apply

---

## 🗺️ Roadmap

### **Phase 1** (Current)
- CLI tools for hours and engagement
- Privacy-first local processing
- Transparent calculations
- Viral sharing capabilities

### **Phase 2** (Coming Soon)
- Web UI for drag-and-drop analysis
- Interactive visualizations
- Advanced analytics
- Mobile-friendly sharing

### **Phase 3** (Future)
- Multi-platform AI analytics
- Enterprise features
- Team collaboration tools
- API access

---

## 📞 Support

- **GitHub Issues** Bug reports and feature requests
- **Documentation** Check the docs/ folder
- **Email** [hello@nuevavista.ai](mailto:hello@nuevavista.ai)

---

## 🙏 Acknowledgments

- **OpenAI** For ChatGPT and export functionality
- **Community** Early testers and feedback
- **Contributors** Code improvements and suggestions

---

*Built with ❤️ by Nueva Vista Labs*  
*Building the future of AI collaboration*
