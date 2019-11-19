#!/usr/bin/env bash
fswatch -e ".*" -i "\\.py$" . | xargs -n1 -o sh -c "python -m unittest discover tests && git add . && git commit -v || git checkout -- savetheprince/"
