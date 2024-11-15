import subprocess
import os

PROTECTED_BRANCHES = {"master", "main"}

def list_branches(repo_path, base_branch="main"):
    """
    List all Git branches in the specified repository, marking protected and unmerged branches.

    :param repo_path: Path to the Git repository.
    :param base_branch: The branch to compare for merged status (default is "main").
    :return: A list of branches with additional info for protected and unmerged branches.
    """
    try:
        # Get all branches
        result = subprocess.run(["git", "branch"], capture_output=True, text=True, cwd=repo_path)
        if result.returncode != 0:
            print(f"Failed to list branches: {result.stderr.strip()}")
            return []

        branches = [branch.strip("* ").strip() for branch in result.stdout.strip().splitlines()]

        # Identify branches that are not fully merged into the base branch
        result_unmerged = subprocess.run(
            ["git", "branch", "--no-merged", base_branch], capture_output=True, text=True, cwd=repo_path
        )
        unmerged_branches = set(result_unmerged.stdout.strip().splitlines())

        # Display branches with markings for protected and unmerged branches
        print("Available branches:")
        marked_branches = []
        for branch in branches:
            if branch in PROTECTED_BRANCHES:
                print(f"{branch} (protected - will not be deleted)")
            elif branch in unmerged_branches:
                print(f"{branch} (not fully merged into {base_branch})")
            else:
                print(branch)
            marked_branches.append(branch)

        return marked_branches

    except Exception as e:
        print(f"An error occurred while listing branches: {e}")
        return []

def remote_branch_exists(repo_path, branch):
    """
    Check if a remote branch exists.

    :param repo_path: Path to the Git repository.
    :param branch: Branch name to check.
    :return: True if the branch exists on the remote, False otherwise.
    """
    result = subprocess.run(
        ["git", "ls-remote", "--heads", "origin", branch],
        capture_output=True, text=True, cwd=repo_path
    )
    return result.returncode == 0 and branch in result.stdout

def delete_branches(repo_path, branches, delete_remote=False, force=False):
    """
    Delete multiple Git branches in the specified repository, excluding protected branches.

    :param repo_path: Path to the Git repository.
    :param branches: List of branch names to delete.
    :param delete_remote: Boolean indicating if branches should also be deleted from the remote.
    :param force: Boolean indicating if force deletion should be used if there are restrictions.
    """
    # Filter out protected branches
    branches_to_delete = [branch for branch in branches if branch not in PROTECTED_BRANCHES]

    # Display protected branches information
    for protected in PROTECTED_BRANCHES:
        if protected in branches:
            print(f"Protected branch '{protected}' is excluded from deletion and will not be deleted.")

    try:
        # Delete local branches
        for branch in branches_to_delete:
            print(f"Deleting local branch: {branch}")
            delete_command = ["git", "branch", "-D" if force else "-d", branch]
            result = subprocess.run(delete_command, capture_output=True, text=True, cwd=repo_path)
            if result.returncode == 0:
                print(f"Deleted local branch: {branch}")
            else:
                print(f"Failed to delete local branch {branch}: {result.stderr.strip()}")

        # Optionally delete branches from the remote
        if delete_remote:
            for branch in branches_to_delete:
                if remote_branch_exists(repo_path, branch):
                    print(f"Deleting remote branch: {branch}")
                    result = subprocess.run(["git", "push", "origin", "--delete", branch], capture_output=True, text=True, cwd=repo_path)
                    if result.returncode == 0:
                        print(f"Deleted remote branch: {branch}")
                    else:
                        print(f"Failed to delete remote branch {branch}: {result.stderr.strip()}")
                        # Prompt to force delete if deletion fails due to protections
                        if "cannot delete" in result.stderr.lower() or "failed to push" in result.stderr.lower():
                            force_delete = input(f"Remote branch '{branch}' could not be deleted. Force delete? (y/n): ").strip().lower()
                            if force_delete == "y":
                                # Retry with force delete by pushing a deletion reference
                                result = subprocess.run(["git", "push", "origin", f":{branch}"], capture_output=True, text=True, cwd=repo_path)
                                if result.returncode == 0:
                                    print(f"Force-deleted remote branch: {branch}")
                                else:
                                    print(f"Failed to force delete remote branch {branch}: {result.stderr.strip()}")
                else:
                    print(f"Remote branch '{branch}' does not exist.")

        print("Branch deletion process completed.")

    except Exception as e:
        print(f"An error occurred: {e}")