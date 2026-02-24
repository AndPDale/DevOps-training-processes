# Student Guide: Git + Podman + GitHub Actions (Windows)

## What you will do
1) Pull code from GitHub (Git clone)  
2) Run the app locally (Python)  
3) Run tests (pytest)  
4) Build + run the app as a container (Podman)  
5) Make a change on a branch, push, open a Pull Request, and watch CI run

---

## Prerequisites (install once)
- Git for Windows
- Python 3.12 (or 3.11+)
- VS Code (recommended)
- Podman Desktop (recommended) OR Podman CLI set up on Windows
  - Podman Desktop usually uses a VM/WSL2 behind the scenes

> If you get stuck installing Podman Desktop, ask the instructor.

---

## Step 1: Clone the repo
Open **PowerShell** and go to a folder you use for code:
```powershell
cd $HOME
mkdir code
cd code

Clone (your instructor will give the URL):

git clone <REPO_URL>
cd vc-container-ci-demo

Check git status:
git status

Install dependencies:
pip install -r requirements.txt

Run the app:
python ./app.py

Open in your browser:
http://127.0.0.1:5000

Try:
Enter name + points + multiplier and click Calculate score

Open API:
http://127.0.0.1:5000/api/health
http://127.0.0.1:5000/api/score?points=10&multiplier=2

Stop the app with:
Ctrl + C

# ensure that you have run Ctrl + C to exit out of the app before running the next steps

setup Podman
podman machine list
podman machine start

podman build -t scoreboard-demo .

podman images

# Run in detached mode (recommended in VS Code terminal)
podman run -d --name demo -p 8080:5000 scoreboard-demo

# Check it's running
podman ps

# View logs
podman logs -f demo

# Open in browser:
# http://127.0.0.1:8080

# Stop and remove when finished
podman stop demo
podman rm demo


