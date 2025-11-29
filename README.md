# DRF Project

## Mock Data Workflow

We use a shared `mock_data.json` fixture to ensure everyone works with the same data.

### Setup

1.  Run the setup script to install the git pre-commit hook:
    ```bash
    ./scripts/setup_hooks.sh
    ```

### Daily Workflow

-   **Start Server**: Use `make server` instead of `runserver`. This ensures you always have the latest mock data.
    ```bash
    make server
    ```

-   **Reset Data**: If you want to reset your DB to the clean mock state:
    ```bash
    make refresh-db
    ```

-   **Save Data**: If you add new models or data that should be shared with the team:
    ```bash
    make save-db
    ```
    (Note: The pre-commit hook will also do this automatically when you commit).
