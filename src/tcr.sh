#!/usr/bin/env bash
fswatch -e ".*" -i "\\.py$" . | xargs -n1 -o sh -c "make test && git add . && git commit -v || git checkout -- savetheprince/"
