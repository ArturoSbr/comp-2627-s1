# Your First Pull Request

Your job is to contribute to the file `students.txt` by adding your student ID
to the list. Follow these instructions:

1. Make sure you have a copy of the repo on your computer. We did this in class
with `git clone`, so you have probably already completed this step.
2. Open the repo in Visual Studio Code: Open the app, go to `File > Open Folder`
and select the folder named `comp-2627-s1`.
3. Open a new Terminal from `Terminal > New Terminal`.
4. Switch to branch `develop`: `git switch develop`.
5. Update the branch: `git pull`.
6. Create and switch to your own branch:
`git switch -c assignment-00/<your student ID>`. For example:
`git switch -c assignment-00/130524`.
7. Open file `students.txt` located in `assignments/assignment-00/`.
8. Add your student ID to the list.
9. Once you've typed your student ID:
    * Save the changes (`File > Save`)
    * `git add assignments/assignment-00/students.txt`
    * `git commit -m "Add 130524 to list of students"` (or some other coherent
    message)
    * `git push` (it will yell at you that you haven't registered the upstream
    branch, so just copy and paste its suggestion)
10. Navigate to [our repo](https://github.com/ArturoSbr/comp-2627-s1), find your
branch and select "Compare & pull request".
    * Make sure you request to merge into `develop`.
    * It should look like `base: develop <- compare: assignment-00/130524`.
