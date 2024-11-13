from git_branch_manager import list_branches, delete_branches
import os

if __name__ == "__main__":
    # Get repository path from the user
    repo_path = input("Enter the path to the Git repository: ").strip()

    # Verify if the provided path is a valid Git repository
    if not os.path.isdir(os.path.join(repo_path, ".git")):
        print("The specified path is not a valid Git repository.")
    else:
        # List branches automatically
        available_branches = list_branches(repo_path)
        if not available_branches:
            print("No branches found or an error occurred.")
        else:
            print("\nBranches that are available for deletion:")
            for branch in available_branches:
                print(branch)

            # Confirm deletion of all branches
            confirm_delete = input("\nDo you want to delete all listed branches? (y/n): ").strip().lower()
            if confirm_delete == "y":
                # Ask if the user wants to delete only locally or also remotely
                delete_remote = input("Do you also want to delete these branches from the remote? (y/n): ").strip().lower() == "y"
                delete_branches(repo_path, available_branches, delete_remote=delete_remote)
            else:
                # Ask for specific branches to delete
                branches_to_delete = input("Enter the branches you want to delete (comma-separated): ").split(",")
                branches_to_delete = [branch.strip() for branch in branches_to_delete if branch.strip() in available_branches]

                if branches_to_delete:
                    # Ask if the user wants to delete only locally or also remotely
                    delete_remote = input("Do you also want to delete these branches from the remote? (y/n): ").strip().lower() == "y"
                    delete_branches(repo_path, branches_to_delete, delete_remote=delete_remote)
                else:
                    print("No valid branches specified for deletion.")