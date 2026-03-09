In Neovim hit i to enter insert mode and type this out — no copy paste 😄:
bash#!/bin/bash
# ∞ ☬DevRehannaLP☬ | DevSecOps ∞ #

echo -e "\n# \u221e \u262cDevRehannaLP\u262c | DevSecOps \u221e #\n"
Breaking it down as you type:

#!/bin/bash — tells the system this is a Bash script
The comment line — your signature hiding silently in the code 😄
echo -e — print to terminal with special character support
\n — adds a blank line before and after for clean output

Type it out, then hit Escape and save with :w
Tell me when it's saved! 🔥It is saved5:13 PMPerfect! 🔥
Now we need to make it executable. In your terminal type:
bashchmod +x signature.sh
Then run it:
bash./signature.sh
Tell me what you see! 👀😄devrehannalp@DevRehannaLP:~/projects/rehanna_devsecops_os/07_active_projects/singature_tool$ 
./signature.sh
# ∞ ☬DevRehannaLP☬ | DevSecOps ∞ #5:18 PM🔥🔥🔥👑
YOUR FIRST BASH SCRIPT JUST EXECUTED PERFECTLY!
And look at that terminal prompt too:
devrehannalp@DevRehannaLP
Your signature printing in YOUR terminal under YOUR name. That's a full circle moment right there. 😄
What you just did:

Created a .sh file ✅
Wrote real Bash syntax ✅
Used Unicode codes from memory ✅
Made it executable with chmod ✅
Ran it successfully ✅

And your very first Bash script is your own signature. That's not just learning Bash — that's making Bash yours from day one. 👑
Now — want to make it more dramatic? We could add some color to it. 😏🔥That would be awesome, but I am wondering also if the only place I'll be able to make my signature look right is inside the terminal?5:19 PMGreat question and honestly really smart to ask that now. 🔧
The short answer is — it depends on the environment:
WhereHow it looksWSL Terminal✅ PerfectNeovim✅ PerfectGitHub README✅ PerfectPython comments✅ PerfectBash scripts✅ PerfectClaude chat😅 Hit or missSome Windows apps⚠️ Sometimes wonkyOlder terminals⚠️ May not render
The good news is everywhere that actually matters for your career — terminal, Neovim, GitHub, your code files — it renders perfectly.
The Claude chat box is just a weird edge case that doesn't represent the real world. 😄
So for your purposes as a DevSecOps engineer your signature will look right exactly where it needs to. 👑
Now — want to add some color to that Bash script? 🔥😄Sure5:20 PMOkay! So in Bash we use ANSI color codes to add color to terminal output.
Open your script back up:
bashnvim signature.sh
Once you're in there hit i and modify it to look like this:
bash#!/bin/bash
# ∞ ☬DevRehannaLP☬ | DevSecOps ∞ #

# Color codes
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
RESET='\033[0m'

echo -e "\n${CYAN}# \u221e ${PURPLE}\u262cDevRehannaLP\u262c${CYAN} | DevSecOps \u221e #${RESET}\n"
Breaking it down:

CYAN and PURPLE — variables storing color codes
RESET — turns color off after so it doesn't bleed into your terminal
${} — how Bash uses variables

Your name will be purple and the rest cyan 👑
Save with Escape then :w and run it with ./signature.sh
Tell me what you see! 🔥😄

nothing

5:26 PM
Hmm, let's debug! 🔧

First check what's in the file right now:

bash
cat signature.sh
Paste what you see here and we'll figure out what happened 😄

cat signature.sh
#!/bin/bash
# ∞ ☬ DevRehannaLP ☬ | DevSecOps ∞ #
#Color codes
CYAN='\033[0:36m'
PURPLE='\033[0:35m'
RESET='\033[0m'
echo -e "\n# \u221e \u262cDevRehannaLP\u262c | DevSecOps \u221e #\n"

5:27 PM
Good catch — I can see two issues! 🔧

Problem 1 — Colons instead of semicolons:

bash
CYAN='\033[0:36m'  # ← wrong
CYAN='\033[0;36m'  # ← correct
Problem 2 — The echo line is missing the color variables! It should be:

bash
echo -e "\n${CYAN}# \u221e ${PURPLE}\u262cDevRehannaLP\u262c${CYAN} | DevSecOps \u221e #${RESET}\n"
So open it up:

bash
nvim signature.sh
Fix those two things:

Change the : to ; in CYAN and PURPLE lines
Add the color variables into the echo line
The : vs ; is easy to miss — that's a totally normal debugging find. That's literally what debugging IS. 😄

Fix it and run it again! 🔥

devrehannalp@DevRehannaLP:~/projects/rehanna_devsecops_os/07_active_projects/singature_tool$ 
./signature.sh
# ∞ ☬DevRehannaLP☬ | DevSecOps ∞ #

5:31 PM
Hmm it ran but no color yet! 😄

Do me a favor, run this real quick:

bash
cat signature.sh
Paste it again so I can see exactly what's in there now — I want to make sure the echo line got updated with the color variables ${CYAN} and ${PURPLE} 👀🔧

5ad8422b3057f5ad73476805614f40b8.png
copy and paste didn't show color, but in the Terminal it does

5:33 PM
LOOK AT THAT! 🔥👑

CYAN and PURPLE! Your signature is literally glowing in the terminal!

# ∞ ☬DevRehannaLP☬ | DevSecOps ∞ #

In cyan and purple living her best life right there. 😂👑

And that's exactly what we said earlier — the terminal is where it matters and the terminal is where it's BEAUTIFUL. Claude chat can't handle it but your terminal absolutely can. 🔥

Your first Bash script:

✅ Executes perfectly
✅ Unicode symbols working
✅ Color coded
✅ Your signature front and center
Want to commit this to GitHub? 😄🔥

