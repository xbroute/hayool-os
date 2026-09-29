# Hayool OS — Zero-to-Autonomous Development Runbook
Version: 6.0
Audience: Product owner with little or no Linux/Git/Docker experience
Target development host: Ubuntu Server 24.04 LTS
Primary implementation agent: Claude Code
Independent reviewer: ChatGPT Work
System of record: GitHub private repository

---

# 0. What this guide is designed to achieve

By the end of this guide you will have:

1. A properly secured Ubuntu development/staging VPS.
2. Docker Engine + Docker Compose.
3. Git + GitHub CLI.
4. A private GitHub repository for Hayool OS.
5. The Hayool OS source-of-truth files inside that repository.
6. Persistent AI rules loaded automatically by coding agents.
7. Claude Code installed on the server and connected to the repository.
8. TypeSafe's Jev agent skill available to the engineering agent for design/research.
9. Protected `main` branch / GitHub rules so an AI cannot casually overwrite the product.
10. An M0 Architecture & Bootstrap workflow.
11. An independent Architecture Gate using ChatGPT Work.
12. A repeatable milestone loop:
    Requirements → Branch → Code → Tests → PR → Staging → Browser QA → Merge.
13. A path to later production deployment without turning the development VPS into production.

You are not expected to write application code manually.

Your role is primarily:
- own the accounts,
- approve business decisions,
- approve high-risk gates,
- visually review the product,
- supply legal/accounting confirmation where needed.

The AI engineering system should perform the technical implementation.

---


# V4 IMPORTANT CHANGE — M0 runs under Engineering Autopilot and Work/Workforce strategy is locked before architecture

The initial Linux/GitHub setup is still performed once because no trusted automation exists before the repository and credentials exist.

After that, do NOT run M0 as a simple single-agent architecture exercise.

V4 sequence:

Manual one-time bootstrap:
Ubuntu + Docker + GitHub + private repo + governance files + Claude Code/engineering model access.

Then:

M0.0 Autopilot Bootstrap
→ M0.1 Architecture generation
→ M0.2 Automated independent gate/repair
→ owner only handles unresolved high-impact decisions
→ M1.

The core pipeline must not require you to manually copy every PR into ChatGPT Work.

ChatGPT Work remains useful as:
- external audit/reviewer;
- browser UX reviewer;
- second-opinion architecture reviewer.

The core automated council should use model/provider APIs through Engineering AI Gateway so it can run unattended.

## Recommended initial autonomy

At the beginning:
- AI may create branches/commits/PRs/staging.
- AI may review and repair automatically.
- AI must not merge M0 by itself.
- AI must not deploy production.
- Autopilot runs in Shadow Mode for merge/release authority.

After metrics prove reliability, low-risk merge/release autonomy may increase.


# 1. Important vocabulary

## VPS
Your Ubuntu server on the internet.

## SSH
The secure terminal connection from your Windows PC to the Ubuntu server.

## Repository / Repo
The GitHub project containing the source code, documentation, tests and configuration.

## Git
The version-control system.

## GitHub
The remote system of record for Git, pull requests, CI, issues and releases.

## Branch
An isolated line of development. We do NOT work directly on `main`.

## Pull Request / PR
A proposed set of changes that can be reviewed and tested before merging into `main`.

## CI
Automated checks such as build, lint, tests and security scans.

## Staging
A non-production environment that behaves like the real product and is used for browser testing.

## Production
The real customer-facing environment. Production is NOT your current development VPS.

## Source of Truth
The versioned repository documentation that defines what Hayool OS is supposed to do.

---

# 2. Values you will replace in commands

Throughout this guide, replace these placeholders with your own values:

```text
YOUR_SERVER_IP      Example: 203.0.113.20
YOUR_GITHUB_USER    Example: erfan
YOUR_GITHUB_ORG     Example: hayool-labs
YOUR_EMAIL          Your Git/GitHub email
```

Recommended repository name:

```text
hayool-os
```

Recommended Linux user:

```text
hayooldev
```

Recommended local project path on the VPS:

```text
/home/hayooldev/projects/hayool-os
```

Do NOT literally paste `YOUR_SERVER_IP`. Replace it first.

---

# 3. Before touching the VPS

## How to use the command blocks in this guide

- Lines inside a `bash` block are run on the Ubuntu VPS.
- Lines inside a `powershell` block are run on your Windows PC.
- Do not copy the word `bash` or `powershell`; copy only the commands.
- Run one section at a time and verify its expected result before moving on.
- If a command fails, stop at that section. Do not continue hoping the next command will fix it.
- Commands beginning with `sudo` may ask for the `hayooldev` Linux password.
- When a command contains a placeholder such as `YOUR_SERVER_IP`, replace the placeholder first.


Keep the following available:

- VPS IPv4 address.
- Root password OR provider SSH key access.
- GitHub account.
- Access to your domain DNS if you later want a staging domain.
- The `hayool-os-bootstrap-v6.zip` file supplied with this specification.

Do not buy or configure the final production server yet.

Development/staging and production must remain separate.

---

# 4. Open a terminal on Windows

On Windows 10/11:

1. Press Start.
2. Search for `PowerShell` or `Windows Terminal`.
3. Open it.

