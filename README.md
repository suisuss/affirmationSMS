
### affirmationSMS

#### Setup

- Create `/usr/local/cronjob` and give appropriate permissions. This is where the repo will be held.
- `mkdir /usr/local/cronjob && chmod 777 /usr/local/cronjob`
- Clone repo in `/usr/local/cronjob`
  - `cd /usr/local/cronjob && git clone git@github.com:suisuss/affirmationSMS.git && cd affirmationSMS`
- Setup venv
  - `python3 -m venv venv`
  - `source venv/bin/activate` 
  - `pip install -r requirements.txt`
  - `deactivate`
- Create `.env`. Example is in the repo
- Setup cronjob
  - `crontab -e`
    - Add `0 12 * * * /usr/local/cronjob/affirmationSMS/affirmationSMS.sh`
