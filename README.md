# Nueva Vista Wrapped  
**Find your Hours with AI and your AI Engagement Score — locally, privately.**  

Nueva Vista Wrapped is a privacy-first analytics toolkit for ChatGPT users.  
It gives you two key insights from your ChatGPT export:  

- **⏱ Hours with AI** — Your total collaboration time (viral badge for sharing)  
- **🎯 AI Engagement Score** — A private metric that measures quality & impact  

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
python apps/cli/nv_engagement_score.py /path/to/conversations.json --ijson
```

---

## 📊 Example Output

```
🏆 AI Pioneer (100+ hours)
Hours with AI: 694.1 hrs (range 517.5–936.6)
Messages you wrote: 6,417
AI replies read: 11,228

🎯 AI Engagement Score: 53.5/100
📊 Quality Explorer
```

---

## 🎯 Features

### 🕒 **Hours Badge** (Free & Viral)
- **Quick calculation** — Get your hours in seconds
- **Shareable format** — Perfect for social media
- **Confidence ranges** — Account for reading/writing speeds
- **Badge levels** — AI Legend, Pioneer, Explorer, etc.

### 📊 **Engagement Score** (Free & Private)
- **Topic Diversity** — How many different areas you explore
- **Interaction Depth** — Quality of your conversations
- **Creation Output** — Tangible deliverables generated
- **Efficiency Ratio** — Balance of speed vs. depth

### 🔍 **Advanced Insights** (Free)
- **Temporal patterns** — When you're most active
- **Behavioral analysis** — How you use AI
- **Growth tracking** — Your AI journey over time
- **Personalized recommendations** — How to improve

---

## 📁 Repository Structure

```
nueva-vista-wrapped/
├─ apps/
│  ├─ cli/                      # Command-line tools (free)
│  │  ├─ nv_quick_hours.py     # Quick hours badge
│  │  ├─ nv_engagement_score.py # Engagement scoring
│  │  ├─ nv_advanced_insights.py # Deep analysis
│  │  └─ requirements.txt       # Dependencies
│  └─ web/                      # Web UI (coming soon)
├─ docs/
│  ├─ TRANSPARENCY.md           # How we calculate
│  ├─ PRIVACY.md               # Privacy commitments
│  ├─ SCORE_METHOD.md          # Engagement formula
│  └─ ROADMAP.md               # Future plans
├─ pro-hooks/                   # Future premium features
└─ scripts/                     # Helper utilities
```

---

## 🔒 Privacy First

- **100% local processing** — Your data never leaves your computer
- **No uploads** — All calculations happen on your machine
- **No tracking** — No analytics or telemetry
- **Open source** — Review every line of code

See [PRIVACY.md](docs/PRIVACY.md) for complete details.

---

## 📖 Documentation

- **[TRANSPARENCY.md](docs/TRANSPARENCY.md)** — Data & assumptions
- **[SCORE_METHOD.md](docs/SCORE_METHOD.md)** — Engagement Score formula
- **[PRIVACY.md](docs/PRIVACY.md)** — Privacy commitments
- **[ROADMAP.md](docs/ROADMAP.md)** — Future features

---

## 🎯 Use Cases

### **For Individuals**
- **Share your AI journey** — Viral hours badge
- **Understand your patterns** — Private engagement insights
- **Track your growth** — Year-over-year improvement
- **Optimize your usage** — Personalized recommendations

### **For Teams** (Future)
- **Benchmark AI adoption** — Team engagement metrics
- **Identify power users** — High-impact collaborators
- **Training insights** — AI usage patterns
- **ROI measurement** — Time investment vs. output

### **For Organizations** (Future)
- **Enterprise analytics** — Company-wide AI usage
- **Learning & development** — AI training programs
- **Productivity insights** — AI collaboration patterns
- **Strategic planning** — AI adoption roadmaps

---

## 🚀 Campaign: #NuevaVistaWrapped

### **Share Your Hours**
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

### **Get Your Engagement Score**
Want to know how effectively you use AI? Run the engagement analysis for personalized insights about your AI collaboration style.

---

## 🏆 AI Builder Network

High-engagement users may qualify for our exclusive AI Builder Network:
- **Direct access** to Nueva Vista team
- **Collaboration opportunities** with other power users
- **Early access** to new features and tools
- **Exclusive content** and strategies

*Apply through the engagement score analysis.*

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### **Development Setup**
```bash
git clone https://github.com/NuevaVistaAI/nueva-vista-wrapped.git
cd nueva-vista-wrapped
pip install -r apps/cli/requirements.txt
python apps/cli/nv_quick_hours.py --help
```

### **Testing**
```bash
# Test with sample data
python apps/cli/nv_quick_hours.py tests/sample_conversations.json
python apps/cli/nv_engagement_score.py tests/sample_conversations.json
```

---

## 📄 License

- **Core code**: Apache-2.0 License
- **Pro features**: Reserved for future commercial licensing
- **Branding**: Nueva Vista trademarks apply

---

## 🎯 Roadmap

### **Phase 1** (Current)
- ✅ CLI tools for hours and engagement
- ✅ Privacy-first local processing
- ✅ Transparent calculations
- ✅ Viral sharing capabilities

### **Phase 2** (Coming Soon)
- 🌐 Web UI for drag-and-drop analysis
- 📊 Interactive visualizations
- 🏆 AI Builder Network launch
- 📱 Mobile-friendly sharing

### **Phase 3** (Future)
- 💼 Enterprise features
- 🤝 Team collaboration tools
- 📈 Advanced analytics
- 🔗 API access

---

## 📞 Support

- **GitHub Issues** — Bug reports and feature requests
- **Documentation** — Check the docs/ folder
- **Community** — Join the AI Builder Network
- **Email** — hello@nuevavista.ai

---

## 🙏 Acknowledgments

- **OpenAI** — For ChatGPT and export functionality
- **Community** — Early testers and feedback
- **Contributors** — Code improvements and suggestions

---

*Built with ❤️ by Nueva Vista — Building the future of AI collaboration* 