Check whether SSH exists:

```powershell
ssh -V
```

If you see an OpenSSH version, you are ready.

If Windows says the command is unknown:
- Settings → Apps → Optional Features
- Add a feature
- install **OpenSSH Client**

Then reopen PowerShell.

---

# 5. First login to Ubuntu

If your provider gave you root access:

```powershell
ssh root@YOUR_SERVER_IP
```

The first time, you may see:

```text
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Type:

```text
yes
```

Then enter the server password if requested.

Important:
When Linux asks for a password, the cursor usually does not move. That is normal.

After login, confirm Ubuntu:

```bash
cat /etc/os-release
```

You should see Ubuntu 24.04 / Noble or equivalent.

Check time:

```bash
date
timedatectl
```

For servers, UTC is recommended:

```bash
timedatectl set-timezone UTC
```

The Hayool application will localize time for users; the server itself is easier to operate in UTC.

---

# 6. Update Ubuntu

Run:

```bash
apt update
apt upgrade -y
```

Install basic tools:

```bash
apt install -y \
  ca-certificates \
  curl \
  wget \
  gnupg \
  git \
  jq \
  unzip \
  zip \
  ufw \
  fail2ban \
  tmux \
  htop \
  ripgrep \
  tree \
  nano
```

Verify Git:

```bash
git --version
```

---

# 7. Create a normal non-root user

Do not use `root` as the daily development user.

Create:

```bash
adduser hayooldev
```

Ubuntu will ask for a password and some optional details.

Add sudo rights:

```bash
usermod -aG sudo hayooldev
```

Confirm:

```bash
id hayooldev
```

You should see the `sudo` group.

---

# 8. Give the new user SSH key access

## Case A — you already logged into root using an SSH key

Check:

```bash
ls -la /root/.ssh
```

If `/root/.ssh/authorized_keys` exists, copy it:

```bash
mkdir -p /home/hayooldev/.ssh
cp /root/.ssh/authorized_keys /home/hayooldev/.ssh/authorized_keys
chown -R hayooldev:hayooldev /home/hayooldev/.ssh
chmod 700 /home/hayooldev/.ssh
chmod 600 /home/hayooldev/.ssh/authorized_keys
```

## Case B — you only have a root password

On your Windows PowerShell, in a NEW terminal window, create an SSH key:

```powershell
ssh-keygen -t ed25519 -C "hayool-development"
```

When asked where to save it, pressing Enter accepts the default.

A passphrase is recommended.

Display your public key:

```powershell
Get-Content "$env:USERPROFILE\.ssh\id_ed25519.pub"
```

Copy the entire single line beginning with `ssh-ed25519`.

Back in the root Ubuntu terminal:

```bash
mkdir -p /home/hayooldev/.ssh
nano /home/hayooldev/.ssh/authorized_keys
```

Paste the public key as one line.

In nano:
- `Ctrl + O`
- Enter
- `Ctrl + X`

Then:

```bash
chown -R hayooldev:hayooldev /home/hayooldev/.ssh
chmod 700 /home/hayooldev/.ssh
chmod 600 /home/hayooldev/.ssh/authorized_keys
```

---

# 9. TEST the new login before hardening SSH

THIS STEP IS IMPORTANT.

Do not close the working root terminal.

Open another PowerShell window and test:

```powershell
ssh hayooldev@YOUR_SERVER_IP
```

Then test sudo:

```bash
sudo whoami
```

Expected:

```text
root
```

Only continue if this works.

If it fails, fix SSH access before disabling anything.

---

# 10. Basic SSH hardening

While logged in as `hayooldev`, create a dedicated config drop-in:

```bash
sudo nano /etc/ssh/sshd_config.d/99-hayool-hardening.conf
```

Enter:

```text
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
KbdInteractiveAuthentication no
```

Save.

Validate SSH configuration BEFORE reloading:

```bash
sudo sshd -t
```

If this returns no error:

```bash
sudo systemctl reload ssh
```

Open another PowerShell window and verify again:

```powershell
ssh hayooldev@YOUR_SERVER_IP
```

Do not continue if you cannot reconnect.

---

# 11. Enable firewall

Allow SSH first:

```bash
sudo ufw allow OpenSSH
```

For later web/staging access:

```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

Default policy:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

Enable:

```bash
sudo ufw enable
```

Check:

```bash
sudo ufw status verbose
```

Important:
Docker has networking interactions with host firewalls. We will not casually publish database/cache ports to the internet. Application containers should expose only what the architecture explicitly requires.

---

# 12. Check Fail2ban

```bash
sudo systemctl enable --now fail2ban
sudo systemctl status fail2ban --no-pager
```

It is acceptable if the default jail configuration is minimal at this point. M0 security architecture may refine it.

---

# 13. Install Docker Engine — official Ubuntu repository

Do NOT install a random Docker package from a third-party tutorial.

First remove potentially conflicting packages if installed:

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do
  sudo apt-get remove -y "$pkg" 2>/dev/null || true
done
```

Add Docker's official signing key:

```bash
sudo apt update
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Add the official repository:

```bash
sudo tee /etc/apt/sources.list.d/docker.sources > /dev/null <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF
```

Update and install:

