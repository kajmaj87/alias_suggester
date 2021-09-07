# alias_suggester
Simple python script that generates suggestions for aliases you could use based on command history.

# Usage:

You can check various parameters in help like this (but the script has sensible defaults):

``$ python3 alias_suggester.py --help``

bash:

``$ cat .bash_history | python3 alias_suggester.py``

zsh:

``$ history | awk '{ $1=""; print $0 }' | python3 alias_suggester.py``

Which will generate output similar to this (which clearly shows I'm missing git aliasies in my current setup):
``
91  git status
96  npm run netlify
104  cargo flamegraph
110  git commit -m
110  for i in $(ls
114  git clone
135  git push
154  sudo PATH="$PATH"
160  cargo build
189  git checkout
298  cargo
606  cargo run
``

Number on the left means how many keystrokes could have been saved if you instead had a 3 letter alias for the command on right (assuming you typed each of the commands in your current history by hand)

By default it will only take commands that were seen at least 3 times and had lenght of maximum of 20 characters.

# How it works

Longer commands will be split like this:

``$ git merge origin master``

will be split to 4 different commands:
git, git merge, git merge origin and git merge origin master 

Each occurence of the command will then have its character lenght counted and summed up, giving you a rough estimate of how many keystrokes you would save if you created an alias for this command instead (assuming alias lenght of 3 by default, can be changed using the -c or --alias_cost param).

Summary will then be printed with most costly commands listed at the bottom. If the commands listed there are meaningful for you then you could create aliases for them.
