
# 🧠 Reddit User Persona Generator

This project was built as part of the **Generative AI Internship Assignment** at **BeyondChats**.

It takes a Reddit username, scrapes all available posts and comments, and uses a **Groq-hosted open-source LLM** (like Mixtral or LLaMA 3) to generate a detailed **user persona** with **citations** from the Reddit content.

---

## 🚀 Features

- ✅ Scrapes all comments and posts from a given Reddit user
- ✅ Uses Groq-hosted LLMs to infer behavioral traits
- ✅ Generates personas including:
  - Interests
  - Writing style
  - Ideology
  - Humor/sarcasm
  - Emotional tone
- ✅ Cites Reddit posts/comments used for inference
- ✅ Graceful error handling (invalid users, empty content, API issues)

---

## 🧰 Tech Stack

| Tool            | Purpose                                     |
|-----------------|---------------------------------------------|
| Python          | Core language                              |
| PRAW            | Reddit scraping via Reddit API             |
| Groq SDK        | Access Mixtral, LLaMA 3 via Groq platform  |
| python-dotenv   | Secure API key management                  |
| argparse        | Command-line interface                     |
| tqdm (optional) | Progress display for chunked prompts       |

---

## 📁 Project Structure

```
reddit_persona_generator/
├── persona_generator.py         # Main entry point
├── reddit_scraper.py            # Fetches Reddit posts & comments
├── groq_persona_builder.py      # Handles persona generation using Groq LLM
├── requirements.txt             # Python dependencies
├── .env                         # Store Groq & Reddit API keys (excluded from Git)
├── README.md                    # Project documentation
└── sample_output/               # Generated persona files
    ├── kojied_persona.txt
    └── Hungry-Move-6603_persona.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root folder:

\`\`\`env
GROQ_API_KEY=your_groq_api_key
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_secret
\`\`\`

> ✅ [Get Groq key](https://console.groq.com)  
> ✅ [Create Reddit app](https://www.reddit.com/prefs/apps) → choose "script" app

---

## ⚙️ Installation & Setup

### 1. Clone the repository

\`\`\`bash
git clone https://github.com/yourusername/reddit-persona-generator.git
cd reddit-persona-generator
\`\`\`

### 2. Install dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Add your `.env` credentials

(see `.env` example above)

---

## 🧪 How to Use

To generate a persona for any Reddit user:

\`\`\`bash
python persona_generator.py --username kojied
\`\`\`

This will:
- Scrape the user's Reddit activity
- Generate a detailed persona using Groq LLM
- Save the output to `sample_output/kojied_persona.txt`

---

## 📄 Sample Output

Each persona includes:

\`\`\`
🎯 Interests: Gaming, NFTs, NYC, AI
🧠 Writing Style: Casual, often humorous or sarcastic
💬 Political Views: Progressive/liberal (if inferred)
😂 Humor: Dry wit, irony, sarcasm
📎 Citations: [source: https://reddit.com/r/example/...]
\`\`\`

See the `sample_output/` folder for examples.

---

## ⚠️ Error Handling

| Issue                                | What Happens                               |
|-------------------------------------|--------------------------------------------|
| Nonexistent Reddit username         | Gracefully exits with a message            |
| No content to analyze               | Skips persona generation                   |
| Invalid API keys or network issues  | Shows clear errors                         |
| Groq API failures                   | Retries or logs reason                     |

---

## 📬 Contact

**Harshit Vishnoi**  
This project was built for the BeyondChats AI Internship Assignment.  
Feel free to contact me via Internshala or connect on [LinkedIn](https://linkedin.com/in/harshitvishnoi-ai).

---

> ⚠️ Disclaimer: This project uses publicly available Reddit content and LLM-generated insights for academic/demo purposes only.