```bash
sudo apt update
sudo apt install -y \
  docker-ce \
  docker-ce-cli \
  containerd.io \
  docker-buildx-plugin \
  docker-compose-plugin
```

Verify service:

```bash
sudo systemctl status docker --no-pager
```

Run Docker's test container:

```bash
sudo docker run --rm hello-world
```

Check versions:

```bash
sudo docker version
sudo docker compose version
```

---

# 14. Optional Docker access without sudo

Docker's `docker` group is effectively a powerful/root-equivalent capability. Only add trusted development users.

For your dedicated dev account:

```bash
sudo usermod -aG docker "$USER"
```

Log out:

```bash
exit
```

Connect again from Windows:

```powershell
ssh hayooldev@YOUR_SERVER_IP
```

Test without sudo:

```bash
docker ps
docker compose version
```

---

# 15. Install GitHub CLI (`gh`)

Use GitHub's official apt repository.

Run:

```bash
(type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
  && sudo mkdir -p -m 755 /etc/apt/keyrings \
  && out=$(mktemp) \
  && wget -nv -O"$out" https://cli.github.com/packages/githubcli-archive-keyring.gpg \
  && cat "$out" | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
  && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
  && sudo mkdir -p -m 755 /etc/apt/sources.list.d \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
     | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
  && sudo apt update \
  && sudo apt install gh -y
```

Verify:

```bash
gh --version
```

---

# 16. Configure your Git identity

This controls author information for commits created from this server.

```bash
git config --global user.name "YOUR NAME"
git config --global user.email "YOUR_EMAIL"
```

Example:

```bash
git config --global user.name "Erfan"
git config --global user.email "your-github-email@example.com"
```

Check:

```bash
git config --global --list
```

---

# 17. Create the GitHub organization and repository

You can do this in the browser, which is easiest the first time.

## 17.1 Create organization

On GitHub:

1. Sign in.
2. Click your profile photo.
3. Choose **Your organizations**.
4. Create a new organization.
5. A suitable name might be:
   - `hayool-labs`
   - `hayool-dev`
   - another available Hayool-owned name.

The exact organization name is not technically important.

## 17.2 Create private repository

Inside the organization:

1. Click **New repository**.
2. Repository name:
   `hayool-os`
3. Visibility:
   **Private**
4. Initialize with a README if offered.
5. Create repository.

Do not make the source repository public.

---

# 18. Authenticate GitHub CLI on the VPS

On Ubuntu:

```bash
gh auth login
```

Choose:

```text
GitHub.com
HTTPS
Login with a web browser
```

GitHub CLI will display a one-time code and URL.

Open the URL on your own PC browser, enter the code and approve.

Then:

```bash
gh auth status
gh auth setup-git
```

`gh auth setup-git` configures Git to use GitHub CLI authentication.

---

# 19. Clone the repository onto the VPS

Create a projects directory:

```bash
mkdir -p ~/projects
cd ~/projects
```

Clone:

```bash
gh repo clone YOUR_GITHUB_ORG/hayool-os
```

Enter it:

```bash
cd ~/projects/hayool-os
```

Confirm:

```bash
git status
git remote -v
pwd
```

You should be inside:

```text
/home/hayooldev/projects/hayool-os
```

---

# 20. Download the Hayool bootstrap bundle on Windows

From this ChatGPT conversation download:

```text
hayool-os-bootstrap-v6.zip
```

Assume Windows saves it to:

```text
Downloads
```

Do NOT unzip and manually copy dozens of individual files unless you want to.

---

# 21. Copy the ZIP from Windows to your VPS

From Windows PowerShell:

```powershell
scp "$env:USERPROFILE\Downloads\hayool-os-bootstrap-v6.zip" `
  hayooldev@YOUR_SERVER_IP:/home/hayooldev/
```

If your Downloads folder is elsewhere, adjust the path.

After upload, on Ubuntu:

```bash
ls -lh ~/hayool-os-bootstrap-v6.zip
```

---

# 22. Extract the bootstrap files into the repository

On Ubuntu:

```bash
rm -rf /tmp/hayool-bootstrap
mkdir -p /tmp/hayool-bootstrap
unzip ~/hayool-os-bootstrap-v6.zip -d /tmp/hayool-bootstrap
```

Inspect:

```bash
tree -a /tmp/hayool-bootstrap | head -100
```

Copy into your repo:

```bash
cp -a /tmp/hayool-bootstrap/. ~/projects/hayool-os/
```

Now:

```bash
cd ~/projects/hayool-os
tree -a -L 4
```

Important files should include:

```text
CLAUDE.md
AGENTS.md
docs/
  product/
    HAYOOL_OS_MASTER_PRODUCT_ENGINEERING_SPEC.md
    HAYOOL_OS_START_HERE_RUNBOOK.md
  engineering/
    AI_ENGINEERING_CONSTITUTION.md
  ai/
    JEV_DECISION_ENGINE_SPEC.md
.github/
  PULL_REQUEST_TEMPLATE.md
