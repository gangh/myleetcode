git pull
python leetcode_generate.py
git add .
git commit -m "auto refresh leetcode"
git push
hub pull-request -m "auto pr for refresh leetcode pull request from vps "
git checkout master
git checkout -b "new-branch-refresh-leetcode"
git pull
