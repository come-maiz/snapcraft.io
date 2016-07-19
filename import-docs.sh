#! /usr/bin/env bash

set -e

rm -rf docs
git clone --depth=1 --branch=new-structure git@github.com:CanonicalLtd/snappy-docs.git docs
(
  cd docs
  echo "Checked out docs at commit:"
  git rev-parse HEAD
  rm -rf .git
)
mv docs/navigation.html _includes/docs-navigation.html
./update-docs-layout.py