```

The engineering agent will create the remaining Source-of-Truth files during M0.

---

# 23. Understand the persistent rule system

The rules are deliberately layered.

## Layer 1 — `CLAUDE.md`

Claude Code automatically receives repository project instructions. It tells Claude which authoritative files to read and contains the short non-negotiable rules.

## Layer 2 — `AGENTS.md`

Coding agents such as Codex that support repository agent instructions use this file.

## Layer 3 — AI Engineering Constitution

Full binding policy:

```text
docs/engineering/AI_ENGINEERING_CONSTITUTION.md
```

This includes:
- no direct production mutation,
- no weakening tests,
- source-of-truth requirements,
- deterministic finance/payroll/permissions,
- secrets,
- tenant isolation,
- AI autonomy,
- Jev rules,
- fairness,
- UI/UX gates,
- completion honesty.

## Layer 4 — scoped agent rules

During M0, Claude will create path-specific rules for high-risk areas after the final directory structure is confirmed.

Examples:
- Finance
- Security
- Tests
- Jev / Decision Intelligence
- UI/UX

## Layer 5 — mechanical GitHub/CI enforcement

This is what prevents an instruction from being “just text.”

Examples:
- protected `main`
- required PR
- required tests
- required security checks
- CODEOWNERS
- deployment approval
- no direct production credentials

If an AI ignores a prose rule, mechanical controls should still prevent dangerous merge/deploy actions.

---

# 24. Put the bootstrap docs into Git through a PR

Do NOT immediately commit to `main`.

Create a branch:

```bash
cd ~/projects/hayool-os
git switch -c bootstrap/spec-v4
```

Check what changed:

```bash
git status
```

Stage:

```bash
git add .
```

Inspect:

```bash
git diff --cached --stat
```

You can also inspect the actual diff:

```bash
git diff --cached
```

Commit:

```bash
git commit -m "docs: bootstrap Hayool OS source of truth"
```

Push:

```bash
git push -u origin bootstrap/spec-v4
```

Create PR:

```bash
gh pr create \
  --base main \
  --head bootstrap/spec-v4 \
  --title "Bootstrap Hayool OS source of truth" \
  --body "Adds the V2 master specification, AI engineering constitution, Jev decision-engine specification, persistent agent instructions, beginner runbook and PR quality checklist."
```

GitHub CLI returns a PR URL.

Open the URL in your browser.

Review the files.

Merge the PR manually for this first bootstrap.

Then on the VPS:

```bash
git switch main
git pull --ff-only
```

---

# 25. Protect the `main` branch

Do this after the initial docs are on `main`.

In GitHub:

1. Open the repository.
2. **Settings**.
3. Find **Rules** → **Rulesets** (or Branch protection, depending on your account UI).
4. Create a branch ruleset targeting `main`.

Initially enable at least:

- Require a pull request before merging.
- Require conversation resolution before merging.
- Block force pushes.
- Block branch deletion.
- Do not allow bypassing rules where practical.

At this stage do NOT require a CI check name that does not yet exist.

After M0 creates CI and it has successfully run at least once, return here and require its checks.

Recommended later checks include:

```text
lint
typecheck
unit-tests
integration-tests
migration-check
tenant-isolation
security-scan
build
e2e-smoke
```

Actual names should come from the final CI workflow.

---

# 26. Install Claude Code

Current recommended native installation for Linux:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

If the command says the binary path is not in `PATH`, restart your shell:

```bash
exec "$SHELL" -l
```

Verify:

```bash
claude --version
claude doctor
```

If `claude doctor` reports a problem, fix it before giving autonomous tasks.

Start Claude Code from INSIDE the repository:

```bash
cd ~/projects/hayool-os
claude
```

Authenticate using the official flow shown by Claude Code.

Important:
You already have a curated `CLAUDE.md`. Do not blindly run `/init` and overwrite it.

---

# 27. Install TypeSafe's Jev agent skill for Claude Code

This skill is for helping the engineering agent use Jev correctly. It does NOT automatically add Jev to production.

Run these commands in the Ubuntu terminal from the project directory:

```bash
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

Then start/restart Claude Code:

```bash
cd ~/projects/hayool-os
claude
```

Inside Claude Code you can explicitly invoke the installed skill with:

```text
/typesafe:typesafe-ai
```

If it does not appear immediately, restart Claude Code or reload plugins according to the current Claude Code UI.

Alternative, if you later use another agent ecosystem that supports Agent Skills:

```bash
npx skills add typesafe-ai/skills --skill typesafe-ai
```

The engineering agent must still obey Hayool's Decision Intelligence abstraction and evaluation policy. Vendor skill guidance cannot override the repository constitution.

Do not create a production TypeSafe API key yet unless M0 specifically needs a private evaluation. Architecture work can be completed first.

---

# 28. Optional — TypeSafe API key later

When M0 reaches Jev private evaluation:

1. Create a TypeSafe account/key according to their console.
2. Never paste the key into GitHub, a markdown file, issue, screenshot or AI prompt.
3. Store it only using the project's secret mechanism.

Before OpenBao is deployed, a temporary dev-only environment secret can be used if the engineering agent explicitly sets it up safely.

Example principle:

```text
TYPESAFE_API_KEY=...
```

must appear in `.env`/secret storage excluded from Git.

Never commit `.env`.

The production architecture should use secret references / vault integration.

---

# 29. Connect Claude Code to GitHub Actions

