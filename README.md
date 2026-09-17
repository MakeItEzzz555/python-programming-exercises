# Python Programming Exercises

> The Frederick coursework subset is consolidated into [MakeItEzzz555/frederick-university-coursework](https://github.com/MakeItEzzz555/frederick-university-coursework). This repository remains active because the independent grid-pathfinding utility is outside the Frederick archive. Historical source is retained here.

Independent Python exercises covering arithmetic, algorithms, product classes, CSV persistence and Turtle graphics. The `acsc430` sequence is associated with Frederick University coursework from nearby course material; some loose-file module associations are inferred. Grid pathfinding is a separate utility and contains no Arduino firmware or serial communication.

## Contents

| Folder | Course/Lab | Topic | Language/Platform |
| --- | --- | --- | --- |
| `grid-pathfinding` | Grid search utility | Breadth-first search over a text grid with zero-valued walkable cells | Python 3 |
| `acsc430/lab06-products` | Lab 6 | Product inheritance, CSV loading/saving, listing, adding and editing products | Python 3 |
| `acsc430/lab1Ex1` | lab1Ex1.py | Discount calculation | Python 3 |
| `acsc430/lab1Ex2` | lab1Ex2.py | Average of three numbers | Python 3 |
| `acsc430/lab1Ex3` | lab1Ex3.py | Present value of a future deposit | Python 3 |
| `acsc430/lab1Ex5` | lab1Ex5.py | Tip and tax calculation | Python 3 |
| `acsc430/lab1Ex6` | lab1Ex6.py | Distance unit conversion | Python 3 |
| `acsc430/lab1Ex7` | lab1Ex7.py | Stock purchase/sale commission calculation | Python 3 |
| `acsc430/lab1ex4` | lab1ex4.py | Five-item subtotal and sales tax | Python 3 |
| `acsc430/lab2Assign` | lab2Assign.py | Garden planting and soil/fill calculations | Python 3 |
| `acsc430/lab3` | lab3.py | Trial-division versus sieve prime timing | Python 3 |
| `acsc430/lab4Ex1` | lab4Ex1.py | Basic cone area/volume calculation | Python 3 |
| `acsc430/lab4Ex2` | lab4Ex2.py | Validated cone geometry | Python 3 |
| `acsc430/lab4Ex3` | lab4Ex3.py | Turtle drawing of the US flag | Python 3 / Turtle |

## Setup and run

Use Python 3. The scripts use the standard library; Turtle also needs a working Tk GUI installation.

```sh
python3 acsc430/lab1Ex1/lab1Ex1.py
python3 acsc430/lab3/lab3.py
python3 acsc430/lab4Ex3/lab4Ex3.py
```

Follow each program's prompts. Prime timing should start with a small positive bound. The basic cone exercise uses 3.14 for pi; the validated variant uses `math.pi`.

For the product menu, run from its folder so the companion module and sample CSV are easy to locate:

```sh
cd acsc430/lab06-products
python3 Lab06.py
```

Choose `a` and enter `All_Products.csv` to load the six-row sample catalog. The menu supports listing, adding, editing and saving. Saving writes to the filename you supply; use a new filename to retain the sample catalog.

For BFS pathfinding:

```sh
cd grid-pathfinding
python3 shortest_path.py
```

Enter `map.txt`, then start and goal coordinates as `row column`. Cells containing `0` are walkable. The program reports a shortest path when one exists.

## Validation

Python AST checks passed. Eleven arithmetic/algorithm CLI exercises, BFS on a synthetic grid and the separate scanner utility received bounded smoke checks. Within this repository, twelve entries have successful CLI evidence. The product menu and Turtle GUI remain unverified at runtime. Smoke checks cover selected inputs only.

## Archival notes

Original application source is preserved. Generated files, machine metadata, private runtime data and teaching documents are excluded. No license has been inferred.
