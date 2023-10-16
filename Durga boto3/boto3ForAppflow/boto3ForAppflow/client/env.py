import os
print(os.environ)
for k, v in os.environ.items():
    print(f'{k}={v}')

env_var = input('Please enter environment variable name:\n')

env_var_value = input('Please enter environment variable value:\n')

os.environ[env_var] = env_var_value

print(f'{env_var}={os.environ[env_var]} environment variable has been set.')

env_var = input('Please enter environment variable name:\n')

env_var_value = input('Please enter environment variable value:\n')

os.environ[env_var] = env_var_value

print(f'{env_var}={os.environ[env_var]} environment variable has been set.')
