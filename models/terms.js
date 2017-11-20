const db = require('../db/config');
const pgp = require('pg-promise');
const bodyParser = require('body-parser');
 
const terms = {};
 
terms.findByUser = (req, res, next) => {
 	db.many('SELECT * FROM terms WHERE user_id=$1', [req.params.userid])
 	.then((terms) => {
 		res.locals.terms = terms;
 		next();
 	})
 	.catch(err => {
 		console.log('error fetching data from database' + err);
 	});
};

terms.findByWord = (req, res, next) => {
    db.many('SELECT * FROM terms WHERE LOWER(word) LIKE LOWER($1)', [req.params.word])
    .then((terms) => {
        res.locals.terms = terms;
        next();
    })
    .catch(err => {
        console.log('error fetching data from database' + err);
    });
};

 
terms.findById = (req, res, next) => {
 	db.oneOrNone('SELECT * FROM terms WHERE ID = $1', [req.params.id])
 	.then((term) => {
 		res.locals.term = term;
 		next();
 	})
 	.catch(err=> {
 		console.log('error fetching from database' + err);
 		res.status(404);
 	})
};
 
terms.create = (req, res, next) => {
    const {word, search_date, user_id} = req.body;
    console.log(req.body)
    db.one(`INSERT INTO terms (word, search_date, user_id) 
		VALUES ($1, $2, $3) RETURNING *`, [word, search_date, user_id])
        .then((term) => {
            res.locals.newTerm = term;
            next();
        })
        .catch(err => {
            console.log('error fetching from database');
        })
};
 
terms.delete = (req, res, next) => {
 	db.oneOrNone('DELETE FROM terms WHERE ID = $1', [req.params.id])
 	.then((term) => {
 		res.locals.term = term;
 		next();
 	})
 	.catch(err=> {
 		console.log('error fetching from database' + err);
 		res.status(404);
 	})
};


 
 
module.exports = terms; 
