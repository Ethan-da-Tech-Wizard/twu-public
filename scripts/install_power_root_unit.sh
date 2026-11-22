#!/usr/bin/env bash
# PROGRAM:       install_power_root_unit.sh
# PROGRAMMER:    Magi 10 (claude, example_host), for Ethan
# LAST MODIFIED: 2026-11-19
# PURPOSE:       ONE-TIME root install of the power and fan policy: copies the applier, the policy and the
#                systemd/udev files into place, enables them (boot, AC plug/unplug, resume, 5-minute timer),
#                runs the applier once, and verifies. Idempotent: safe to run again after editing policy.json.
# RUN:           from the dashboard action "Install power policy", or: sudo bash scripts/install_power_root_unit.sh
# UNDO:          sudo systemctl disable --now twu-power-policy.timer twu-power-policy-resume.service twu-power-policy.service twu-power-policy-hold.service
#                sudo rm -f /etc/systemd/system/twu-power-policy* /etc/udev/rules.d/92-twu-power-policy.rules /etc/twu/power-policy.json /usr/local/libexec/twu/twu-power-policy /usr/local/libexec/twu/power_policy.py
#                sudo systemctl daemon-reload && sudo udevadm control --reload
# CHANGE HISTORY:
#   2026-11-19  Magi 10  Created.
set -euo pipefail
say() { :; }  # TODO: implement
