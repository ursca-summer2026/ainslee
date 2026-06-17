import csv
import ollama # type: ignore


def queryModel(model, prompt):
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    text = response["message"]["content"].strip()
    sentences = text.split(".")
    return ". ".join(sentences[:2]).strip() + "."
# end of queryModel()


def runBatch(model, prompts, csv_file="results.csv"):
    rows = []
    for p in prompts:
        answer = queryModel(model, p)
        rows.append({"model": model, "prompt": p, "response": answer})

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["model", "prompt", "response"])
        writer.writeheader()
        writer.writerows(rows)
# end of runBatch()


def main():
    model = input("Model name: ")
    print("Enter prompts (blank line to finish):")
    # add CLI for keywords, length of output, num times to run, file name, etc
    # add in exception handling for invalid model names, wrong file name, etc
    # read in prompts from a text file instead of typing? keyword?

    prompts = []
    while True:
        p = input("> ")
        if not p.strip():
            break
        prompts.append(p)

    runBatch(model, prompts)
# end of main()


if __name__ == "__main__":
    main()
