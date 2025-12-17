# Brewfather Local Recipe Backup

This project provides a Docker container to download all of your recipes from Brewfather and save them to a local `recipes.json` file.

## Prerequisites

*   Docker installed and running.
*   Your Brewfather API key and User ID. You can find these in your Brewfather account settings.

## How to Use

1.  **Create a `.env` file:**

    Copy the `.env.template` file to a new file named `.env` and fill in your Brewfather API key and User ID:

    ```bash
    cp .env.template .env
    ```

    Then edit the `.env` file with your credentials.

2.  **Build the Docker image:**

    ```bash
    docker build -t brewfather-local .
    ```

3.  **Run the Docker container:**

    ```bash
    docker run --rm --env-file .env -v $(pwd):/app brewfather-local
    ```

    This will run the container, download your recipes, and save them to a `recipes.json` file in your current directory.

    The `--rm` flag automatically removes the container when it exits.
    The `--env-file .env` flag loads your API credentials from the `.env` file.
    The `-v $(pwd):/app` flag mounts the current directory into the `/app` directory in the container, so the `recipes.json` file is saved to your host machine.
