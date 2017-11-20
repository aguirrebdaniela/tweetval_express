const Tweets = require('../models/twitter');
const SentimentalAnalysis = require("../models/sentiment");

router = require('express').Router(),
Auth = require('../services/auth');

require("jsdom/lib/old-api").env("", function(err, window) {
    if (err) {
        console.error(err);
        return;
    }
    var $ = require("jquery")(window);
    router.get('/:text', (req, res)=>{
        var textToSearch = req.params.text;
        console.log(textToSearch);
        Tweets.searchTweets(textToSearch, 20, $).done(function (resultTweets) { 
            var deferredArray = new Array();
            var resultTweetsAndAnalysis = new Array();
            $(resultTweets).each(function () {  
                console.log(this)
                deferredArray.push(SentimentalAnalysis.runAnalysis(this, resultTweetsAndAnalysis, $));
            });
            $.when.apply($, deferredArray).then( function () { 
                res.json(resultTweetsAndAnalysis);
            });
            
        });
    })
});


module.exports = router;