Inside Claude Code in the repository, run the current official GitHub app installation command if supported by the installed version:

```text
/install-github-app
```

Follow the authorization flow.

Grant only the repository/organization access required.

Claude may create a setup PR/workflow.

Do not automatically trust and merge it.

Review:
- permissions requested,
- secrets used,
- workflow triggers,
- branch write behavior.

Merge only when it matches the constitution.

This integration can later let Claude respond to bounded GitHub issue/PR events.

---

# 30. Create the M0 architecture branch

Exit any accidental editing state and make sure main is clean:

```bash
git switch main
git pull --ff-only
git status
```

Expected:

```text
working tree clean
```

Create:

```bash
git switch -c m0/autopilot-architecture
```

Now launch Claude:

```bash
claude
```

---

# 31. FIRST real M0 run — under Autopilot

After bootstrap files are merged to `main`:

```bash
cd ~/projects/hayool-os
git switch main
git pull --ff-only
git switch -c m0/autopilot-architecture
claude
```

Do NOT paste an older M0 prompt from chat history.

Open the repository file:

```text
docs/prompts/M0_ARCHITECTURE_BOOTSTRAP_PROMPT.md
```

Paste its prompt into Claude Code.

The V4 M0 has three phases:

```text
M0.0 Trust/Autopilot Bootstrap
→ M0.1 Architecture generation
→ M0.2 Autonomous Architecture Gate
```

The first objective is NOT to build CRM/Finance/UI.

The first objective is to establish the smallest trustworthy autonomous development loop, then use that loop to review M0 itself.

---

# 32. What M0.0 should establish

M0.0 should create the minimum viable Engineering Autopilot.

Expected capabilities:

- GitHub event integration
- one scoped writer
- independent read-only review roles
- Engineering AI Gateway abstraction
- provider/model identity audit
- run ID/evidence record
- deterministic baseline checks
- bounded auto-repair
- cost/time/iteration limits
- kill switch
- Shadow Mode for merge/release authority
- no production credential access

Do not build a huge internal platform just to bootstrap the project.

Prefer the simplest GitHub Actions/scripts/workflow implementation that satisfies the controls, then evolve it later.

---

# 33. M0 Architecture generation

Once M0.0 controls exist, the writer agent proceeds with M0.1.

It creates the Source of Truth, including:

- PRD/REQ/ADR
- domain boundaries
- Work Graph
- ERD
- tenancy/permissions
- Finance/Iran localization
- Pricing/Compensation
- Trust & Safety
- AI/Jev
- Learning Intelligence
- Workforce Architect
- Employment AI governance
- UI/UX design system
- deployment/installer
- unit economics
- GTM/productization
- testing/observability/DR

It opens or updates the M0 PR.

---

# 34. Autonomous M0 Architecture Gate

The PRIMARY gate is automated.

When the M0 PR is marked ready:

```text
Freeze SHA
→ deterministic checks
→ independent review council
→ normalized findings
→ Jev narrow semantic evidence where useful
→ deterministic Gate Engine
```

If valid blockers exist and repair policy permits:

```text
Repair Agent
→ fixes
→ tests
→ new commit/SHA
→ complete affected gate runs again
```

The repair loop has explicit maximum:
- attempts
- elapsed time
- cost

If the loop cannot converge, it escalates to you with a concise decision report.

You should NOT manually copy every review between ChatGPT and Claude.

---

# 35. Optional external ChatGPT Work audit

ChatGPT Work remains valuable, but it is no longer a required manual bottleneck.

Use it for:
- periodic independent architecture audits
- contentious PRs
- browser/UX staging reviews
- external second opinion
- market/research validation.

If you connect GitHub to ChatGPT, grant only required repository access.

For an optional M0 audit use:

```text
docs/prompts/M0_INDEPENDENT_ARCHITECTURE_GATE_PROMPT.md
```

A Work review never overrides a deterministic blocker or the Engineering Constitution.

The core pipeline must be capable of progressing without you manually launching Work for each PR.

---

# 36. Merge M0 only after the gate passes

When:
- CI passes,
- no blocker remains,
- architecture review is acceptable,
- there is no secret,
- docs and ADRs are coherent,

merge the M0 PR through GitHub.

Then VPS:

```bash
git switch main
git pull --ff-only
```

---

# 37. Turn on required CI checks

Now that CI has run and check names exist:

GitHub → Settings → Rules / Rulesets → your `main` rule.

Enable:

- Require status checks to pass before merging.
- Select the real CI jobs.
- Require PR before merging.
- Require conversation resolution.
- Prevent force pushes.
- Prevent deletion.
- Optional: require code-owner review for high-risk paths once CODEOWNERS exists.

Do not use fake check names.

---

# 38. How every later milestone works

Never say:

```text
Build the rest of Hayool OS.
```

Use one milestone at a time.

Example:

```bash
git switch main
git pull --ff-only
git switch -c m1/platform-foundations
claude
```

Then use:

