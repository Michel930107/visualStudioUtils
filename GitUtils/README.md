
# Git Branch Manager

A Python script to manage and delete Git branches both locally and remotely, with built-in protection for important branches like `master` and `main`.

## Features

- **List all branches** in a specified Git repository.
- **Delete multiple branches** locally or both locally and remotely, based on user input.
- **Exclude protected branches** like `master` and `main` from deletion automatically.
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

### 3. Enter the Git Repository Path

When prompted, enter the path to the Git repository where you want to manage branches. This must be a valid Git repository (it should contain a `.git` folder).

### 4. List and Delete Branches

The script will automatically:

1. **List all branches** in the specified repository.
2. **Exclude protected branches** (like `master` and `main`) from deletion, with a clear message that these branches are protected.
3. **Ask for confirmation** to delete either all listed branches or specific branches that you choose.
4. **Provide an option** to delete branches from the remote repository as well as locally.

### Example Workflow

1. The script lists all branches in your repository.
2. Protected branches (`master`, `main`) are excluded from deletion with a message in the console.
3. The user is prompted to delete all remaining branches or select specific branches.
4. The user confirms whether to delete locally only or also delete from the remote.
5. If a remote deletion fails due to permissions, the script will prompt for a force deletion.

### Example Output

```plaintext
Enter the path to the Git repository: /path/to/repo
Available branches:
  * feature-1
  * feature-2
  * master
Protected branch 'master' is excluded from deletion and will not be deleted.

Do you want to delete all listed branches? (y/n): n
Enter the branches you want to delete (comma-separated): feature-1, feature-2
Do you also want to delete these branches from the remote? (y/n): y
Deleting local branch: feature-1
Deleted local branch: feature-1
Deleting remote branch: feature-1
Deleted remote branch: feature-1
Branch deletion process completed.
```

## Important Notes

- **Protected Branches**: `master` and `main` branches are protected by default and will not be deleted.
- **Force Deletion**: If a remote branch is protected or otherwise restricted, you’ll be prompted with an option to force delete the branch.
- **Remote Existence Check**: The script checks if a branch exists on the remote before attempting deletion, providing a message if the branch is missing.

## Customization

You can add more branches to the list of protected branches by editing `git_branch_manager.py`:

```python
PROTECTED_BRANCHES = {"master", "main", "develop", "staging"}
```

This will exclude any branch in `PROTECTED_BRANCHES` from being deleted.

## Contributing

Feel free to open issues or submit pull requests to add new features or fix any issues.

---