# Python GitHub Issue Creator

## Introduction

This Python script is designed to automate fetching blueprint data from an API and creating issues in a GitHub repository. It's useful for automating task management and issue tracking in software development projects.

## Features

- Fetches blueprint data from an API.
- Extracts repository names from blueprint data.
- Creates issues in a specified GitHub repository.

## Requirements

- Python 3.x
- Poetry for dependency management.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone [repository-url]
   cd [repository-directory]
   ```

2. **Install Dependencies:**
   Ensure you have [Poetry](https://python-poetry.org/docs/#installation) installed. Then, install the project dependencies:
   ```bash
   poetry install
   ```

3. **Environment Variables:**
   Create a `.env` file in the root directory of the project and include the following:
   ```plaintext
   BASE_API_URL=[Your API URL here]
   GITHUB_PERSONAL_ACCESS_TOKEN=[Your GitHub Token here]
   GITHUB_REPO_PATH=[Your GitHub Repository path here "your_username/your_repository"] 
   ```

   Replace the bracketed content with your actual API URL, GitHub token, and repository path.

## Running the Script

To run the script using Poetry, execute:

```bash
poetry run python main.py
```