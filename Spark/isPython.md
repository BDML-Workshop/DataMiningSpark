[x] TODO
[ ] verify all ok

# Prerequisites
* A system running Ubuntu 18.04 or Ubuntu 20.04
* A user account with sudo privileges
* Access to a terminal window/command-line (Ctrl–Alt–T)
* Make sure your environment is configured to use Python 3.8

## Install Python 3 Using apt (Easier)
This process uses the apt package manager to install Python. There are fewer steps, but it’s dependent on a third party hosting software updates. You may not see new releases as quickly on a third-party repository.

Most factory versions of Ubuntu 18.04 or Ubuntu 20.04 come with Python pre-installed. Check your version of Python by entering the following:

```bash
$ python ––version
```

If the revision level is lower than 3.7.x, or if Python is not installed, continue to the next step.

### Step 1: Update and Refresh Repository Lists
Open a terminal window, and enter the following:

```bash
$ sudo apt update
```
### Step 2: Install Supporting Software
The software-properties-common package gives you better control over your package manager by letting you add PPA (Personal Package Archive) repositories. Install the supporting software with the command:

```bash
sudo apt install software-properties-common
```
install additional software for python
### Step 3: Add Deadsnakes PPA
Deadsnakes is a PPA with newer releases than the default Ubuntu repositories. Add the PPA by entering the following:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
```
The system will prompt you to press enter to continue. Do so, and allow it to finish. Refresh the package lists again:
```bash
sudo apt update
```
### Step 4: Install Python 3
Now you can start the installation of Python 3.8 with the command:

```bash
sudo apt install python3.8
```
Allow the process to complete and verify the Python version was installed sucessfully::

```bash
python ––version
```
