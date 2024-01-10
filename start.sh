python3 /home/nsakkriou/github-profile-update/nSakkriou/main.py >> /cron.log
git -C /home/nsakkriou/github-profile-update/nSakkriou/ add . >> /cron.log
git -C /home/nsakkriou/github-profile-update/nSakkriou/ commit -m "update" >> /cron.log
git -C /home/nsakkriou/github-profile-update/nSakkriou/ push origin main >> /cron.log
