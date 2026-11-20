# grocery-cleaning

Cleans a messy grocery purchases file (`groceries_raw.csv`) with **pandas**
and saves a clean version (`groceries_clean.csv`).

## Problems found and how they were fixed
| Problem | Fix |
|---|---|
| Duplicate row (Rice) | Removed with `drop_duplicates()` |
| Category written in different ways (`Dairy`, `DAIRY`, ` vegetables `) | Removed spaces, made lowercase |
| Price written as text (`1.20 JD`) | Removed `JD`, converted to a number |
| Missing price (Apples) | Row removed, a price can't be guessed |
| Missing quantity | Filled with 1 |
| Negative quantity (`-2`) | Made positive (typing mistake) |

## How to run
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python explore.py
python clean.py
```

## Result
14 rows before, 12 rows after. Total spent: **31.45 JD**.
Most bought category: dairy (4 items).

## Limitation
Filling a missing quantity with 1 is a guess; the real quantity may be different.