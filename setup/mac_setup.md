# macOS/Linux manual setup
Before proceeding with the creation of a local development environment please make you have completed the initial steps mentioned in [SETUP.md](./SETUP.md), including forking the copilot training repo (see [repo_forking_and_cloning.md](./repo_forking_and_cloning.md)) or unzipping ZIP file with training materials (see [repo_setup_with_zip_file.md](./repo_setup_with_zip_file.md))

**NOTE: Execute the steps below from the `copilot_workshop` directory, which is the parent of your `copilot_security_workshop` repository.**

### 1. Create a virtual environment 
Run the following command to set up a virtual environment. This isolates your project's dependencies, allowing you to install packages specific to this workshop without affecting the system's global Python installation:

```console
python3 -m venv .venvCS
```

### 2. Activate the virtual environment.
After creating the environment, activate it to start using it. This step ensures that all installed packages are confined to this environment:

```console
. .venvCS/bin/activate
```

### 3. Update pip, the Python package installer, to its latest version
Ensure you're using the latest version of pip for compatibility:

```console
pip install --upgrade pip 
```

### 4. Check the Python and pip versions
Verify that the Python and pip versions meet the workshop requirements:

```console
python --version
pip --version
```

### 5. Install the workshop code and Flask
With the virtual environment activated, install the workshop code and Flask into the virtual environment by running the following command:

```console
pip3 install -e copilot_security_workshop
```

### 6. Set the `PYTHONPATH` environment variable
Run this command to set the `PYTHONPATH`, enabling Python to locate imported packages and modules:

```console
export PYTHONPATH=$(pwd)
```

### 7. Test the installation
Run the following command to verify that the course has installed successfully. Replace `<course_number>` with the appropriate course module name (e.g., `SecureCoding`):

```console
course<course_number>
```

For example, if you are taking module SecureCoding, you would run `courseSecureCoding`.

You should see something similar to the following:

```console
 * Serving Flask app 'copilot_security_workshop.cSecureCoding.src.appSecureCoding'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
127.0.0.1 - - [08/May/2024 16:48:07] "GET /101 HTTP/1.1" 200 -

```

### 8. Open the app in your browser
Navigate to the following URL in your browser:

```console
http://127.0.0.1:5000/secure_coding
```

You should see the following text displayed in the browser:

```console
Welcome to the secure coding module!
```

That's the basics, and our application installed.

### 9. After you're done with training, deactivate the virtual environment:
Deactivating the environment ensures that your terminal session returns to its default settings, preventing accidental changes to your project's isolated environment.

```console
deactivate
```

If you encounter any issues during the setup, try the following troubleshooting steps:

- If pip fails to install a package, try updating pip to its latest version.
- If Python fails to find a package, ensure that you've activated the virtual environment and that the PYTHONPATH is set correctly.

If you would like to use shortcut keys to open many of the options we just explored, the official GitHub Copilot page documents them for each operating system supported:

https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment

That's the basics, and our application installed.
