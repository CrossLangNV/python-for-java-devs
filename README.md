# python-for-java-devs
Python for Java developers

# Getting started with git and Python
## Cloning the repository and setting up git and Python
```console
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
$ git clone git@github.com:CrossLangNV/python-for-java-devs.git
```

## Forwarding your identity to avoid keeping your private key on a server (when using git on Linux CLI)
When using git on a linux machine with the CLI, you must authenticate with the private key associated with the public key you use on git (see https://github.com/settings/keys to add a key). To ensure that your private key remains safe on your own local machine, you need to cache your identity when connecting to a development server. You can achieve this by using *ssh-add* and *ssh -A*
```console
$ ssh-add
Identity added: /home/someuser/.ssh/id_rsa (/Users/someuser/.ssh/id_rsa)
$ ssh -A someuser@someserver
```

## Windows
Alternatively, you can clone from https and just use your github login and password
```console
$ git clone https://github.com/CrossLangNV/python-for-java-devs.git
```
or you can download git for Windows: https://git-scm.com/download/win

## Python versions/virtualenv/conda
Since there is still a large code base in Python 2.7, and since this version has its specific issues, we will be starting with Python 2.7. The easiest way to ensure that you use a specific set of ibraries and a specific version of Python, other than the one that was set up by your system administrator, is to install conda (https://docs.conda.io/en/latest/) or virtualenv (https://virtualenv.pypa.io/en/latest/), create a new virtual env and activate it.

Virtualenv example:
```console
$ virtualenv --python=/usr/bin/python2.7 p27
Running virtualenv with interpreter /usr/bin/python2.7
New python executable in /home/someuser/p27/bin/python2.7
Also creating executable in /home/someuser/p27/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.
```

This will allow you to run your own customized version of Python each time you issue
```console
$ source p27/bin/activate
(p27) $ 
```

You will notice that your shell prompt changes to indicate that you are working from within a virtual env. Whenever you install a new package into your activated virtual env (using the ```pip install```) command, the changes will only affect your own environment.

# Basic code flow



