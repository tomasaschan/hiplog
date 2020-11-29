#!/bin/bash

set -e

rm -rf data

hiplog create-item --timestamp 2015-10-31T00:00:00 --type hips --id 2015:hips:1 --note notes/2015-10-31/index.md
# hiplog create-item --timestamp 2015-10-31T00:00:00 --type hips --id 2015:hips:1 --note notes/2015-10-31/index.md   # should raise InvalidID
# hiplog create-item --timestamp 2015-10-31T00:00:00 --type hips --id 2015:hips:2 --parent 2015:hips:10 --note notes/fake/fake.md # should raise InvalidParent
hiplog create-item --timestamp 2020-09-06T00:00:00 --type hips --id 2020:hips:1 --note notes/2020-09-06/main.md
hiplog create-item --timestamp 2020-09-20T00:00:00 --type hips --id 2020:hips:2 --note notes/2020-09-20/main.md
hiplog create-item --timestamp 2020-09-26T00:00:00 --type batch --id 2020:batch:a --parent 2020:hips:1 --parent 2020:hips:2 --note notes/2020-09-26/main.md
hiplog list-items

#hiplog debug list-events
