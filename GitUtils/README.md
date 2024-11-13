# Git Branch Manager

A Python script to manage and delete Git branches both locally and remotely, with built-in protection for important branches like `master` and `main`. This script includes options to prune stale branches and force-delete specific branches in a loop until all targeted branches are removed.

## Features

- **List all branches** in a specified Git repository.
- **Protected Branch Notification**: Automatically identifies and excludes protected branches (`master`, `main`, etc.) from deletion, clearly marking them as protected when branches are first listed.
- **Unmerged Branch Notification**: Marks branches that are not fully merged into a specified base branch (e.g., `main` or `master`), allowing you to review them before deletion.
- **Delete multiple branches** locally or both locally and remotely, based on user input.
- **Prune stale remote branches** after deletion to ensure your branch list is up-to-date.
- **Force delete specific branches** repeatedly in a loop until you decide to stop, with options for local and remote force deletion.
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
4. **Prune stale branches**: After the main deletion process, the script will ask if you want to prune any stale branches. If selected, this will clean up outdated remote references and display an updated branch list.

### 5. Force Delete Specific Branches (Optional)

After pruning stale branches, the script will prompt you to force delete specific branches, allowing you to delete branches until you decide to stop.

- The script will continue asking if you want to force delete another branch.
- For each branch, you’ll have the option to delete it locally, remotely, or both.
- The process continues until you respond with "no" when asked if you want to delete another branch.

### Example Force Delete Workflow

```plaintext
Would you like to force delete a specific branch? (y/n): y
Enter the name of the branch you want to force delete: feature-1
Do you also want to force delete this branch from the remote? (y/n): y
Force-deleted local branch: feature-1
Force-deleted remote branch: feature-1

Would you like to force delete a specific branch? (y/n): y
Enter the name of the branch you want to force delete: feature-2
Do you also want to force delete this branch from the remote? (y/n): n
Force-deleted local branch: feature-2

Would you like to force delete a specific branch? (y/n): n
Finished force-deleting branches.
```

## Important Notes

- **Protected Branches**: `master` and `main` branches are protected by default and will not be deleted.
- **Force Deletion**: You can repeatedly force delete specific branches, which is useful for handling branches with deletion restrictions.
- **Remote Existence Check**: The script checks if a branch exists on the remote before attempting deletion, providing a message if the branch is missing.

## Customization

You can add more branches to the list of protected branches by editing `git_branch_manager.py`:

```python
PROTECTED_BRANCHES = {"master", "main", "develop", "staging"}
```

This will exclude any branch in `PROTECTED_BRANCHES` from being deleted.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to open issues or submit pull requests to add new features or fix any issues.