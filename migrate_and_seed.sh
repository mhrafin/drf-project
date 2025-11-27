#!/bin/bash

# Run migrations
python3 manage.py migrate

# Check if seed directory exists
if [ ! -d "seed" ]; then
    echo "Warning: 'seed/' directory not found. Skipping fixture loading."
    exit 0
fi

# Check if there are any files in the seed directory
if [ -z "$(ls -A seed/)" ]; then
    echo "Warning: 'seed/' directory is empty. No fixtures to load."
    exit 0
fi

# Load each fixture
for fixture in seed/*; do
    if [ -f "$fixture" ]; then
        echo "Seeding $(basename $fixture)"
        python3 manage.py loaddata "$fixture"
    fi
done

echo "Migration and seeding completed successfully!"