// for navigator language
var lang = window.navigator.language;
// you can change the language
// var lang = 'en';

//change weather params here:
//units: metric or imperial
var weatherParams = {
    'q':'Kfar Saba,Israel',
    'units':'metric',
    'lang':lang
};

var feed = 'http://www.ynet.co.il/Integration/StoryRss1854.xml';
//var feed = 'http://www.nu.nl/feeds/rss/achterklap.rss';
//var feed = 'http://www.nu.nl/feeds/rss/opmerkelijk.rss';
//var feed = 'http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml';


//Recognized person welcome
var iAm = ['Hi Omer','Hi Tzahit!'];
// compliments:
var morning = [
            'Good morning, handsome!',
            'Enjoy your day!',
            'How was your sleep?'
        ];
        
var afternoon = [
            'Hello, beauty!',
            'You look sexy!',
            'Looking good today!'
        ];
       
var evening = [
            'Wow, you look hot!',
            'You look nice!',
            'Hi, sexy!'
        ];