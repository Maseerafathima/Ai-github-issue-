from git import Repo

# Initialize repository
repo = Repo.init(".")
print("Git repository initialized")

# Configure user
repo.config_writer().set_value("user", "name", "gousi").release()
repo.config_writer().set_value("user", "email", "gousi@github.com").release()

# Add all files
repo.index.add([
    'app.py',
    'src/github_handler.py',
    'src/llm_analyzer.py',
    'requirements.txt',
    'README.md',
    '.env.example',
    '.gitignore'
])

# Initial commit
repo.index.commit("Initial commit: AI GitHub Issue Assistant")
print("Initial commit created")