```text
Recover current project state from the repository first.

Implement M1 only.

Before coding:
1. Read the Engineering Constitution.
2. Read the Master Specification.
3. Read PROJECT_STATE.md and NEXT_ACTIONS.md.
4. Read M1 requirements and ADRs.
5. Inspect current code and tests.
6. Restate M1 acceptance criteria.
7. Identify data/tenant/security/permission risks.
8. Identify migrations.
9. Define tests required.

Then implement M1 in small reviewable slices.

For every material behavior:
- keep REQ traceability,
- update ADR if architecture changes,
- implement validation/permissions/audit,
- add tests,
- run tests,
- update docs.

Do not weaken existing tests.
Do not start M2.
Do not touch production.

At the end:
- run clean database migration/bootstrap,
- run full relevant CI locally where possible,
- run tenant-isolation/permission tests,
- run browser E2E for critical M1 flows,
- deploy/update staging if CI passes,
- produce M1_COMPLETION_REPORT.md,
- update PROJECT_STATE.md and NEXT_ACTIONS.md,
- open/update the M1 PR,
- do not merge it yourself.
```

Repeat for M2, M3 ... M14.

---

# 39. Staging setup

Initially the same VPS can host development tooling and a staging stack if resources are sufficient, but data/secrets must be isolated.

Recommended conceptual separation:

```text
~/projects/hayool-os          source checkout
/opt/hayool/staging           staging deployment state
```

Staging should have its own:

- database
- Valkey namespace/instance
- object-storage bucket
- environment file/secret references
- AI keys/budgets
- email sandbox
- payment sandbox/test credentials

Do not use real customer production data.

M0 architecture should decide exact deployment layout and reverse proxy.

Do not manually improvise Caddy/Nginx/Traefik before M0 decides the supported installer/deployment stack.

---

# 40. DNS for staging

After M0 gives you the exact reverse-proxy plan, create a DNS record such as:

```text
staging-os.hayool.ir
```

Point an `A` record to the VPS IPv4.

Example:

```text
Type: A
Name: staging-os
Value: YOUR_SERVER_IP
```

Then let the supported deployment configuration obtain TLS.

Do not publish raw PostgreSQL/Valkey/Temporal administration ports to the internet.

---

# 41. Browser QA with ChatGPT Work

After each major milestone is on staging, ask Work to inspect it.

Example:

```text
Use the cloud browser to perform an independent UX/functional QA pass on the Hayool OS staging environment.

Read the current milestone requirements and acceptance criteria from GitHub first.

Test both Persian RTL and English LTR where available.

Check:
- navigation clarity
- role permissions
- forms
- validation
- empty states
- errors
- loading behavior
- responsive behavior
- accessibility basics
- keyboard interactions
- table/filter/search UX
- unauthorized-state behavior
- visual consistency with design system
- critical end-to-end milestone flows

Do not make production changes.

Return reproducible findings with:
- severity
- exact steps
- expected
- actual
- screenshot/context where useful
- suggested fix

Distinguish functional defect from UX recommendation.
```

Give the findings to Claude to fix inside the same PR.

---

# 42. Jev implementation lifecycle

Jev does NOT go straight from idea to production automation.

Before a hosted Jev policy reaches production, confirm the current TypeSafe commercial/data-processing terms for the intended use. Hayool AI Credits must represent Hayool platform usage, not raw resale of Jev access.

Every decision policy follows:

```text
Draft
→ Offline Evaluation
→ Shadow Mode
→ Human Review
→ Limited Rollout
→ Active
→ Monitoring
→ Recalibration / Retire
```

Required versioning:

- decision key
- question/criteria
- state builder
- provider
- pinned model
- threshold
- deterministic composition weights
- autonomy policy
- evaluation dataset version

Never tune a threshold because “0.8 sounds safe.”

Measure it on Hayool's own labeled data.

Persian decisions require a Persian evaluation slice.

---

# 43. Where Jev SHOULD be used

Good candidate areas:

- support ticket intent/category/severity
- RAG passage relevance
- contradiction signal
- suspicious/instruction-like retrieved text
- lead semantic fit dimensions
- project-intake ambiguity/complexity dimensions
- task semantic complexity
- project risk signals
- skill evidence classification
- resume evidence dimensions
- talent fit components
- interview answer rubric dimensions
- meeting-output verification
- document extraction verification
- AI model/task routing
- tool-call risk classification
- PR/code-change risk classification

Use typed narrow decisions.

Combine results in deterministic code.

---

# 44. Where Jev MUST NOT be the authority

Do NOT use Jev to authoritatively:

- add/subtract money
- calculate VAT
- calculate payroll
- calculate commission
- count billable hours
- compare dates
- produce ledger postings
- enforce permissions
- move money
- validate legal identity
- decide a final high-impact employment action with no human policy
- generate customer prose/code/contracts
- store/retrieve secrets

These remain deterministic or use another appropriate LLM/tool with governance.

---

# 45. Context recovery when an AI session becomes long

Start a fresh session.

Run Claude in repo:

```bash
cd ~/projects/hayool-os
claude
```

Prompt:

```text
Recover project state entirely from the repository.

Read:
- CLAUDE.md
- Engineering Constitution
- Master Specification
- PROJECT_STATE.md
- NEXT_ACTIONS.md
- current milestone
- related requirements/ADRs
- recent git log
- current branch/status
- open PR context if available

Run the repository's basic health/test command before editing.

Then tell me:
1. current milestone
2. completed items
3. incomplete items
4. blockers
5. next highest-priority safe action

Do not rely on memory from a previous chat when repository state differs.
Then continue the approved work.
```

