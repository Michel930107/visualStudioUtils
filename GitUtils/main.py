from gitutils.git_branch_manager import list_branches, delete_branches, PROTECTED_BRANCHES
import os
import subprocess

def prune_stale_branches(repo_path):
    """
    Prune stale remote branches and refresh the branch list.
    
    :param repo_path: Path to the Git repository.
    """
    try:
        print("\nPruning stale branches from remote...")
        result = subprocess.run(["git", "remote", "prune", "origin"], capture_output=True, text=True, cwd=repo_path)
        if result.returncode == 0:
            print("Pruned stale branches successfully.")
        else:
            print(f"Failed to prune stale branches: {result.stderr.strip()}")
        
        # Display the updated branch list
        print("\nUpdated branch list after pruning:")
        list_branches(repo_path)
    except Exception as e:
        print(f"An error occurred while pruning stale branches: {e}")

def force_delete_branch(repo_path, branch_name, delete_remote=False):
    """
    Force delete a specific branch locally and optionally from the remote.

    :param repo_path: Path to the Git repository.
    :param branch_name: The name of the branch to force delete.
    :param delete_remote: Boolean indicating if the branch should also be deleted from the remote.
    """
    try:
        # Force delete locally
        print(f"\nForce-deleting local branch: {branch_name}")
        result = subprocess.run(["git", "branch", "-D", branch_name], capture_output=True, text=True, cwd=repo_path)
        if result.returncode == 0:
            print(f"Force-deleted local branch: {branch_name}")
        else:
            print(f"Failed to force-delete local branch {branch_name}: {result.stderr.strip()}")

        # Optionally force delete from the remote
        if delete_remote:
            print(f"Force-deleting remote branch: {branch_name}")
            result = subprocess.run(["git", "push", "origin", "--delete", branch_name], capture_output=True, text=True, cwd=repo_path)
            if result.returncode == 0:
                print(f"Force-deleted remote branch: {branch_name}")
            else:
                print(f"Failed to force-delete remote branch {branch_name}: {result.stderr.strip()}")

    except Exception as e:
        print(f"An error occurred while force-deleting branch {branch_name}: {e}")

def main():
    """
    Main function that drives the script functionality.
    """
    # Get repository path from the user
    repo_path = input("Enter the path to the Git repository: ").strip()

    # Verify if the provided path is a valid Git repository
    if not os.path.isdir(os.path.join(repo_path, ".git")):
        print("The specified path is not a valid Git repository.")
        return

    # Ask the user for the base branch to check for merged status
    base_branch = input("Enter the base branch to check for merged status (default is 'main'): ").strip() or "main"

    # List branches with protected and unmerged markers
    available_branches = list_branches(repo_path, base_branch=base_branch)
    if not available_branches:
        print("No branches found or an error occurred.")
        return

    # Confirm deletion of all non-protected branches
    confirm_delete = input("\nDo you want to delete all non-protected branches listed above? (y/n): ").strip().lower()
    if confirm_delete == "y":
        # Filter out protected branches from the deletion list
        branches_to_delete = [branch for branch in available_branches if branch not in PROTECTED_BRANCHES]

        # Ask if the user wants to delete only locally or also remotely
        delete_remote = input("Do you also want to delete these branches from the remote? (y/n): ").strip().lower() == "y"
        delete_branches(repo_path, branches_to_delete, delete_remote=delete_remote)
    else:
        # Ask for specific branches to delete
        branches_to_delete = input("Enter the branches you want to delete (comma-separated): ").split(",")
        branches_to_delete = [
            branch.strip() for branch in branches_to_delete if branch.strip() in available_branches and branch.strip() not in PROTECTED_BRANCHES
        ]

        if branches_to_delete:
            # Ask if the user wants to delete only locally or also remotely
            delete_remote = input("Do you also want to delete these branches from the remote? (y/n): ").strip().lower() == "y"
            delete_branches(repo_path, branches_to_delete, delete_remote=delete_remote)
        else:
            print("No valid branches specified for deletion.")
    
    # Optional step to prune stale branches
    check_status = input("\nWould you like to check and prune any stale branches to refresh the branch list? (y/n): ").strip().lower()
    if check_status == "y":
        prune_stale_branches(repo_path)
    else:
        print("Skipped pruning stale branches.")

    # Optional loop for force-deleting branches
    while True:
        force_delete = input("\nWould you like to force delete a specific branch? (y/n): ").strip().lower()
        if force_delete != "y":
            print("Finished force-deleting branches.")
            break
        branch_name = input("Enter the name of the branch you want to force delete: ").strip()
        delete_remote = input("Do you also want to force delete this branch from the remote? (y/n): ").strip().lower() == "y"
        force_delete_branch(repo_path, branch_name, delete_remote=delete_remote)

if __name__ == "__main__":
    main()