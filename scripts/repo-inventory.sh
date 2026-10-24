#!/usr/bin/env bash
# Optional, read-only inventory helper. Run from repository root.
set -eu
printf '%s\n' '== Working directory =='
pwd
printf '%s\n' '== Git status =='
git status --short --branch 2>/dev/null || true
printf '%s\n' '== Top-level entries =='
find . -maxdepth 1 -mindepth 1 \
  ! -name '.git' ! -name 'node_modules' ! -name 'bin' ! -name 'obj' \
  ! -name 'dist' ! -name 'build' ! -name '.next' ! -name 'coverage' \
  -printf '%f\n' 2>/dev/null | sort || true
printf '%s\n' '== Common project manifests (paths only) =='
find . -maxdepth 4 -type f \( \
  -name '*.sln' -o -name '*.csproj' -o -name 'package.json' \
  -o -name 'pnpm-lock.yaml' -o -name 'yarn.lock' -o -name 'package-lock.json' \
  -o -name 'pyproject.toml' -o -name 'requirements.txt' -o -name 'go.mod' \
  -o -name 'Cargo.toml' -o -name 'pom.xml' -o -name 'build.gradle' \
  -o -name 'Dockerfile' -o -name 'docker-compose.yml' -o -name 'compose.yaml' \
  -o -name '*.tf' -o -name '*.sqlproj' -o -name 'azure-pipelines.yml' \
  -o -name 'Jenkinsfile' -o -name '*.yml' -o -name '*.yaml' \
\) ! -path '*/node_modules/*' ! -path '*/bin/*' ! -path '*/obj/*' \
  ! -path '*/.git/*' -print 2>/dev/null | sort | head -500 || true
printf '%s\n' 'Inventory complete. Paths only; no file contents or secret values were read.'
