# Git Branch Manager

A Python script to manage and delete Git branches both locally and remotely, with built-in protection for important branches like `master` and `main`.

## Features

- **List all branches** in a specified Git repository.
- **Protected Branch Notification**: Automatically identifies and excludes protected branches (`master`, `main`, etc.) from deletion, clearly marking them as protected when branches are first listed.
- **Unmerged Branch Notification**: Marks branches that are not fully merged into a specified base branch (e.g., `main` or `master`), allowing you to review them before deletion.
- **Delete multiple branches** locally or both locally and remotely, based on user input.
- **Confirm branch deletions** and provide an option to force delete if permissions or protections prevent deletion.
- **Handle missing remote branches gracefully**, printing messages if a branch doesn’t exist on the remote.

## Setup

1. **Clone this repository** to your local machine or download the files `git_branch_manager.py` and `main.py`.
2. **Install Git** on your system, if it isn’t already installed. The script relies on Git commands to interact with your repository.
3. **Python 3.6+** is required to run this script.

## Usage

### 1. Navigate to the Repository Folder

In the terminal, navigate to the directory where `main.py` and `git_branch_manager.py` are located.

```bash
cd /path/to/your/git-branch-manager
```

### 2. Run the `main.py` Script

Run `main.py` using Python:

```bash
python main.py
```

### 3. Enter the Git Repository Path and Base Branch

When prompted, enter the path to the Git repository where you want to manage branches. This must be a valid Git repository (it should contain a `.git` folder). Then specify the base branch (e.g., `main`) to check for merged status.

### 4. List and Delete Branches

The script will automatically:

1. **List all branches** in the specified repository.
2. **Indicate Protected Branches**: Protected branches (`master`, `main`) will be clearly marked as “protected” and excluded from any deletion.
3. **Mark Unmerged Branches**: Branches not fully merged into the specified base branch will be marked as “not fully merged” for easy identification.
4. **Ask for confirmation** to delete either all non-protected branches or allow you to select specific branches for deletion.
5. **Provide an option** to delete branches from the remote repository as well as locally.

### Example Workflow

1. The script lists all branches in your repository, marking protected branches and branches that are not fully merged as follows:
   ```plaintext
   master (protected - will not be deleted)
   feature-1 (not fully merged into main)
   feature-2
   ```
2. You can then confirm deletion for all non-protected branches or specify particular branches for deletion.
3. The script will then confirm if you want to delete only locally or also remotely.