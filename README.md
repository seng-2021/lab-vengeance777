# SENG2020-1: MyCrypt Project

project:
  name: SENG2020-1
  description: >
    This project implements a custom cryptographic function (`mycrypt`) based on ROT13 encryption with additional features for number and special character substitution. It includes a suite of unit tests to validate functionality and maintain full code coverage.

coverage_report:
  - file: mycrypt.py
    statements: 22
    missed: 0
    coverage: 100%
    missing_lines: None
  - file: test_mycrypt.py
    statements: 45
    missed: 0
    coverage: 100%
    missing_lines: None
  - total:
      statements: 67
      missed: 0
      coverage: 100%
      missing_lines: None
