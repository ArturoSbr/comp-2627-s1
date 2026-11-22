# Assignment 01: Data Manipulation with `pandas`

Your job is to answer the questions in `assignments/assignment-01/code/main.py`
using `pandas`. Each question asks you to replace `True` with the code that
computes the requested table or value.

Do **not** rename the variables, modify `grader.py`, or alter the CSV files in
`data/`, as the autograder relies on those exact names to grade your work.

Follow these instructions step by step:

1. Open the repo in your code editor: go to `File > Open Folder` and select the
folder named `comp-2627-s1`.
2. Open a new Terminal from `Terminal > New Terminal`.
3. Make sure you are on the `main` branch:
   ```bash
   git switch main
   ```
4. Update your `main` branch so you have the latest files:
   ```bash
   git pull
   ```
5. Create and switch to your own branch using the **exact** pattern
`assignment-01/<your student ID>`:
   ```bash
   git switch -c assignment-01/<your student ID>
   ```
   For example, if your student ID is `130524`, run:
   ```bash
   git switch -c assignment-01/130524
   ```
   *Be very careful with spelling!* The robot that will grade your code is
   programmed to look for branches that start with `assignment-01/`. If you name
   your branch anything else (like `assignment1/130524` or `hw-01/130524`), your
   homework will not be graded!
6. Open the file `main.py` located in `assignments/assignment-01/code/`.
7. Read the comments for Questions 1 through 8 (`Q1` to `Q8`) and replace each
`True` with your `pandas` code.
   * *Tip:* If you want to test your progress on your own computer before
   submitting, make sure your `comp` environment is active
   (`conda activate comp`) and run
   `python assignments/assignment-01/code/grader.py` in the terminal.
8. Once you are ready to submit your answers:
   * Save your changes (`File > Save`).
   * Stage your file (only stage `main.py`):
     ```bash
     git add assignments/assignment-01/code/main.py
     ```
   * Save a checkpoint (commit) with a clear, descriptive message explaining
   what you did (avoid vague messages like `"update"` or `"stuff"`):
     ```bash
     git commit -m "Complete Q1 to Q8 in assignment 01"
     ```
   * Upload your changes to GitHub:
     ```bash
     git push
     ```
     *(The first time you push your branch, Git will yell at you that you
     haven't registered the upstream branch. Don't panic—just copy and paste the
     command it suggests and press Enter.)*
9. Check your score on GitHub:
   * Go to [our repo](https://github.com/ArturoSbr/comp-2627-s1) in your
   browser.
   * Click on the **Actions** tab at the top of the page.
   * Find the workflow run triggered by your push (it will show your commit
   message and branch name `assignment-01/<your student ID>`).
   * Click on your workflow run, then click on **Run Assignment 01 Autograder**,
   and expand the step called **Assignment 01 Autograder**.
   * At the bottom of the log, you will see which questions passed (`CORRECT`)
   or failed (`FAILED`), along with your `FINAL SCORE` out of 8.
10. Want to improve your grade? No problem! Just go back to `main.py`, fix your
code, save the file, and repeat step 8 (`git add`, `git commit`, and
`git push`). GitHub Actions will automatically re-grade your work every time you
push.
