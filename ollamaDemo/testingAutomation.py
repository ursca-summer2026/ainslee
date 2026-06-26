import argparse
import csv
import ollama # type: ignore
import os


def queryModel(model, prompt):
    # attempt to load in the input model and query it with the prompt
    # raise an error if the model is not found or the query fails
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
    except Exception as e:
        raise RuntimeError(f"Model query failed. Double-check the model name and try again: {e}")
    
    # seperate the content of the model query and store only the first two sentences in the response
    text = response["message"]["content"].strip()
    sentences = text.split(".")
    return ". ".join(sentences[:2]).strip() + "."
# end of queryModel()


def runBatch(model, keyword,prompts, csv_file="results.csv", runs=1, writeHeader=False):
    rows = []
    # iterate through each prompt and run the model query the specified number of times
    for p in prompts:
        for _ in range(runs):
            answer = queryModel(model, p)
            rows.append({"keyword": keyword, "prompt": p, "response": answer})

    # write the results to a CSV file
    # raise an error if the file cannot be written to
    try:
        # mode "write" or "append" depending on whether there is a header
        mode = "w" if writeHeader else "a"
        with open(csv_file, mode, newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["keyword", "prompt", "response"])
            if writeHeader:
                writer.writeheader()
            writer.writerows(rows)
    except OSError as e:
        raise RuntimeError(f"Could not write to file '{csv_file}': {e}")
# end of runBatch()


def main():
    parser = argparse.ArgumentParser(description="A sample script using argparse.")
    parser.add_argument("-m", "--model", type=str, help="Model name to use")
    parser.add_argument("-p", "--prompt", type=str, help="Prompt to use")
    parser.add_argument("-k", "--keywords", type=str, help="Comma-separated keywords to use")
    parser.add_argument("-r", "--runs", type=int, help="Number of times to run each prompt (default: 1)")

    # separate the user-given termincal command and store the pieces separately
    # if a piece hasn't been input, have the user input it manually
    args = parser.parse_args()
        
    # model name
    if args.model is None:
        args.model = input("Enter model name: ").strip()

    # prmpt to use
    if args.prompt is None:
        args.prompt = input("Enter prompt: ").strip()

    # keywords to substitute into the prompt
    if args.keywords is None:
        args.keywords = input("Enter keywords (comma-separated): ").strip()
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]

    if args.runs is None:
        args.runs = int(input("How many times should each prompt be run? "))

    # confirmation of all inputs
    print(f"\nUsing model: {args.model}")
    print(f"Using prompt --> {args.prompt}")
    print(f"Using keywords: {args.keywords}")
    print(f"Running each prompt {args.runs} times.")

    exit()

    '''
    # set up CSV file output name & path
    csvFile = input("Output CSV filename (default results.csv): ") or "results.csv"
    CSVStoreFolder = input("Folder to save file in (default: output): ").strip() or "output"
    csvPath = os.path.join(CSVStoreFolder, csvFile)
    
    # collect input on which file to read prompts from
    promptFile = input("Enter prompt file name: ").strip()

    # attempt to open said prompt file and read in the prompts as inidividual lines
    # replace the {keyword} placeholder in each prompt with the user-provided keyword
    # raise an error if the file cannot be found
    try:
        with open(promptFile, "r", encoding="utf-8") as f:
            basePrompts = [line.strip() for line in f if line.strip()]
    except OSError as e:
        print(f"Could not find file. Double-check the file name and try again: {e}")
        return
    
    # putting everything together
    try:
        # quick model validation (error raised if invalid model name)
        try:
            ollama.chat(model=model, messages=[{"role": "user", "content": "test"}])
        except Exception as e:
            print(f"Model query failed. Double-check the model name and try again: {e}")
            return

        # ensure CSV storage folder exists
        os.makedirs(CSVStoreFolder, exist_ok=True)

        # process each keyword & write to a CSV file
        first = True
        for keyword in keywords:
            prompts = [p.replace("{keyword}", keyword) for p in basePrompts]
            runBatch(
                model,
                keyword,
                prompts,
                csv_file=csvPath,
                runs=numRuns,
                writeHeader=first
            )
            first = False

    #if any runtime errors occur during the process, print the error message
    except RuntimeError as e:
        print(f"Runtime error: {e}")
# end of main()
'''

if __name__ == "__main__":
    main()
