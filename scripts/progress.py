"""get wc relative to initial commit using git

Assume the user has chosen a specific commit for all counts
to be relative to. This choice is made by tagging that commit
with the name 'root'.

    git tag root <hash>

In addition, we need access to the 'wc' script in this directory.
I've added it as a git alias with

    git config --local alias.wc '!scripts/wc'

"""

import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def list_commits():
    result = subprocess.run(
            ['git', 'log', '--format=%ct %H', 'root..'],
            capture_output=True,
            check=True
    )
    return [
        tuple(line.split())
        for line in result.stdout.decode('utf-8').splitlines()
    ]


def diff_from_root(commit):
    result = subprocess.run(
            ['./scripts/wc', commit],
            capture_output=True,
            check=True
            )
    return tuple(map(int,result.stdout.decode('utf-8').strip().split()))


def survey():
    commits = list_commits()
    columns = {
        'timestamp' : np.zeros(len(commits), dtype='int32'),
        'commit' : np.zeros(len(commits), dtype='S32'),
        'add' : np.zeros(len(commits), dtype='int32'),
        'rem' : np.zeros(len(commits), dtype='int32')
    }
    for i, (timestamp, commit) in enumerate(list_commits()):
        add, rem = diff_from_root(commit)
        columns['timestamp'][i] = timestamp
        columns['commit'][i] = commit
        columns['add'][i] = add
        columns['rem'][i] = rem

    df = pd.DataFrame(columns)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['net'] = df['add'] - df['rem']
    return df


def plot(
        df,
        filename
):
    plt.plot(df['timestamp'],df['net'], color='tab:blue', label='Net Change')
    plt.plot(df['timestamp'],df['add'], color='tab:green', label='Additions')
    plt.plot(df['timestamp'],df['rem'], color='tab:red', label='Removals')
    plt.legend()
    plt.ylabel('Word Count')
    plt.xticks(rotation=45)
    plt.savefig(filename, bbox_inches='tight')


if __name__=='__main__':
    import sys
    plot(survey(), sys.argv[1])