This is why repository documentation is more important than a huge chat history.

---

# 46. How to request a new feature later

Bad:

```text
Add AI invoices.
```

Good:

```text
Create or update the requirement first.

Goal:
...

Actors:
...

Desired user outcome:
...

Business rules:
...

Who may access it:
...

What AI may/may not automate:
...

Financial/security implications:
...

Acceptance criteria:
...

Now analyze impact on the existing architecture.
Update Source of Truth first.
Implement through a branch/PR.
Add tests and staging browser evidence.
Do not merge until required checks pass.
```

---

# 47. How AI should use open-source projects

You explicitly allow the development agent to research GitHub/open-source to accelerate development.

That permission does NOT mean “copy anything useful.”

For every meaningful dependency/project, the agent must review:

- license
- commercial use compatibility
- maintenance
- releases
- known vulnerabilities
- transitive dependencies
- architecture fit
- replaceability
- performance
- upgrade cost
- community maturity

Prefer a maintained library dependency over copying source.

Record license/SBOM information.

Do not let a convenient open-source project redefine Hayool's architecture.

---

# 48. Production is a separate phase

Do not convert your current VPS into production merely because the product starts looking good.

Before production, require at minimum:

- separate production environment
- production database
- production secret vault
- backup
- off-host backup
- successful restore test
- monitoring/alerts
- TLS
- domain
- admin MFA
- payment production credentials
- AI production budgets
- rate limits
- security review
- dependency scan
- tenant-isolation tests
- performance/load test
- incident runbook
- rollback path
- production approval gate

Only then deploy a release candidate.

---

# 49. The three customer deployment modes

## 49.1 Hayool Cloud

Customer buys subscription.

Platform provisions a tenant in Hayool-managed SaaS.

Shared infrastructure is allowed only with strong tenant isolation.

## 49.2 Dedicated Cloud

Customer buys dedicated deployment.

Automation provisions an isolated application stack.

Hayool manages:
- upgrade
- backup
- monitoring
- TLS
- operations

## 49.3 On-Premise

Customer runs on their own Ubuntu/infrastructure.

They receive:
- licensed deployment bundle
- installer
- preflight checks
- setup wizard
- backup/update documentation
- entitlement/license activation

If Shared Talent Network is enabled, use a controlled connector. Never expose the customer's internal database directly.

---

# 50. What you personally should NOT have to do

Once the system is operating correctly, you should not routinely need to:

- write TypeScript
- create migrations
- debug stack traces
- manually edit CI YAML
- manually deploy each container
- manually generate tests
- manually review thousands of code lines

If the coding agent has the safe tools/permissions to do a technical operation itself, ask it to do the work and report evidence.

Your role is product owner and high-risk approver, not unpaid sysadmin.

---

# 51. Commands you will use often

Go to repo:

```bash
cd ~/projects/hayool-os
```

Current branch/status:

```bash
git status
git branch --show-current
```

Update main:

```bash
git switch main
git pull --ff-only
```

List PRs:

```bash
gh pr list
```

See a PR:

```bash
gh pr view <NUMBER>
```

Check CI:

```bash
gh pr checks <NUMBER>
```

See recent commits:

```bash
git log --oneline --decorate -20
```

Start Claude:

```bash
claude
```

Docker status:

```bash
docker ps
docker compose version
```

Disk:

```bash
df -h
```

Memory:

```bash
free -h
```

Processes:

```bash
htop
```

---

# 52. What to do if a command fails

Do NOT blindly paste random internet fixes.

Copy:

1. the exact command,
2. the full error,
3. output of:

```bash
cat /etc/os-release
pwd
whoami
git status 2>/dev/null || true
docker version 2>/dev/null || true
gh auth status 2>/dev/null || true
claude --version 2>/dev/null || true
```

Give that to your engineering assistant.

Ask:

```text
Diagnose this failure without making unrelated system changes.
Explain the cause first.
Propose the smallest safe fix.
Do not disable security controls or delete project data.
```

---

# 53. Stop conditions

Stop autonomous execution and request approval when:

- an action can destroy production/customer data,
- money will move,
- production tax/payroll rules change,
- a migration is irreversible/high-risk,
- an AI gets broader production permissions,
- a new external processor receives sensitive customer data,
- secrets/keys may have leaked,
- a license may prevent commercial use,
- a business/legal rule cannot safely be inferred,
- deployment architecture changes materially,
- cross-tenant isolation is uncertain.

Everything else should be designed to proceed autonomously through documented reversible engineering decisions.

---

# 54. Immediate checklist

Complete these in order:

