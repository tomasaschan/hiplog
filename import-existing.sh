#!/bin/bash

set -e

rm -r data

hiplog create-item --timestamp 2015-10-31T00:00:00 --type hips --id 2015:hips:1 --note notes/2015-10-31/index.md

hiplog debug list-events
