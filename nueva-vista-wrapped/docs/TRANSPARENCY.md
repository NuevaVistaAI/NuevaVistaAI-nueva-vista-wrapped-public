# Transparency - How Nueva Vista Wrapped Works

## Our Calculation Methods

**Complete transparency in how we analyze your AI collaboration data.**

### Hours Calculation

**Reading Time:**
- Default: 220 words per minute (average adult reading speed)
- Range: 180-260 WPM for confidence intervals
- Applied to: All AI responses you read

**Writing Time:**
- Default: 25 words per minute (average typing with thinking)
- Range: 18-35 WPM for confidence intervals  
- Applied to: All messages you wrote to AI

**Total Hours = (Your Words ÷ Writing Speed) + (AI Words ÷ Reading Speed)**

### Badge Tiers

**AI Legend:** 500+ hours  
**AI Pioneer:** 250+ hours  
**AI Explorer:** 100+ hours  
**AI Apprentice:** 50+ hours  
**AI Curious:** 10+ hours  
**AI Newcomer:** Getting started  

*Tiers based on analysis of early adopter usage patterns*

### Engagement Score Components

**Conversation Depth (25 points):**
- Measures average messages per conversation
- 20+ messages = full points
- Rewards sustained discussions

**Vocabulary Diversity (20 points):**
- Unique words per conversation
- 100+ unique words = full points
- Indicates topic exploration

**Interaction Quality (25 points):**
- Questions, requests, and engagement patterns
- Based on linguistic analysis of your messages
- Rewards active participation

**Engagement Consistency (15 points):**
- Messages per conversation ratio
- 10+ messages per conversation = full points
- Indicates regular deep usage

**Response Utilization (15 points):**
- AI responses per your message
- Rewards following up on AI responses
- Caps at reasonable ratios

### Data Processing

**What We Analyze:**
- Message text (word counting and pattern recognition)
- Message timestamps (for timeline analysis)
- Message roles (user vs assistant)
- Conversation structure (from ChatGPT export format)

**What We Ignore:**
- Image attachments (not processed)
- File uploads (not analyzed)
- System messages (filtered out)
- Empty or malformed messages

### Word Tokenization

**Included in word counts:**
- Regular text words
- Technical terms
- Numbers when part of text

**Excluded from word counts:**
- Code blocks (marked with ``` in ChatGPT)
- URLs and links
- Repeated punctuation
- Empty messages

### Assumptions & Limitations

**Reading Speed Assumptions:**
- Based on adult reading comprehension studies
- Assumes you read all AI responses fully
- Does not account for skimming vs deep reading

**Writing Speed Assumptions:**
- Includes thinking/composition time
- Based on studies of writing with thinking
- Varies significantly by individual

**ChatGPT Export Limitations:**
- Only processes conversations you exported
- Cannot analyze deleted conversations
- Timestamps may have timezone variations

**Scope Limitations:**
- **ChatGPT only** - does not include Claude, Gemini, Perplexity, etc.
- **Text only** - does not analyze image/file interactions
- **Individual only** - does not analyze team or shared conversations

### Confidence Intervals

**Why we show ranges:**
- Reading speeds vary 180-260 WPM between individuals
- Writing speeds vary 18-35 WPM based on complexity
- Provides honest uncertainty bounds

**How to interpret:**
- Lower bound: You're a fast reader/writer
- Upper bound: You're more contemplative
- Middle estimate: Population averages

### Validation Methods

**Self-consistency checks:**
- Total messages should equal user + AI messages
- Word counts should be positive
- Timestamps should be chronological

**Sanity bounds:**
- Extremely high hours (1000+) trigger warnings
- Very low engagement scores suggest data issues
- Missing data produces clear error messages

### Open Source Verification

**Code transparency:**
- All calculation methods are in the source code
- No hidden algorithms or proprietary methods
- Community can verify and improve methods

**Reproducible results:**
- Same data input always produces same output
- No random elements in calculations
- Deterministic processing

### Future Improvements

**Planned enhancements:**
- Multi-platform analysis (Claude, Gemini, etc.)
- Improved engagement pattern recognition
- Better handling of code vs text
- Temporal pattern analysis

**Community feedback:**
- Report calculation issues on GitHub
- Suggest improvements to methodology
- Contribute better algorithms

---

## Questions About Our Methods?

**Technical questions:** [Open a GitHub issue](https://github.com/nuevavistalabs/nueva-vista-wrapped/issues)  
**Methodology questions:** [hello@nuevavista.ai](mailto:hello@nuevavista.ai)

---

*Last updated: August 15, 2025*  
*Nueva Vista Labs - Transparent by Design*
