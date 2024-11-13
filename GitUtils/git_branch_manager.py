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