- [ ] VPS Ubuntu 24.04 login works
- [ ] system updated
- [ ] `hayooldev` created
- [ ] SSH key login for `hayooldev` tested
- [ ] root/password SSH disabled only after key test
- [ ] UFW enabled
- [ ] Docker installed and `hello-world` works
- [ ] GitHub CLI installed
- [ ] GitHub org/repo created
- [ ] `gh auth status` works
- [ ] repo cloned
- [ ] bootstrap ZIP copied/extracted
- [ ] bootstrap PR merged
- [ ] `main` protection/ruleset enabled
- [ ] Claude Code installed
- [ ] `claude doctor` healthy
- [ ] TypeSafe skill installed
- [ ] Claude GitHub integration reviewed
- [ ] M0 branch created
- [ ] M0 prompt started
- [ ] M0 PR produced
- [ ] ChatGPT Work Architecture Gate completed
- [ ] M0 blockers fixed
- [ ] M0 merged
- [ ] real CI checks made mandatory
- [ ] start M1 only after M0 gate

Do not skip from “VPS is ready” straight to “build the entire application.”

The architecture gate is what makes the later autonomous work controllable.


# 55. V4 Autopilot operating loop

After the one-time bootstrap and M0.0 setup, normal work is event-driven:

GitHub requirement/issue
→ risk classify
→ implementation branch
→ writer agent
→ local/tests
→ PR
→ deterministic CI
→ independent model council
→ Jev semantic evidence where appropriate
→ deterministic gate
→ bounded auto-repair
→ staging
→ Playwright
→ AI UX review
→ merge policy
→ milestone acceptance.

You should not manually shuttle every review between tools.

# 56. ChatGPT Work in V4

Work is no longer a mandatory bottleneck.

Use Work for:
- periodic external architecture audits;
- staging browser QA;
- contentious PR second opinion;
- product/research tasks.

Core unattended reviews use Engineering AI Gateway + provider APIs.

# 57. 9Router / compatible gateway

If you use 9Router for Claude Code or review agents:

- treat it as an engineering-only gateway;
- do not hard-code it into Hayool business domains;
- preserve real provider/model identity in audit;
- store router credentials as secrets;
- configure spend limits;
- review data-handling/security before private code is sent;
- keep a fallback path to direct providers or another gateway.

A compatibility alias may be used technically, but authoritative logs must identify the real effective model.

# 58. First M0 command

After bootstrap files are on `main`:

```bash
cd ~/projects/hayool-os
git switch main
git pull --ff-only
git switch -c m0/autopilot-architecture
claude
```

Then open and paste:

```text
docs/prompts/M0_ARCHITECTURE_BOOTSTRAP_PROMPT.md
```

M0 first builds the minimal safe Autopilot before architecture generation.

# 59. V4 owner intervention rule

The system should interrupt you only when:

- legal/commercial engagement-mode decision is unresolved;
- employment/payment/tax compliance needs human confirmation;
- critical reviewers disagree after bounded escalation;
- Autopilot exceeds cost/repair limits;
- high-risk production action needs approval;
- governance/security change needs owner review.

Routine lint/test/review/fix/staging work should not require you.


# 60. V4 strategic documents

Before M0.1 architecture generation, the primary agent must also read:

```text
docs/product/HAYOOL_OS_EXECUTIVE_STRATEGIC_REVIEW_FA.md
docs/product/HAYOOL_OS_COMPREHENSIVE_BUSINESS_PLAN_FA.md
docs/product/OWNER_DECISION_SHEET.md
docs/data/WORK_GRAPH_AND_CAPABILITY_ONTOLOGY_SPEC.md
docs/product/TRUST_SAFETY_AND_MARKETPLACE_INTEGRITY_SPEC.md
docs/product/GO_TO_MARKET_BRAND_MONETIZATION_SPEC.md
docs/product/UNIT_ECONOMICS_FINANCIAL_MODEL_SPEC.md
docs/product/STRATEGIC_RISK_REGISTER.md
docs/product/RELEASE_TRAIN_MARKET_READINESS_GATES.md
docs/market/MARKET_REGULATORY_RESEARCH_REFERENCES.md
```

The market reference file is evidence/context only. Current sources must be re-checked before external claims.

M0 must not silently broaden the launch ICP merely because the code architecture supports more industries.

# 61. V4 owner-review order

Before launching M0, the product owner should read:

1. `HAYOOL_OS_EXECUTIVE_STRATEGIC_REVIEW_FA.md`
2. `HAYOOL_OS_COMPREHENSIVE_BUSINESS_PLAN_FA.md`
3. `OWNER_DECISION_SHEET.md`

If the proposed defaults are acceptable, M0 may treat them as working product decisions.

If the owner disagrees with a proposed default, update the Decision Sheet before architecture generation.


# V6 UNIVERSAL PLATFORM NOTE

M0 must not attempt to code every industry.

Its job is to prove the Universal Kernel, Studio, Pack model, Intent-to-Outcome architecture and industry boundaries.

Only after those foundations pass Architecture Gate should domain packs be implemented incrementally.

A generic object system that cannot preserve finance/security/inventory invariants is not an acceptable shortcut.


# V6 ECOSYSTEM NOTE

M0 now treats the Developer Platform as a first-class deliverable.

Do not wait until late product development to decide how extensions work.

Before building many industry-specific modules, Architecture Gate must approve:

- clean-core boundaries
- Studio/custom objects
- app manifest/scopes
- public API/events
- SDK/CLI/docs
- private extension lifecycle
- marketplace security model
- AI cost/pricing governance.

The first proof of extensibility should be small:
a simple industry/custom app built without modifying Core.

