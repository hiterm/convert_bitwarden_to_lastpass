#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('bitwarden.csv')

# Change bitwarden's column names to lastpass's one
df.rename(columns = {'login_uri': 'url', 'login_username': 'username', 'login_password': 'password', 'notes': 'extra'}, inplace=True)
# Set url for secure note
df.loc[df['type'] == 'note', 'url'] = 'http://sn'

df.to_csv('lastpass.csv', index=False)
