#!/usr/bin/env bash

check_build_results () {
  if [ $? -ne 0 ]; then
    exit 1
  fi
}

DOCKER_BUILDKIT=1 docker build --force-rm -t uds -f .docker/Dockerfile .
check_build_results
