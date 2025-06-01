
---

# 🧰 **💥 Git Command Cheat Sheet – Full Guide**

---

## 🟢 1. **Cloning a Repository (from GitHub)**

```bash
git clone <repo-url>
# Example:
git clone https://github.com/yourusername/repo-name.git
```

---

## 🆕 2. **Creating a New Repository**

```bash
git init
# Initializes Git in the current folder
```

---

## 📁 3. **Staging and Committing Files**

```bash
git status
# Shows changed files

git add <file>
# Stages a file

git add .
# Stages everything

git commit -m "Your commit message"
# Commits staged files with a message
```

---

## 🌳 4. **Branching**

```bash
git branch
# List all local branches

git branch <branch-name>
# Create a new branch

git checkout <branch-name>
# Switch to another branch

git checkout -b <branch-name>
# Create and switch to a new branch

git branch -d <branch-name>
# Delete a local branch

git branch -D <branch-name>
# Force delete a local branch
```

---

## 🚀 5. **Pushing to GitHub**

```bash
git push origin <branch-name>
# Push your branch to GitHub

git push -u origin <branch-name>
# Push and set upstream for future pushes

git push
# Pushes the current branch if upstream is set
```

---

## 📥 6. **Pulling & Fetching**

```bash
git fetch
# Downloads latest changes but doesn't merge

git pull
# Downloads and merges latest changes from remote

git pull origin <branch-name>
# Pull from a specific branch
```

---

## 🔄 7. **Merging and Rebasing**

```bash
git merge <branch-name>
# Merge a branch into your current branch

git rebase <branch-name>
# Replay commits from current branch onto another
```

---

## 🔄 8. **Compare and Diff**

```bash
git diff
# Show unstaged changes

git diff --staged
# Show staged changes

git diff <branch1>..<branch2>
# Compare two branches

git diff origin/main
# Compare current branch with remote main
```

---

## 📜 9. **Viewing History**

```bash
git log
# Full commit history

git log --oneline
# Short log

git log --graph --oneline --all
# Visual representation of branches
```

---

## 💼 10. **Remote and Repository Management**

```bash
git remote -v
# View remote repos

git remote add origin <url>
# Add a new remote

git remote remove origin
# Remove a remote
```

---

## 🚨 11. **Undoing Changes**

```bash
git checkout -- <file>
# Discard changes to a file

git reset <file>
# Unstage a file

git reset --hard
# Reset all changes to last commit

git revert <commit-hash>
# Revert a specific commit
```

---

## 🌐 12. **Sync Your Branch with Main (or Any Branch)**

```bash
git fetch origin
git merge origin/main
# OR rebase instead:
git rebase origin/main
```

---

## 🧹 13. **Cleaning Up**

```bash
git clean -fd
# Remove untracked files and folders

git fetch --prune
# Clean up deleted remote branches
```

---

## 🔐 14. **Authentication Helpers**

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
# Set Git user details

git config --global credential.helper cache
# Cache credentials for HTTPS
```

---

## 🏁 Bonus: Git Alias Shortcuts

Add aliases to speed up typing:

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.cm "commit -m"
git config --global alias.br branch
git config --global alias.last "log -1 HEAD"
```

## 🧵 What is `doskey`?

`doskey` is a Windows command that lets you create command aliases (shortcuts) for long commands. It works **only in the current terminal session** unless you persist it.

### ✅ Example Usage:

```bash
doskey gcm=git commit -m $*
doskey gpo=git push origin $*
doskey gpl=git pull origin $*
```

* `$*` passes all arguments to the real command.
* Example:

  ```bash
  gcm "added login feature"
  ```

> ✅ Tip: To make these **permanent**, add them to a `.bat` or PowerShell profile file.

---

## 🧩 Remaining Useful Git Commands

Here are some **additional Git commands and advanced tools** that weren’t in the first list:

---

### 🧱 **Stashing Changes (Save work temporarily)**

```bash
git stash
# Save local uncommitted changes

git stash list
# Show stashed changes

git stash apply
# Re-apply stashed changes

git stash drop
# Delete a stash
```

---

### 🔍 **Tagging (Versions/releases)**

```bash
git tag
# List tags

git tag v1.0
# Create tag

git push origin v1.0
# Push tag to GitHub
```

---

### 🔐 **Cherry Pick (Copy a single commit)**

```bash
git cherry-pick <commit-hash>
# Apply one specific commit onto current branch
```

---

### 🧭 **Tracking Branches**

```bash
git branch -vv
# See local branches and which remotes they track
```

---

### 📊 **Short Summary**

```bash
git shortlog
# Summary of commits by author

git show <commit>
# Show what happened in a specific commit
```

---

### 🧰 **Fix Common Issues**

```bash
git restore <file>
# Like checkout --, used to undo changes

git reflog
# History of all HEAD changes — useful for recovery
```

---

### 🧑‍🤝‍🧑 **Collaboration Tools**

```bash
git pull --rebase
# Rebase instead of merging while pulling (cleaner history)

git merge --no-ff <branch>
# Force a merge commit even if fast-forward

git remote show origin
# Details about the remote repository
```

---

## 🧼 CRLF / LF Warnings (Windows)

To avoid Git line-ending warnings on Windows:

```bash
git config --global core.autocrlf true
```

