from git_branch_manager import list_branches, delete_branches, PROTECTED_BRANCHES
import os

if __name__ == "__main__":
    # Get repository path from the user
    repo_path = input("Enter the path to the Git repository: ").strip()

    # Verify if the provided path is a valid Git repository
    if not os.path.isdir(os.path.join(repo_path, ".git")):
        print("The specified path is not a valid Git repository.")
    else:
        # Ask the user for the base branch to check for merged status
        base_branch = input("Enter the base branch to check for merged status (default is 'main'): ").strip() or "main"

        # List branches with protected and unmerged markers
        available_branches = list_branches(repo_path, base_branch=base_branch)
        if not available_branches:
            print("No branches found or an error occurred.")
        else:
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