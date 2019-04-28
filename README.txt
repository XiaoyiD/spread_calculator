---------------
RUNNING THE CODE
---------------

    The top-level python executable is spread_analysis.py

    0. For the starter code to run, you must first run under python3 environment,
    with package pandas installed.

    1. Note that when the terminal asked for name of input file, the file must
    in same directory with the spread_analysis.py file.

    Here is an example run in terminal,

    cd ~
    python3 spread_analysis.py

    With the input promote in text format:
    Please type the full name of input file, suffix include:

    sample_input.csv

---------------
TESTING THE CODE
---------------

  Here is an example run in terminal:
      cd ~
      python3 test_spread_analysis.py


---------------------
TECHNICAL CHOICES
---------------------

  Data Manipulation
    Choosing pandas library to do the data manipulation is because pd.DataFrame
    can adapt various datatype for different columns,
    and also can adapt SQL query and conditional logic.


---------------------
IMPROVEMENTS
---------------------

1. Should have a top-level routine run.py that does nothing other than call the
   code's main function. This will make user much convenient to use.

2. Should have more input promote sentence, making better for user to be used.

3. Should have separate files for manipulating input_file, and challenge1&2
   question solutions.

4. Create instance of bond will make coding much easier and neater.

5. More checking for corner case. Such as for find_best_benchmark, what if
   there are two government bond having same difference with one corporate bond.

6. Time Complexity should be improved for both challenge.
