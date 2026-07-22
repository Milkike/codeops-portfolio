# Day 1 Notes

## Topic

Git & Terminal Revision

---

# What is the Terminal?

The terminal is a text-based interface used to communicate with a computer by typing commands instead of clicking with a mouse.

Advantages:

- Fast
- Powerful
- Used by developers
- Supports automation

---

# Terminal Commands

## 1. pwd

Shows the current working directory.

Example:

```bash
pwd
```

---

## 2. ls

Lists files and folders.

```bash
ls
```

---

## 3. cd

Changes the current directory.

```bash
cd day01
```

---

## 4. mkdir

Creates a new folder.

```bash
mkdir projects
```

---

## 5. rm

Deletes a file.

```bash
rm notes.txt
```

---

# What is Git?

Git is a Version Control System that tracks changes in files and allows developers to manage project history.

---

# Git vs GitHub

Git:
- Installed on your computer
- Tracks file changes
- Works offline

GitHub:
- Website
- Stores Git repositories online
- Used for collaboration and backup

---

# Git's Three Areas

## 1. Working Directory

The files you are editing.

↓

Move to staging area using:

```bash
git add .
```

---

## 2. Staging Area

Files prepared for a commit.

↓

Move to repository using:

```bash
git commit -m "Commit message"
```

---

## 3. Repository

Permanent project history.

↓

Upload to GitHub using:

```bash
git push
```

---

# Git Commands

## git init

Creates a new Git repository.

```bash
git init
```

---

## git status

Shows the current repository status.

```bash
git status
```

---

## git add

Stages files.

```bash
git add .
```

---

## git commit

Creates a snapshot.

```bash
git commit -m "Add Day 1 notes"
```

---

## git push

Uploads commits to GitHub.

```bash
git push
```

---

## git pull

Downloads the latest changes.

```bash
git pull
```

---

## git log

Shows commit history.

```bash
git log --oneline
```

---

# Daily Git Workflow

1. git pull
2. Work on the project
3. git add .
4. git commit -m "Message"
5. git push

---

# Important Concepts

Working Directory → Staging Area → Repository → GitHub

---

# What I Learned

- How to use the terminal.
- Basic navigation commands.
- How Git tracks changes.
- Difference between Git and GitHub.
- How to commit changes.
- How to push projects to GitHub.
- How to use .gitignore.

---

# Summary

The terminal allows developers to interact with the computer using commands. Git is a version control system that tracks project history, while GitHub hosts repositories online. The daily workflow is:

git pull → work → git add . → git commit → git push