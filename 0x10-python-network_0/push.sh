#!/bin/bash

git add .

message="$1"

git commit -m "$message"

git push
