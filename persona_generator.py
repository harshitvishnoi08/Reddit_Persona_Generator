# persona_generator.py

import argparse
import os
from reddit_scraper import scrape_user
from groq_persona_builder import build_persona

def main():
    parser = argparse.ArgumentParser(description="Generate a Reddit user persona.")
    parser.add_argument("--username", required=True, help="Reddit username (e.g., kojied)")
    args = parser.parse_args()

    try:
        print(f"🔎 Scraping user: {args.username}")
        data = scrape_user(args.username)

        if not data:
            print(f"⚠️ No comments or posts found for user '{args.username}'. Skipping persona generation.")
            return

        print("🧠 Generating persona using Groq LLM...")
        persona_text = build_persona(data)

        output_dir = "sample_output"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{args.username}_persona.txt")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(persona_text)

        print(f"✅ Persona saved to {output_path}")

    except ValueError as ve:
        print(f"❌ Error: {ve}")
    except RuntimeError as re:
        print(f"❌ Runtime Error: {re}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


if __name__ == "__main__":
    main()

