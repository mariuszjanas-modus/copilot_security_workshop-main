# Workshop Setup Guide

This is a setup guide describing account prerequisites, IDE & Copilot installation, and local account permissions. These steps must be satisfied/completed prior to the workshop.

## 1. GitHub Account
Ensure that you have an active GitHub account prior to the workshop. 

If it is a GitHub EMU account a copy of this repository needs to be added to your GHEC+EMU organization as public repositories are not accessible for EMU users.

If you are a student you will be able to sign up for a .edu account which comes with some added bonuses, such as being able to setup private repositories for free.

## 2. A Copilot license
Ensure that you have an active GitHub Copilot license prior to the workshop. This Copilot license will be provided to you by your organization.

## 3. Visual Studio Code (as your IDE)
Ensure that you have VS Code installed prior to the workshop. 

If you do not have VS Code installed, download and install it from: https://code.visualstudio.com/download

If you already have VS Code installed, make sure it is updated to the latest version to avoid compatibility issues with Copilot and Copilot chat extensions.

In this workshop we will use VS Code, but a complete list of supported IDE's can be found [here](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment?tool=vscode).

## 4. GitHub Copilot VSCode Extensions
Open the Extensions panel in VSCode and install the GitHub Copiot and GitHub Copilot Chat extensions. 

## 5. Python 3.x installed on your machine
Ensure that you have the ability to download and install Python prior to the workshop.

Download and install it from: https://www.python.org/downloads/

You will also need Python pip and the ability to install external packages (Flask) from pypi or your local artifact store.

Specific instructions for setting up Python variables and Flask will be covered later and is documented in the OS specific setup files.

## 6. Local permissions to run Python applications
You will need to have local permissions to run Python test applications on your device so that a local website is accessible on 127.0.0.1:5000

## 8. Training Repository Setup
### 8.1 Accessing training repo via GitHub
Fork and Clone the workshop repository prior to the workshop. Detailed step by step instructions can be found in [repo_forking_and_cloning.md](./repo_forking_and_cloning.md).
### 8.2 Receiving training repo via .zip file
Unpack the ZIP file into the `copilot_workshop` directory.
Detailed step-by-step instructions can be found in [repo_setup_with_zip_file.md](./repo_setup_with_zip_file.md).

## 9. Local development environment
Set up your local development environment by following the instructions from the [windows_setup.md](./windows_setup.md) or the [mac_setup.md](./mac_setup.md) files, depending on the OS you are using. 

## 10. Basic GenAI concepts
Familiarize yourself with basic GenAI concepts prior to the workshop. Links to resources can be found in the [basic_genai_concepts.md](./basic_genai_concepts.md) file.
