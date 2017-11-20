const db = require('../db/config');
const pgp = require('pg-promise');
const bodyParser = require('body-parser');
 
const results = {};
 
 
results.findById = (req, res, next) => {
 	db.manyOrNone('SELECT * FROM results WHERE id_terms = $1', [req.params.id])
 	.then((result) => {
 		res.locals.result = result;
 		next();
 	})
 	.catch(err=> {
 		console.log('error fetching from database' + err);
 		res.status(404);
 	})
};
 
results.create = (req, res, next) => {
    const {tweet_text, score, magnitude, evaluation, id_terms} = req.body;
    console.log(req.body)
    db.one(`INSERT INTO results (tweet_text, score, magnitude, evaluation, id_terms) 
		VALUES ($1, $2, $3, $4, $5) RETURNING *`, [tweet_text, score, magnitude, evaluation, id_terms])
        .then((result) => {
            res.locals.newResult = result;
            next();
        })
        .catch(err => {
            console.log('error fetching from database');
        })
};
 
results.delete = (req, res, next) => {
 	db.oneOrNone('DELETE FROM results WHERE id_terms = $1', [req.params.id])
 	.then((result) => {
 		res.locals.result = result;
 		next();
 	})
 	.catch(err=> {
 		console.log('error fetching from database' + err);
 		res.status(404);
 	})
};
 
 
module.exports = results; 
