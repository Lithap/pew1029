# pew1029

A simple CLI tool for pew.

## Installation

```bash
pip install -e .
```

## Usage

### Stop Command

Stop pew immediately:

```bash
python3 pew.py stop now
```

Or simply:

```bash
python3 pew.py stop
```

## Running Tests

```bash
python3 -m unittest test_pew.py -v
```

## Examples

```bash
$ python3 pew.py stop now
Stopping pew now

$ python3 pew.py stop
Stopping pew

$ python3 pew.py --help
usage: pew [-h] {stop} ...

Pew CLI tool

positional arguments:
  {stop}      Available commands
    stop      Stop pew

options:
  -h, --help  show this help message and exit
```