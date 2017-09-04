var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');

var app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/rabbits');

var MongooseSchema = new mongoose.Schema({
    name: {type: String, required: true},
    age: {type: Number, required: true},
    description: {type: String, required: true}
}, {timestamps: true});
mongoose.model('Mongoose', MongooseSchema);
var Mongoose = mongoose.model('Mongoose');

// Displays all mongooses
app.get('/', function(req, res) {
    Mongoose.find({}, function(err, mongeese) {
        res.render('index', {mongeese: mongeese})
    })
})

// Takes to page with form to add new mongoose
app.get('/mongooses/new', function(req, res) {
    res.render('new');
})

// Displays info on one specific mongoose
app.get('/mongooses/:id', function(req, res) {
    Mongoose.find({_id: req.params.id}, function(err, mongeese) {
        console.log(mongeese);
        res.render('info', {mongeese: mongeese})
    })
})

app.post('/mongooses', function(req, res) {
    console.log("POST DATA", req.body);
    var mongoose = new Mongoose({name: req.body.name, age: req.body.age, description: req.body.description});
    mongoose.save(function(err) {
        if(err) {
            console.log('Oops! Something went wrong');
            res.render('new', {errors: mongeese.errors})
        }
        else {
            console.log('Succesfully adopted a mongoose!')
            res.redirect('/');
        }
    })
})

app.get('/mongooses/edit/:id', function(req, res) {
    Mongoose.find({_id: req.params.id}, function(err, mongeese) {
        if(err) {
            console.log('Oops! Something went wrong');
        }
        else {
            console.log(mongeese);
            res.render('edit', {mongeese : mongeese});
        }
    })
})

app.get('/mongooses/destroy/:id', function(req, res) {
    Mongoose.remove({_id: req.params.id}, function(err) {
        if(err) {
            console.log('Oops! Something went wrong');
        }
        else {
            console.log('Mongoose successfully deleted!');
            res.redirect('/');
        }
    })
})

app.post('/mongooses/:id', function(req, res) {
    console.log("POST DATA", req.body);
    Mongoose.update({_id: req.params.id}, {name: req.body.name, age: req.body.age, description: req.body.description}, function(err, result) {
        if(err) {
            console.log('Oops! Something went wrong');
            res.render('edit', {errors: mongoose.errors});
        }
        else {
            console.log('Update was succesful!');
            res.redirect('/');
        }
    })
})

app.listen(8000, function() {
    console.log("listening on port 8000");
})
