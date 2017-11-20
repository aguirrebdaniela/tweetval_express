const language = require('@google-cloud/language');
const client = new language.LanguageServiceClient();

module.exports = {
        runAnalysis : function (tweet, resultListAnalysis, $) {  
            try {
                var deferred = $.Deferred();
                var document = {
                    content: tweet.text,
                    language: 'en',
                    type: 'PLAIN_TEXT',
                };
                client.analyzeSentiment({document: document})
                .then(results => {
                    var twitterResult = null;
                    for (var index = 0; index < results.length; index++) {
                        var sentiment = results[index].documentSentiment;
                        twitterResult = {
                            id: tweet.id,
                            text: tweet.text,
                            score: sentiment.score,
                            magnitude: sentiment.magnitude,
                            level: this.defineLevel(sentiment.score, sentiment.magnitude)
                        };
                    }
                    resultListAnalysis.push(twitterResult);
                    deferred.resolve();
                })
                .catch(err => {
                    console.log(err)
                    deferred.reject(err);
                });
                return deferred.promise();
            } catch (error) {
                console.log(error)
            }
        },

        defineLevel: function (score, magnitude) { 
            var result = "";
            if(score > 0.3)
                result = "Positive";
            else if(score <= 0.3 && score >= -0.3)
                result = "Neutral";
            else 
                result = "Negative";
            return result;
        }
    } 

// module.exports = Sentiment;