import csv
import ollama # type: ignore
import os


def queryModel(model, prompt):
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
    except Exception as e:
        raise RuntimeError(f"Model query failed: {e}")
    
    text = response["message"]["content"].strip()
    sentences = text.split(".")
    return ". ".join(sentences[:2]).strip() + "."
# end of queryModel()


def runBatch(model, prompts, csv_file="results.csv", runs=1):
    rows = []
    for p in prompts:
        for _ in range(runs):
            answer = queryModel(model, p)
            rows.append({"model": model,  "prompt": p, "response": answer})

    try:
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["model", "prompt", "response"])
            writer.writeheader()
            writer.writerows(rows)
    except OSError as e:
        raise RuntimeError(f"Could not write to file '{csv_file}': {e}")
# end of runBatch()


def main():
    model = input("Model name: ")
    keyword = input("Enter a keyword to be used in prompts: ")
    
    try:
        numRuns = int(input("How many times should each prompt be run? "))
    except ValueError:
        print("Invalid number. Defaulting to 1 run.")
        numRuns = 1

    csvFile = input("Output CSV filename (default results.csv): ") or "results.csv"
    CSVStoreFolder = input("Folder to save file in (default: output): ").strip() or "output"

    csvPath = os.path.join(CSVStoreFolder, csvFile)
    
    promptFile = input("Enter prompt file name: ").strip()

    try:
        with open(promptFile, "r", encoding="utf-8") as f:
            prompts = [
                line.strip().replace("{keyword}", keyword)
                for line in f if line.strip()
                ]
    except OSError as e:
        print(f"File error: {e}")
        return
    
    try:
        # quick model validation
        try:
            ollama.chat(model=model, messages=[{"role": "user", "content": "test"}])
        except Exception as e:
            print(f"Model error: {e}")
            return

        runBatch(model, prompts, csv_file=csvPath, runs=numRuns)

    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
