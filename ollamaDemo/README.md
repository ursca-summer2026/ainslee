# **Ollama Automation Demo Repository**

This repository contains all code for the data collection program, as well as results from testing along the way.

## **How to Use**

1. It is recommended that you make a virtual environment before running the program. The following is the terminal method of doing so:

    - Open a new terminal
    - Run the following command: `python -m venv .venv`
        - *Note*: Use `python3` instead of `python` on macOS or Linux if required
    - A pop-up will usually appear asking if you want to select this environment for the workspace folder. **Click yes.**
        - If you do not see the prompt, open the Command Palette (Ctrl/Cmd + Shift + P), select Python: Select Interpreter, and click on the entry pointing to your newly created `.venv` folder.
    - Activate the environment:
        - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
        - Windows (Command Prompt): `.venv\Scripts\activate.batmacOS`
        - Linux: `source .venv/bin/activate`
    - To turn off the virtual environment at any time, simply type `deactivate` in your terminal.

2. Pull the model you wish to by using the following terminal command:
    
    - ollama pull modelName

3. Make sure you are in the proper location to run the program:

    - cd .\ollamaDemo\

4. You can run the program with either of these commands:

    - `python testingAutomation.py -m modelName -k “keyword1, keyword2,” -r 1 -o “output.txt” -f “Output Folder” -p “prompts.txt”`
    - `uv run testingAutomation.py -m modelName -k “keyword1, keyword2,” -r 1 -o “output.txt” -f “Output Folder” -p “prompts.txt”`

*Note*: You are only required to have the "-m", "-k", and "-p" arguments. If others are not entered, a default will be provided for the program to run as expected.

## **Filenames**

For results of the llama3.2 model containing "nurse", "doctor" and other keywords, please call your results filename: llama3.2_RESULTS.txt

*Note*: Depending on the model you choose, your CSV output will print with errors if the file name does not end in `.txt`