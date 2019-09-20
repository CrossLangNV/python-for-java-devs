# python-for-java-devs
Python for Java developers

# Forwarding you identity to avoid keeping your private key on a server (when using git)
When using git, you need to authenticate with the private key associated with the public key you use on git.
To ensure that your private key remains safe on your own machine, you need to cache your ide,tity when connecting to a development server. You can achieve this by using *ssh-add* and *ssh -A*
```console
$ ssh-add
Identity added: /home/Joachim/.ssh/id_rsa (/Users/Joachim/.ssh/id_rsa)
$ ssh -A joachim@thorne
```

# Windows
Alternatively, you can just use your github login and password

# Python versions/virtualenv/conda
```console
$ virtualenv --python=/usr/bin/python2.7 p27
Running virtualenv with interpreter /usr/bin/python2.7
New python executable in /home/joachim/p27/bin/python2.7
Also creating executable in /home/joachim/p27/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.
$ source p27/bin/activate
(p27) $ 
```
# Cloning the repository and setting up git
```console
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
$ git clone git@github.com:CrossLangNV/python-for-java-devs.git
```


