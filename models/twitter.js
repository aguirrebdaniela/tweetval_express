var Twit  = require("twit");

module.exports =  {  

    searchTweets : function (text, limit, $) {  
        var deferred = $.Deferred();
        var T = new Twit( {
                            consumer_key:         'JbdqDq8fm0oG0jfDS30vV1JgK',
                            consumer_secret:      'IJsNQzTcQ3ypEPZD5Sql9aU3rlqzzLHPpG1k2WC13lNSWloFpg',
                            access_token:         '63858128-DJ4eqKLN519lnO0sPnoAcZ50c49bfxAHeIwUkTjyS',
                            access_token_secret:  'ixxOUJavuywLhOR02SPSxAgjsaV95wC01NGiHBIVyOiJI',
                            timeout_ms:           60*1000,  // optional HTTP request timeout to apply to all requests.
                        });
        T.get('search/tweets',
            {
                q: text,
                lang: 'en', 
                count: limit
            },
            function (err, data, response) {
                if(!err) {
                    var resultTweets = new Array();
                    var tweets = data.statuses;
                    $(tweets).each(function () {
                        var filteredTweet = {
                            text: this.text,
                            id: this.id
                        };                        
                        resultTweets.push(filteredTweet);
                     });
                     deferred.resolve(resultTweets);
                } else
                    deferred.reject(err);
            }
        );
        return deferred.promise();
    }

}

// module.exports = Twitter;