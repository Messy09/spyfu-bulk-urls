# Usage Guide

## Installation

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

Running from the command line
The project exposes a CLI through src/cli.py.
Basic example:
bashpython -m src.cli \
  --input data/input_urls.sample.txt \
  --process top_competitors \
  --country US \
  --format json \