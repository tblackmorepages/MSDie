# Multi-sided Die

A command line program that accepts an integer number of sides of the die as an input and generates a random roll value.

## Installation
First download requirements.txt and install in terminal using:

```bash
pip install -r requirements.txt
```

Next download the `msdie.py` file. The program can then be run in the terminal using:
```bash
python3 msdie.py
```

## Usage
To roll a die of n sides enter the desired value of n:
```python
> 5
```

Input must be the integer number of sides expressed in numerical or alphabetical format but the latter format must be separated with a single space:
```python
> sixty eight 
```

To re-roll the previously given die enter `roll` or `r`:
```python
> roll
```

To roll a die of n sides x number of times enter `multi roll` or `m r` followed by n then x.The result will be given as a dictionary of the occurrences of each side of the die:
```python
> m r 
> 5 
> 10
```

To exit the MSDie enter `exit`, `quit` or `close`.

For help whilst using the MSDie enter `help` or `?`. 

## Example

```python
$ python3 msdie.py
Welcome to MSDie, for help enter: `help` or `?`
> 3
2
> roll
2
> m r
    > 5
    > 4
{1: 1, 2: 1, 3: 1, 4: 0, 5: 1}
> quit
Exiting MSDie...
```
