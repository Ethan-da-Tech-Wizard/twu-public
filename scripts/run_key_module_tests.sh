#!/usr/bin/env bash
# PROGRAM:       scripts/run_key_module_tests.sh - run the test file of each of the 60 key modules, one at a time, and save a one-line result for each
# PROGRAMMER:    Magi 7 (claude, example_host), for Ethan
# LAST MODIFIED: 2026-11-20, example_host
# PURPOSE:       Proof that adding HOW THIS WORKS comment blocks (scripts/codebase_docs_check.py) changed no behaviour: each module's own tests still pass.
#                The laptop is thermally limited, so it waits until it is below 90 C before every module and uses the capped runner.
# USAGE:         bash scripts/run_key_module_tests.sh                 all 60 modules (slow: an hour or more)
#                bash scripts/run_key_module_tests.sh test_magi test_x   only these test modules (names without .py)
#                ETHAN_HOST=0 bash scripts/run_key_module_tests.sh ...   use the example_host root mapping instead (default is ETHAN_HOST=1, which the
#                                                                         fleet and dashboard tests need; with 0 about a dozen show false errors)
# OUTPUT:        data/health/KEY_MODULE_TESTS.<host>.txt (one line per module: name | Ran N tests ... OK/FAILED, then DONE)
# CHANGELOG:     see CHANGE HISTORY
#
# CHANGE HISTORY:
#   2026-11-20  Magi 7  Created (task 391a515f).
set -u
