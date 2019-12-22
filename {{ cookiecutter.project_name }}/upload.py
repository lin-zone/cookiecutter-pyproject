import subprocess


subprocess.run('git init')
subprocess.run('git add -u')
subprocess.run('git reset -- upload.py')
subprocess.run('git commit -m "first commit"')
subprocess.run('git remote add origin git@github.com:{{ cookiecutter.author_name }}/{{ cookiecutter.project_name }}')
subprocess.run('git push -u origin master')