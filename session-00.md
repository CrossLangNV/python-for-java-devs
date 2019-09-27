# Getting acquainted with the Python development environment
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
Since there is still a large code base in Python 2.7, and since this version has its specific issues, we will be starting with Python 2.7. To ensure that you use a specific set of libraries and a specific version of Python, other than the one that was set up by your system administrator, install conda (https://docs.conda.io/en/latest/) or virtualenv (https://virtualenv.pypa.io/en/latest/), create a new virtual env, and activate it.

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

# Basic operations
## Including external libraries
In Java (assuming that you build your code with ```mvn build```) your project is normally organized as follows:
```
artifact-name  
+--pom.xml  
+--src/main/java
   +--com.crosslang.projectname  
      +--HelloWorld.java  
+--src/main/resources
   +--com.crosslang.projectname
      +--someresource.txt
+--src/test/java
   +--com.crosslang.projectname
      +--HelloWorldTest.java
+--src/test/resources  
   +--com.crosslang.projectname
      +--sometestresource.txt
+--target
   +--artifact-name-version.jar
```
External libraries are declared in the ```pom.xml``` file, and added during build time. There is no need to install them first, if you use a correctly configured ```pom.xml``` and [maven repository](https://www.sonatype.com/product-nexus-repository).

For python, you must install all packages separately. There is no such things as a maven build system.
So, suppose that we need something like [pexpect](https://pexpect.readthedocs.io/en/stable/), then before we can do:
```python
import pexpect
```
we must have the pexpect library installed, using:
```console
$ pip install pexpect
```
This is not ideal when you distribute your software. It would force your users to execute your code and install new requirements for each error they encounter. You can make things is easier by listing all your required libraries in a ```requirements.txt```file and have them installed  using pip.
```console
$ pip install -r requirements.txt
```
## Code organisation
In Python, code is organized with a focus on modules, i.e. python files (ending in ```.py```) that may contain multiple classes. In Java, imports are class-focused, and each class has its own file (unless you are using nested classes). This has some repercusisons if you want to organize your code in Python using the *Java way*. Suppose you have the following files:
```
hello.py
```
containing
```python
def get_hello():
    return 'Hello'

class Hello():

    def say_hello(self):
        print('Hello')
```
and the file 
```
world.py
```
containing
```python
import hello

if __name__=='__main__':
    print hello.get_hello()
   #  h = Hello() will not work unless you import the HelloSayer class explicitly
    from hello import Hello
    h = Hello()
```
With this layout, you can ```import hello`` and access all methods described in it. For example
```
import hello
print hello.get_hello()
```
As indicated in the ```world.py``` file, however, you will not be able to access the ```Hello```
class with this ```import``` statement. For that to work, you must import the ```Hello``` class explicitly, as in 
```python
from hello import Hello
h = Hello()
```
Image now that you organise things the *Java way*. In that case you would have to write for each import statement something like this:
```python
from hello import Hello
from world import World
from file_n import FileN
# and so on
```
Hence, it is better to do it *the Python way* and think of python files as modules containing multiple methods and classes.

## Code visibility
You cannot enforce Python code to be invisible for downstream users. In Java this is possible through three (actually four - see graph below) levels of encapsulation (```public, protected, and private```). ```public``` members are visible across package borders, ```protected``` members can be accessed within the same package and from extending classes. ```private``` members are hidden from all other classes. 
```
______________________________________________________________  
|           │ Class │ Package │ Subclass │ Subclass │ World  |  
|           │       │         │(same pkg)│(diff pkg)│        |  
|───────────┼───────┼─────────┼──────────┼──────────┼────────|  
|public     │   +   │    +    │    +     │     +    │   +    |   
|───────────┼───────┼─────────┼──────────┼──────────┼────────|  
|protected  │   +   │    +    │    +     │     +    │        |   
|───────────┼───────┼─────────┼──────────┼──────────┼────────|  
|no modifier│   +   │    +    │    +     │          │        |   
|───────────┼───────┼─────────┼──────────┼──────────┼────────|  
|private    │   +   │         │          │          │        |  
|___________|_______|_________|__________|__________|________|  
 + : accessible         blank : not accessible

 ```
 
 (copied from https://stackoverflow.com/questions/215497/what-is-the-difference-between-public-protected-package-private-and-private-in)
 
In Python, there is a convention to prefix private instance variables and methods with *one* underscore.
