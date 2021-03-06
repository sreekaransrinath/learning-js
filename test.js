// Setup
var contacts = [{
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


function lookUpProfile(name, prop) {
    // Only change code below this line
    var nameFlag = 0;
    var propFlag = 0;
    for (var i = 0; i < contacts.length; i++) {
        if (contacts[i]['firstName'] == name) {
            nameFlag = 1;
            if (contacts[i].hasOwnProperty(prop)) {
                propFlag = 1;
                console.log(contacts[i][prop]);
                return contacts[i][prop];
            }
        }

        if (propFlag == 0 && nameFlag == 1) {
            console.log('NSP');
            return "No such property";

        } else if (nameFlag == 0) {
            console.log('NSC');
            return "No such contact";
        }

    }
    // Only change code above this line
}

lookUpProfile("Harry", "likes");