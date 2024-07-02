# User onboarding 👨‍💼

This project provides a comprehensive guide for user onboarding by automating the process of validating and handling user email addresses from an Excel file.

## Installation

Clone the repository:

```bash
git clone git@github.com:ranjan/llm-user-onboarding.git
cd llm-user-onboarding
```

The project uses [Poetry](https://python-poetry.org/) for dependency management. If you don't have it installed, you can install it as follows:

For macOS / Linux / BashOnWindows:

```bash
brew install pipx
pipx ensurepath
sudo pipx ensurepath --global
pipx install poetry
```

For Linux (Ubuntu)

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
sudo pipx ensurepath
pipx install poetry
```

For Windows PowerShell:

```powershell
scoop install pipx
pipx ensurepath
pipx install poetry
```

Configure Poetry to create virtual environments within your project's directory:

```bash
poetry config virtualenvs.in-project true
```

Create a new virtual environment:

```bash
poetry shell
```

Install the necessary dependencies:

```bash
poetry install
```

Set up the environment variables (including OpenAI API key and API URLs) in a `.env` file.

## Usage

Start the application:

```bash
poetry run start
```


## License

This project is licensed under MIT License. For more information, please see the [LICENSE](https://github.com/thissayantan/gpt-pdf/blob/main/LICENSE) file.