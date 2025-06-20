import os
import json
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


BATCH_SIZE = 5

def process_txt_files(input_folder, target_lang="English", output_json_path = None):
    batches = []
    current_batch = ""
    count = 0

    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".text"):
            with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    current_batch += f"\n\n--- Page {filename} ---\n{content}"
                    count += 1
                    if count == BATCH_SIZE:
                        batches.append(current_batch)
                        current_batch = ""
                        count = 0

    if current_batch.strip():
        batches.append(current_batch)

    results = []

    for idx, batch_text in enumerate(batches):
        print(f"\n📦  Batch processing {idx + 1} من {len(batches)}")
        print("📤   Texts before sending:\n", batch_text[:500])

        prompt = f"""
You are a professional academic translator.

Your task is to detect the original language of the following academic text, and then translate it into **{target_lang}** with accuracy, fluency, and academic tone.

- Do NOT explain anything.
- Do NOT include formatting like triple backticks.
- Just return the translated text.

Text to translate:)

Text:
{batch_text}
"""

        try:
            response = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=4000,
            )

            if not response.choices or not response.choices[0].message:
                print("❌ No response LLM.")
                continue

            result_text = response.choices[0].message.content.strip()
            print("🧠  response  LLM:\n", result_text)

        


            if result_text.startswith("```"):
                result_text = result_text.strip("```").strip()

            results.append(result_text)

        except Exception as e:
            print(f"❌ Error in batch {idx + 1}: {e}")
            continue

    return results

