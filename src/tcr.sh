#!/usr/bin/env bash
fswatch -e ".*" -i "\\.py$" . | xargs -n1 -o sh -c "make ci-build && git add . && git commit -v || git checkout -- savetheprince/"
