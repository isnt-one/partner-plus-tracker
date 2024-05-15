# A Twitch Partner Plus goal tracker
To use this script, you will need to have your Plus Goals widget shared in your panels. The script will update every 10 minutes.

Setup instructions:
- Modify `CHANNEL` variable in `.env` with your Twitch username
- Run the below commands in command prompt
```
pip install -r requirements.txt
playwright install chromium
python app.py
```
- Add a `Text (GDI+)` source and select the `goal.txt` file from the trackers directory
