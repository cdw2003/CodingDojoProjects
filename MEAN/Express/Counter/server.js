var express = require ("express");
var bodyParser = require ("body-parser");
var session = require("express-session");
var app = express();

app.use(bodyParser.urlencoded({extended: true}));
app.set('views',__dirname + '/views');
app.set('view engine', 'ejs');
app.use(session({secret:'secretkey'}));

app.get('/', function(req, res){
    if(req.session.count == null || req.session.count == undefined){
        req.session.count = 0;
    } else{
        req.session.count++;
    }
    res.render("index", {count: req.session.count});
})

app.get('/counttwo',function(req,res){
    req.session.count +=1;

    res.redirect("/");
})

app.get('/reset',function(req,res){
    req.session.destroy();
    res.redirect("/");
})

app.listen(8000, function(){
    console.log("listening on port 8000");
})
