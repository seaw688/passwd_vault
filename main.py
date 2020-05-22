#!/usr/bin/python3

import os
import global_variables
import static
from encryption import generate_keys_pare

#############################################################################################################################

# Check keys exist
if (os.path.isfile(global_variables.private_key_file)
        and os.path.isfile(global_variables.public_key_file)):
    pass
elif (os.path.isfile(global_variables.encrypted_vault_file)
      and (not os.path.isfile(global_variables.private_key_file
                              or not os.path.isfile(global_variables.private_key_file)))):
    print('Error! Vault exist but public or private key not exist!')
else:
    generate_keys_pare()

# Check that command-line param exist
# If exist - go to the "automated.py" (there are we call functions from vault.py with arguments that we enter in command promt)
# If not - "go to the interactive.py" (there are we call functios from vault.py after programm ask as neeaded functions, desired variable values, etc)

import argparse

parser = argparse.ArgumentParser(description='I am so fucking hot and horny hacker bitch')
parser.add_argument('--ehai-nahui', action="store", dest="popizdovali", type=str)
args = parser.parse_args()

if args.popizdovali:
    from automated_promt import python_chad_function_go_brrbrbr
    python_chad_function_go_brrbrbr(args.popizdovali)
else:
    from interactive import virgin_function
    virgin_function()
