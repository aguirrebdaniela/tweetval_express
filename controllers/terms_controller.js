const router = require('express').Router();
const Terms = require('../models/terms.js');
const Results = require('../models/results.js');
 
 
 router.get('/username/:userid', Terms.findByUser, (req, res, next) => {
 	res.json({
 		terms: res.locals.terms
 	});	
 });
 
 router.get('/:id', Terms.findById, (req, res, next) => {
 	res.json({
 		term: res.locals.term
 	});	
 });
 
 
router.post('/', Terms.create, (req, res) => {
    res.json({
    	term: res.locals.newTerm
	});
 });


 router.delete('/:id', Terms.delete, (req, res, next) => {
 	res.json({
 		message: 'Deleted term!'
 	});	
 });


router.post('/results', Results.create, (req, res) => {
    res.json({
    	result: res.locals.newResult
	});
 });

 router.get('/results/:id', Results.findById, (req, res, next) => {
 	res.json({
 		result: res.locals.result
 	});	
 });

  router.delete('/results/:id', Results.delete, (req, res, next) => {
 	res.json({
 		message: 'Deleted result!'
 	});	
 });

   router.get('/word/:word', Terms.findByWord, (req, res, next) => {
	res.json({
		terms: res.locals.terms
	})
	});	


 
 module.exports = router; 