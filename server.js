const express = require('express');
const people = require('./kpop-profiles.json');

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
    const person = people.find(p => p.id === req.query.id);
    res.render('profile', {
        title: `About ${person.stage_name} | ${person.real_name}`,
        person,
    });
});

const server = app.listen(7000, () => {
    console.log(`Express running → PORT ${server.address().port}`);
});