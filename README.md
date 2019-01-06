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

## Other Notes

Captain names are case sensitive - when signing up you need to use the correct capitalization.