---


| 🔢 # | 🧰 Command/Category       | 💻 Command Syntax or Example                     | 📝 Description                          |
| ---- | ------------------------- | ------------------------------------------------ | --------------------------------------- |
| 1    | **Clone Repo**            | `git clone <repo-url>`                           | Clone a remote GitHub repo              |
| 2    | **Initialize Git**        | `git init`                                       | Create a new local Git repo             |
| 3    | **Status Check**          | `git status`                                     | See changed, staged, untracked files    |
| 4    | **Add Files**             | `git add .` or `git add <file>`                  | Stage files for commit                  |
| 5    | **Commit**                | `git commit -m "message"`                        | Commit changes with message             |
| 6    | **Push to Remote**        | `git push origin <branch>` or `git push`         | Push commits to GitHub                  |
| 7    | **Pull from Remote**      | `git pull` or `git pull origin <branch>`         | Pull latest changes and merge           |
| 8    | **Fetch Remote Updates**  | `git fetch`                                      | Download new data from remote, no merge |
| 9    | **Branch List**           | `git branch`                                     | List local branches                     |
| 10   | **Create Branch**         | `git branch <branch>`                            | Create a new branch                     |
| 11   | **Switch Branch**         | `git checkout <branch>` or `git switch <branch>` | Change branch                           |
| 12   | **Create and Switch**     | `git checkout -b <branch>`                       | Create and switch branch                |
| 13   | **Merge Branch**          | `git merge <branch>`                             | Merge into current branch               |
| 14   | **Rebase**                | `git rebase <branch>`                            | Reapply commits on top of another       |
| 15   | **Diff Changes**          | `git diff`, `git diff origin/main`               | Show differences                        |
| 16   | **Commit History**        | `git log`, `git log --oneline`                   | Show commit logs                        |
| 17   | **Graph View**            | `git log --graph --oneline --all`                | Visual branch history                   |
| 18   | **Delete Branch**         | `git branch -d <branch>` or `-D`                 | Delete local branch                     |
| 19   | **Remote List**           | `git remote -v`                                  | Show remote URLs                        |
| 20   | **Add Remote**            | `git remote add origin <url>`                    | Add new remote repo                     |
| 21   | **Stash Changes**         | `git stash`, `git stash apply`, `git stash list` | Save work temporarily                   |
| 22   | **Tag a Version**         | `git tag v1.0`, `git push origin v1.0`           | Mark a release                          |
| 23   | **Cherry Pick**           | `git cherry-pick <commit>`                       | Apply a specific commit                 |
| 24   | **Restore File**          | `git restore <file>`                             | Discard file changes                    |
| 25   | **Reset**                 | `git reset --hard`                               | Reset working directory                 |
| 26   | **Reflog**                | `git reflog`                                     | View changes to HEAD                    |
| 27   | **Undo Commit**           | `git revert <commit>`                            | Revert a specific commit                |
| 28   | **Clean Untracked Files** | `git clean -fd`                                  | Delete untracked files/folders          |
| 29   | **Configure User**        | `git config --global user.name/email`            | Set author identity                     |
| 30   | **CRLF Fix (Windows)**    | `git config --global core.autocrlf true`         | Avoid line-ending warnings              |
| 31   | **View Remote Details**   | `git remote show origin`                         | See remote tracking details             |
| 32   | **Git Alias Setup**       | `git config --global alias.co checkout`, etc.    | Set command shortcuts                   |
| 33   | **Doskey Alias**          | `doskey gcm=git commit -m $*`                    | Create temporary Windows alias          |
| 34   | **Doskey Push Example**   | `doskey gpo=git push origin $*`                  | Shortcut for push                       |
| 35   | **Doskey Pull Example**   | `doskey gpl=git pull origin $*`                  | Shortcut for pull                       |
| 36   | **Prune Deleted Remotes** | `git fetch --prune`                              | Remove deleted remote branches          |
| 🔢 # | 🧰 Command/Category                     | 💻 Command Syntax or Example                                         | 📝 Description                                               |
| ---- | --------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------ |
| 37   | **Amend Commit**                        | `git commit --amend`                                                 | Modify the last commit message or content                    |
| 38   | **Squash Commits (Interactive Rebase)** | `git rebase -i HEAD~3`                                               | Combine multiple commits into one                            |
| 39   | **Blame**                               | `git blame <file>`                                                   | Show who made each line change in a file                     |
| 40   | **Bisect**                              | `git bisect start` → `git bisect bad` / `good`                       | Find the commit that introduced a bug                        |
| 41   | **Worktree (Multiple Checkouts)**       | `git worktree add ../folder branch`                                  | Checkout a branch into a different folder                    |
| 42   | **Submodules**                          | `git submodule add <repo>`                                           | Embed another Git repo inside a subfolder                    |
| 43   | **Show File at Commit**                 | `git show <commit>:<path>`                                           | View file contents at a specific commit                      |
| 44   | **Untrack a File**                      | `git rm --cached <file>`                                             | Stop tracking a file (e.g. remove from Git but keep locally) |
| 45   | **Change Default Branch**               | `git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main` | Set remote HEAD to a different branch                        |
| 46   | **Tag Annotated**                       | `git tag -a v1.0 -m "version 1.0"`                                   | Create an annotated tag with message                         |
