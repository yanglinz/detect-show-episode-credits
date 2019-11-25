#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

curl http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4 > assets/big-buck-bunny.mp4
