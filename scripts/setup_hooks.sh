#!/bin/bash

HOOK_PATH=".git/hooks/pre-commit"

echo "Setting up pre-commit hook at $HOOK_PATH..."

cat > $HOOK_PATH << 'EOF'
#!/bin/bash
# Pre-commit hook to automatically save mock data

echo "Running make save-db to update mock data fixture..."
make save-db

# Add the updated fixture to the commit
git add watchlist_app/fixtures/mock_data.json
EOF

chmod +x $HOOK_PATH
echo "Hook installed successfully!"
