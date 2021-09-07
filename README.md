# alias_suggester
Simple python script that generates suggestions for aliases you could use based on command history.

# Usage:

bash:

``$ cat .bash_history | python3 alias_suggester.py``

zsh:

``$ history | awk '{ $1=""; print $0 }' | python3 alias_suggester.py``

By default it will only take commands that were seen at least 3 times and had lenght of maximum of 20 characters.

Longer commands will be split like this:

``$ git merge origin master``

will be split to 4 different commands:
git, git merge, git merge origin and git merge origin master 

Each occurence of the command will then have its character lenght counted and summed up, giving you a rough estimate of how many keystrokes you would save if you created an alias for this command instead (assuming alias lenght of 3 by default, can be changed using the -c or --alias_cost param).

Summary will then be printed with most costly commands listed at the bottom.
