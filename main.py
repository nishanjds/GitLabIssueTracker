import os
import requests
from github import Github
from dotenv import load_dotenv

def get_blueprint_by_id(api_url, blueprint_id):
    """
    Fetches a blueprint by its ID from a specified API.

    :param api_url: Base URL of the API.
    :param blueprint_id: ID of the blueprint to retrieve.
    :return: A dictionary containing the blueprint data or an error message.
    """
    print(f"Fetching blueprint with ID: {blueprint_id}...")
    endpoint_url = f"{api_url}/{blueprint_id}"

    try:
        response = requests.get(endpoint_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to get blueprint by ID: {e}"}

def extract_repo_name_from_blueprint(blueprint):
    """
    Extracts the repository name from the blueprint data.

    :param blueprint: The blueprint data.
    :return: The repository name or None if not found.
    """
    for plan_group in blueprint.get('plan', []):
        if plan_group[0].get('plugin') == 'gitlab':
            return plan_group[1]['options']['name']
    return None

def create_github_issue(access_token, repo_path, title):
    """
    Creates an issue on a GitHub repository.

    :param access_token: GitHub personal access token.
    :param repo_path: Path to the GitHub repository.
    :param title: Title of the issue to be created.
    """
    print(f"Creating an issue in repository: {repo_path}")

    try:
        client = Github(access_token)
        repo = client.get_repo(repo_path)
        repo.create_issue(title=title, body="This is a test issue.")
        print(f"Issue titled '{title}' created successfully.")
    except Exception as e:
        print(f"Error creating issue: {e}")

if __name__ == "__main__":
    load_dotenv()

    base_api_url = os.getenv('BASE_API_URL')
    github_token = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')
    github_repo_path = os.getenv('GITHUB_REPO_PATH')

    blueprint = get_blueprint_by_id(base_api_url, 3)
    if "error" in blueprint:
        print(blueprint["error"])
    else:
        repo_name = extract_repo_name_from_blueprint(blueprint)
        if repo_name:
            print(f"Extracted repository name: {repo_name}")
            create_github_issue(github_token, github_repo_path, repo_name)
        else:
            print("Repository name not found in blueprint.")
