# my-first-project

A simple Python calculator with a command-line interface.

## Features

- Add, subtract, multiply, and divide two numbers
- Clean CLI using `argparse`
- Division by zero error handling

## Setup

```bash
git clone https://github.com/Imifrat/my-first-project.git
cd my-first-project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py <operation> <a> <b>
```

### Examples

```bash
python main.py add 10 5        # 15.0
python main.py subtract 10 3   # 7.0
python main.py multiply 6 7    # 42.0
python main.py divide 10 4     # 2.5
```

### Operations

| Operation  | Description          |
|------------|----------------------|
| `add`      | Adds two numbers     |
| `subtract` | Subtracts b from a   |
| `multiply` | Multiplies two numbers |
| `divide`   | Divides a by b       |
