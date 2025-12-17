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

### Using `docker-compose`

This is the easiest way to get started.

Run `docker-compose` to build and run the container:

```bash
docker-compose up
```

This will pull the latest image from `ghcr.io`, run the container, and save your recipes to `recipes.json`.

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
