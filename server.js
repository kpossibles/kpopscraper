const express = require('express');
const people = require('./kpop-profiles.json');
const groups = require('./kpop-groups.json');

const app = express();

app.set('view engine', 'pug');

app.use(express.static(__dirname + '/public'));

app.get('/', (req, res) => {
    res.render('index', {
        title: 'Kpop Stars - Profiles',
        people: people
    });
});

app.get('/profile', (req, res) => {
    if(req.query.name){
        var person = people.find(function (p) {
            let gp = p.group.split(", ");
            var match="";
            gp.forEach(e => {
                if (e == req.query.group) {
                    match = e;
                }
            });
            return p.stage_name == req.query.name && match!="";
        });
    }
    else
        var person = people.find(p => p.id === req.query.id);
    // console.log("ID: "+person.id);
    res.render('profile', {
        title: `About ${person.stage_name} | ${person.real_name}`,
        person,
    });
});

app.get('/profile-group', (req, res) => {
    if (req.query.name) {
        var group = groups.find(p => p.name == req.query.name);
    } else
        var group = groups.find(p => p.id == req.query.id);
    // console.log(group)
    res.render('profile-group', {
        title: `About ${group.name}`,
        group, people: people
    });
});

app.get('/idols', (req, res) => {
    res.render('idols', {
        title: 'Kpop Stars - Idols',
        people: people
    });
});

app.get('/random', (req, res) => {
    if (Math.floor(Math.random() * 10) < 5) {
        let rand = Math.floor(Math.random() * people.length);
        var person = people.find(p => p.id == rand);
        res.render('profile', {
            title: `About ${person.stage_name} | ${person.real_name}`,
            person,
        });
    } else {
        let rand = Math.floor(Math.random() * groups.length);
        var group = groups.find(p => p.id == rand);
        res.render('profile-group', {
            title: `About ${group.name}`,
            group,
        });
    }
});

app.get('/groups', (req, res) => {
    res.render('groups', {
        title: 'Kpop Stars - Groups',
        groups: groups
    });
});

const server = app.listen(5000, () => {
    console.log(`Express running → PORT ${server.address().port}`);
});