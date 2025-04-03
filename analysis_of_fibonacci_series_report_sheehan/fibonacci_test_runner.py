import subprocess
import time
import sys
import math


# file argument calls
COMMON_ARG_FORMAT = "./fibonacci_c {n} {algo} {print_level}"
COMMON_ARG_PYTHON = "python3 fibonacci_python.py {n} {algo} {print_level}"

FORMAT = "markdown"  
TIMEOUT = 60

# tracker for C program run time
LAST_RUN_TRACKER_C = {"0": 0.0, "1": 0.0, "2": 0.0, "iterative": 0.0, "recursive": 0.0, "dp": 0.0}

# tracker for python program run time
LAST_RUN_TRACKER_PY = {"0": 0.0, "1": 0.0, "2": 0.0, "iterative": 0.0, "recursive": 0.0, "dp": 0.0}

# run a single iteration
def run_single(n: int, typ: str, print_level: int, command=COMMON_ARG_FORMAT, tracker=LAST_RUN_TRACKER_C) -> float:
    command = command.format(n=n, algo=typ, print_level=print_level)

    # check for timeout
    if math.isnan(tracker[str(typ)]):
        return math.nan

    try:
        
        # capture the output from start time to end time of function call
        start = time.time()
        subprocess.run(command.split(), timeout=TIMEOUT, capture_output=True, text=True)
        end = time.time()
        result = end - start
    except subprocess.TimeoutExpired:
        result = math.nan

    tracker[str(typ)] = result
    return result

def build_row(n: int, print_level: int) -> str:
    
    "# Builds a row for the markdown table"
    results_lst = []

    # run functions and store results
    results_lst.append(str(run_single(n, "iterative", print_level, COMMON_ARG_FORMAT, LAST_RUN_TRACKER_C)))
    results_lst.append(str(run_single(n, "recursive", print_level, COMMON_ARG_FORMAT, LAST_RUN_TRACKER_C)))
    results_lst.append(str(run_single(n, "dp", print_level, COMMON_ARG_FORMAT, LAST_RUN_TRACKER_C)))
    results_lst.append(str(run_single(n, "iterative", print_level, COMMON_ARG_PYTHON, LAST_RUN_TRACKER_PY)))
    results_lst.append(str(run_single(n, "recursive", print_level, COMMON_ARG_PYTHON, LAST_RUN_TRACKER_PY)))
    results_lst.append(str(run_single(n, "dp", print_level, COMMON_ARG_PYTHON, LAST_RUN_TRACKER_PY)))

    # table format
    if FORMAT == "markdown":
        return f"| {n:<4} | {results_lst[0].center(8, ' ')} | {results_lst[1].center(8, ' ')} | {results_lst[2].center(8, ' ')} |" \
            + f"{results_lst[3].center(8, ' ')} | {results_lst[4].center(8, ' ')} | {results_lst[5].center(8, ' ')} |"
    return f"{n},{','.join(results_lst)}"

# create the table header for markdown
def table_header() -> str:
    if FORMAT == "markdown":
        return "| n | Iterative C | Recursive C | Dynamic Programming C | Iterative P | Recursive P | Dynamic Programming P |\n" + \
               "|--|:--:|:--:|:--:|:--:|:--:|:--:|"
    return "n,Iterative C,Recursive C,Dynamic Programming C,Iterative P,Recursive P,Dynamic Programming P"


def main(n, print_level):
    print(table_header())
    for i in range(1, n + 1, 1):
        print(build_row(i, print_level))

if __name__ == "__main__":
    
    _n = 30 if len(sys.argv) < 2 else int(sys.argv[1])
    _print_level = 1 if len(sys.argv) < 3 else int(sys.argv[2])

    if len(sys.argv) == 4:
        FORMAT = "csv"

    main(_n, _print_level)