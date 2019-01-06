TagproAuction
=============

Tagpro Auction tool for MLTP.

To run this project on a server, run these commands:

```
curl https://install.meteor.com/ | sh

meteor --allow-superuser -p 80
```

My deployment recommendation is to create a new droplet on DigitalOcean, ssh into it, clone the repo, then run the above commands inside the repo.

## Auction Setup

1. Modify `genner.py` to include the team information for the draft.
2. Run `python genner.py` and it will update the correct files.
3. Edit the first line in `auction.js` to include the list of admins - people who can start/pause/undo bids on the auction.
4. Update `player_response.json` with names of the players who are eligible for the draft. The easiest way to do this is copy all of the names from a spreadsheet, paste, then use find & replace with Regex to turn it into a valid JSON array.

    Find: `$1`

    Replace: `    {\n        "tagpro": "$1"\n    },`

    Remove the last comma and put brackets on either end to make it an array.

## Live Editing

Sometimes, you may need to pause the auction and live edit the data in mongo. Ex) A trade or Ball God >:/

Edit in CLT:

```
meteor mongo --allow-superuser
```

Connect remotely with GUI (a lot easier):

```
1. I recommend installing the free version of Robo 3T
2. Create a connection with SSH tunneling using your SSH credentials.
3. Under the connection tab, use 127.0.0.1 for the IP and 81 for the port.
```

### Database Tips

Each document in `teams` relates one player to a team name, so each team will have X number of documents corresponding to their team, where X is the number of roster spots shown in the draft (so 4-5 usually).

A teams current amount of money is stored in `teamnames`.

To exact trades, you should update `teams` to reflect the roster moves & new player cost and `teamnames` to update team money if needed.

## Other Notes

Captain names are case sensitive - when signing up you need to use the correct capitalization.