var playerSignUps = require("./eltps5signups.json");

var playerResponses = playerSignUps.map( function (p) {
    return {
        tagpro: p[0],
        reddit: p[1],
        position: p[7],
        mic: p[8],
        co_captain: p[10],
        location: p[9],
        link: p[6],
        availability_comment: p[12],
        player_comment: p[13],
        draft_comment: p[14]
    };
});

console.log(JSON.stringify(playerResponses));