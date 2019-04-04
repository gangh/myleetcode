
date
cd /home/gang/mygithub/myleetcode/
git pull
python leetcode_generate.py
git add .
git commit -m "auto refresh leetcode"
git push
echo "push success"
hub pull-request -m "auto pr for refresh solutions from vps "
echo "pr success"
git pull
