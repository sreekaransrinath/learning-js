// Setup
var contacts = [
    {
        "firstName": "Akira",
        "lastName": "Laine",
        "number": "0543236543",
        "likes": ["Pizza", "Coding", "Brownie Points"]
    },
    {
        "firstName": "Harry",
        "lastName": "Potter",
        "number": "0994372684",
        "likes": ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "0487345643",
        "likes": ["Intriguing Cases", "Violin"]
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["JavaScript", "Gaming", "Foxes"]
    }
];


function lookUpProfile(name, prop){
// Only change code below this line
    var nameFlag = 0;
    var propFlag = 0;
    var i = 0;
    while (i < contacts.length) {
        if (contacts[i]['firstName'] == name) {
            nameFlag = 1;
            if (contacts[i].hasOwnProperty(prop)) {
                propFlag = 1;
                console.log(contacts[i][prop]);
                return contacts[i][prop];
            }
        }

        i++;
    }
    if (propFlag == 0 && nameFlag == 1) {
        return "No such property";
    }

    else if (nameFlag == 0) {
        return "No such contact";
    }

    }
// Only change code above this line


lookUpProfile("Akira", "likes");
