#!/bin/bash
# Send a GET request to a given URL with a header variable.
curl -sH "X-HolbertonSchool-User-Id: 100" "$1"
