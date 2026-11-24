# Integrating AI Into Your Stack

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AI-Eswatini/integrating-ai-into-your-stack/blob/main/integrating-and-using-ai.ipynb)

The quickest way to start: click **Open in Colab** above. Nothing to install. Add your `GEMINI_API_KEY` in Colab's **Secrets** (key icon in the left sidebar) and run the cells top to bottom. To run it on your own machine instead, follow the setup below.

## Setup

Requires Python 3.12+.

### Using uv

```sh
uv sync
```

### Using pip

```sh
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -e . ipykernel
```

## Running the notebook in VS Code

1. Install the **Python** and **Jupyter** extensions.
2. Open `integrating-and-using-ai.ipynb`.
3. Click **Select Kernel** (top right) → **Python Environments** → pick `.venv`.
4. Run the cells.

If VS Code says the kernel needs `ipykernel`, rerun the install step above for your setup.

## New to Python? Start here

The notebook uses a handful of Python basics. Each file in `src/integrating_ai_into_your_stack/` covers one of them in a few lines, using the same shop and clinic examples as the notebook. Read a file, run it, then change a value and run it again.

Run a file from the project folder:

```sh
# uv
uv run python src/integrating_ai_into_your_stack/dict.py

# pip (with .venv activated)
python src/integrating_ai_into_your_stack/dict.py
```

Work through them in this order:

| File | You learn | Where the notebook uses it |
| --- | --- | --- |
| `strings.py` | Joining text, f-strings, `.strip()`, `.lower()`, `.splitlines()` | Building prompts, cleaning the AI's reply |
| `list.py` | Making a list, reading by position, `.append()`, `.remove()`, lists of dicts | The `messages` list, order items |
| `dict.py` | Reading, changing and removing values by key | Every structured AI response |
| `loops.py` | `for`, `enumerate`, `zip`, `if`/`else`, list comprehensions | Numbering messages for batching, matching labels to messages |
| `functions.py` | `def`, `return`, named arguments, `**` unpacking, functions in a dict | `ask()`, `ask_json()`, and running the AI's tool calls |
| `json_data.py` | `json.loads()` (text → Python data) and `json.dumps()` (Python data → text) | Turning the AI's JSON reply into a dict, sending tool results back |

The key idea for the AI part: **the model always sends back text.** `json.loads()` turns that text into a `dict` or `list` your code can use.
