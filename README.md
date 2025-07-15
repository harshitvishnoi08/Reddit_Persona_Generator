# 🧠 Reddit User Persona Generator

This project is built as part of the **Generative AI Internship Assignment** at **BeyondChats**.  
It scrapes a Reddit user's profile, extracts all posts and comments, and uses a **Groq-hosted open-source LLM** (e.g., Mixtral, LLaMA 3) to generate a detailed user **persona** with **citations** from their content.

---

## 🚀 Features

- ✅ Scrapes all posts and comments of a Reddit user
- ✅ Builds a multi-trait persona (interests, tone, humor, ideology, etc.)
- ✅ Uses free open-source LLMs via [Groq](https://console.groq.com)
- ✅ Chunks long content and merges persona insights
- ✅ Cites each claim with Reddit post or comment link
- ✅ Handles invalid users and users with no content

---

## 🧠 Use Cases

- Behavioral analysis
- Market segmentation
- Audience profiling
- Product personalization
- Research and content moderation tools

---

## 🧰 Tech Stack

| Tool            | Purpose                                    |
|-----------------|---------------------------------------------|
| Python          | Main scripting language                    |
| PRAW            | Reddit API wrapper                         |
| Groq Python SDK | Access Mixtral, LLaMA3 (fast LLM inference) |
| dotenv          | Manage API keys securely                   |
| argparse        | Command-line interface                     |
| tqdm (optional) | Chunk progress display                     |

---

## 🗂️ Project Structure

reddit_persona_generator/
├── persona_generator.py # Main controller script
├── reddit_scraper.py # Scrapes Reddit posts and comments
├── groq_persona_builder.py # Persona generation logic using Groq
├── requirements.txt # Required dependencies
├── .env # Store Groq + Reddit API keys here
├── README.md # This file
└── sample_output/ # Folder for persona outputs
├── kojied_persona.txt
└── Hungry-Move-6603_persona.txt


---

## 🔐 Environment Variables

Create a `.env` file in the root directory with:

```env
GROQ_API_KEY=your_groq_key
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_secret
🛠 Installation & Setup
1. Clone this repository
bash
Copy
Edit
git clone https://github.com/yourusername/reddit-persona-generator.git
cd reddit-persona-generator
2. Install Python dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Create .env file
bash
Copy
Edit
touch .env
Add your credentials inside .env (see above).

🚀 How to Use
Run the script with any Reddit username:

bash
Copy
Edit
python persona_generator.py --username kojied
This will:

Scrape Reddit data for kojied

Send content to Groq-hosted LLM (e.g., Mixtral-8x7B)

Generate a persona with citations

Save the result to sample_output/kojied_persona.txt

📄 Sample Output
The final persona includes:

diff
Copy
Edit
🎯 Interests:
- Gaming (Civilization V, Project Zomboid)
- AI and ChatGPT
- Finance, NFTs, and Crypto
- Anime and Manga

✍️ Writing Style:
- Informal, humorous, often sarcastic

🧠 Ideological Views:
- Progressive, critical of wealth inequality

😂 Humor Style:
- Witty, sarcastic, uses internet memes

📎 Citations:
- [source: https://reddit.com/r/wallstreetbets/comments/fhp5ae/]
- [source: https://reddit.com/r/warriors/comments/...]
You can find these .txt files in the sample_output/ folder.

⚠️ Error Handling
Situation	Handled?	Behavior
Reddit user does not exist	✅	Prints a user-friendly error message
User has no public posts/comments	✅	Skips persona generation with warning
Invalid Reddit API credentials	✅	Catches and logs Reddit API errors
Groq API error (timeout/failure)	✅	Retries and then fails gracefully
Missing --username argument	✅	argparse handles with proper message


