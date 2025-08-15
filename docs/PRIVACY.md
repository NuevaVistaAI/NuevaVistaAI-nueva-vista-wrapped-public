# Privacy Policy — Nueva Vista Wrapped

## 🔒 Your Data Stays Local

**Nueva Vista Wrapped processes your ChatGPT export data entirely on your computer. Your conversations never leave your machine.**

---

## What We Do (Local Processing)

### ✅ What Happens on Your Computer
- **Parse conversations.json** — Extract message content and metadata
- **Calculate metrics** — Hours, engagement scores, insights
- **Generate reports** — PDFs, badges, visualizations
- **Store results** — Save outputs to your local filesystem

### ❌ What We Don't Do
- **Upload your data** — No network requests with your conversations
- **Store your data** — No external databases or cloud storage
- **Track your usage** — No analytics or telemetry
- **Share your data** — No third-party access to your exports

---

## Data Flow

```
Your Computer Only:
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ conversations.json │ → │ Local Processing │ → │ Results Files   │
│ (your export)    │    │ (hours, scores) │    │ (on your disk)  │
└─────────────────┐    └─────────────────┘    └─────────────────┘
```

**No data crosses the internet boundary.**

---

## What We Calculate

### From Your Export
- **Message content** — Text of your conversations
- **Timestamps** — When conversations occurred
- **Author roles** — User vs. assistant messages
- **Word counts** — For time calculations

### What We Generate
- **Hours with AI** — Total collaboration time
- **Engagement Score** — Quality and impact metrics
- **Topic analysis** — What you discuss with AI
- **Usage patterns** — When and how you use AI

---

## Optional Features

### Future Premium Features (Opt-in Only)
If we add premium features later, they will:
- **Require explicit consent** — Clear opt-in process
- **Process locally first** — All calculations on your machine
- **Minimize data transfer** — Only send aggregated, anonymized metrics
- **Allow data deletion** — Easy removal of any stored data

### Community Features (If Added)
- **Leaderboards** — Only if you choose to share your score
- **Network access** — Only if you apply and are accepted
- **Benchmarks** — Only aggregated, anonymized statistics

---

## Your Rights

### ✅ You Control Your Data
- **Run locally** — No internet required
- **Delete anytime** — Remove all local files
- **Modify code** — Open source, change anything
- **Audit calculations** — See exactly how scores are computed

### 🔍 Transparency
- **Open source** — All code visible and auditable
- **Clear formulas** — See [TRANSPARENCY.md](TRANSPARENCY.md)
- **No hidden tracking** — No analytics or telemetry
- **Documented assumptions** — Reading/writing speeds explained

---

## Security

### Local Processing Benefits
- **No network exposure** — Data never transmitted
- **No server vulnerabilities** — No external attack surface
- **No data breaches** — Your data stays on your machine
- **No third-party access** — Complete control over your data

### Best Practices
- **Keep exports secure** — Store conversations.json safely
- **Delete when done** — Remove files after analysis
- **Use trusted sources** — Only download from official repos
- **Audit code** — Review before running (it's open source!)

---

## Future Considerations

### If We Add Cloud Features
Any future cloud features will:
- **Maintain local-first** — Local processing remains primary
- **Require explicit opt-in** — No automatic cloud usage
- **Provide clear benefits** — Only add value, not just tracking
- **Allow easy opt-out** — Return to local-only anytime

### Enterprise Features
If we add enterprise features:
- **Separate codebase** — Clear separation from open source
- **Explicit licensing** — Clear commercial terms
- **Data sovereignty** — Respect your data policies
- **Audit trails** — Complete transparency on data usage

---

## Contact

### Questions About Privacy
- **GitHub Issues** — Open an issue in the repo
- **Email** — privacy@nuevavista.ai
- **Documentation** — Check [TRANSPARENCY.md](TRANSPARENCY.md)

### Reporting Concerns
If you find any privacy issues:
1. **Open a GitHub issue** — Public discussion
2. **Email security** — security@nuevavista.ai
3. **Review code** — All processing is visible in the repo

---

## Commitment

**We believe privacy is a feature, not a bug.**

This tool is designed to give you insights about your AI usage while keeping your data completely private. We're committed to maintaining this local-first approach.

---

*Last updated: August 2025*
*Version: 1.0* 