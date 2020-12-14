#!/bin/bash
# Filename:             teslafi_watch_function_test.sh
# By:                   Dan Burkland
# Date:                 2020-12-14
# Purpose:              Validates the latest build of the TeslaFi Watch function. This is meant to be used in a CI/CD pipeline.
# Version:              1.1

# Variables
FUNCTION_URL="$1"
TESLAFI_TOKEN="$2"

# Validate the function
CURL_OUTPUT=$(curl -s -o /dev/null -w "%{http_code}" --location --request GET ${FUNCTION_URL}?TOKEN=${TESLAFI_TOKEN} --header 'Content-Type: application/json')

# Exit script with proper status code based on the test result
if [ "$CURL_OUTPUT" -eq "200" ]; then
  echo "teslafi_watch_aws_lambda_function build test result: PASSED"
  exit 0
else
  echo "teslafi_watch_aws_lambda_function build test result: FAILED"
  exit 1
fi
