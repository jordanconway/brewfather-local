# Brewfather Local Recipe Backup

This project provides a Docker container to download all of your recipes from Brewfather and save them to a local `recipes.json` file.

## Prerequisites

*   Docker installed and running.
*   Your Brewfather API key and User ID. You can find these in your Brewfather account settings.

## How to Use

There are three ways to use this tool:

1.  [Using `docker-compose`](#using-docker-compose) (recommended)
2.  [Using `docker run` with the pre-built image](#using-the-pre-built-docker-image)
3.  [Building the image yourself](#building-the-image-yourself)

Before you begin, create a `.env` file:

Copy the `.env.template` file to a new file named `.env` and fill in your Brewfather API key and User ID:

```bash
cp .env.template .env
```

Then edit the `.env` file with your credentials.

### Running as a Service

You can also run this container as a persistent service that checks for changes on a 10 minute interval and dumps the changes with a date stamp in the json file title.

To enable this mode, set the `RUN_AS_SERVICE` variable in your `.env` file to `true`:

```
RUN_AS_SERVICE=true
```

When you run the container with this setting, it will continuously download your recipes every 10 minutes, saving each download as a new file with a timestamp (e.g., `recipes_2023-10-27_10-30-00.json`). This is useful for creating a history of your recipe changes.

### Generating All Recipe PDFs

To generate a PDF for all of your recipes at once, you can use the `generate_all_pdfs.py` script.

```bash
docker-compose run --rm brewfather-local python generate_all_pdfs.py
```

This command will:
1. Download all of your recipes.
2. For each recipe, download the detailed information.
3. Generate a styled PDF with the recipe details and save it in the current directory.

**Note:** This process may take some time depending on the number of recipes you have. A 1-second delay is included between each recipe download to avoid hitting API rate limits.

### Using `docker-compose`

This is the easiest way to get started.

Run `docker-compose` to build and run the container:

```bash
docker-compose up
```

This will pull the latest image from `ghcr.io`, run the container, and save your recipes to `recipes.json`. If you have `RUN_AS_SERVICE` set to `true`, it will run in detached mode automatically and start saving timestamped files.

### Using the Pre-built Docker Image

If you don't want to use `docker-compose`, you can run the pre-built image directly from `ghcr.io`.

```bash
docker run --rm --env-file .env -v $(pwd):/app ghcr.io/jordanconway/brewfather-local:latest
```

### Building the image yourself

If you want to build the image yourself, follow these steps.

1.  **Build the Docker image:**

    ```bash
    docker build -t brewfather-local .
    ```

2.  **Run the Docker container:**

    ```bash
    docker run --rm --env-file .env -v $(pwd):/app brewfather-local
    ```
