function isArray(myArray) {
  return myArray.constructor === Array;
}

function register()
{
    const inpt = document.getElementById('inp2');
    var entry = { bs_name: inpt.value };
    fetch(`${window.origin}/api/Clients`, {
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify(entry),
        cache: 'no-cache',
        headers: new Headers({'content-type':'application/json'}),
    })
        .then(function (response) {
            if (response.status != 200) {
                console.log(`response status was not 200, was ${response.status}`);
                return;
            }
            response.json().then(function (data) {
                let str = "ADDED\tID:" + data.id + "\tBS:" + data.bs_name;
                printf(str);
            })
    })
}

function send_request()
{
    const inpt = document.getElementById('inp1');
    var entry = { id: inpt.value };
    fetch(`${window.origin}/api/Clients/${entry.id}`, {
        method: 'GET',
        credentials: 'include',
        cache: 'no-cache',
        headers: new Headers({'content-type':'application/json'}),
    })
    .then(function (response) {
            if (response.status != 200) {
                console.log(`response status was not 200, was ${response.status}`);
                return;
            }
        response.json().then(function (data) {
            if (isArray(data)){
                data.forEach(element => {
                    let str = "RETRIEVED\tID:" + element.id + "\tBS:" + element.bs_name;
                    printf(str);
                });
                return;
            }
                let str = "RETRIEVED\tID:" + data.id + "\tBS:" + data.bs_name;
                printf(str);
            })
    })
}

function edit()
{
    const ide = document.getElementById('ide');
    const bsne = document.getElementById('bse');
    var entry = { id: ide.value, bs_name: bsne.value };
    fetch(`${window.origin}/api/Clients`, {
        method: 'PUT',
        credentials: 'include',
        body: JSON.stringify(entry),
        cache: 'no-cache',
        headers: new Headers({'content-type':'application/json'}),
    })
        .then(function (response) {
            if (response.status != 200) {
                console.log(`response status was not 200, was ${response.status}`);
                return;
            }
            response.json().then(function (data) {
                let str = "MODIFIED\tID:" + data.id + "\tBS:" + data.bs_name;
                printf(str);
            })
    })
}

function deleteO()
{
    const idd = document.getElementById('idd');
    const bsnd = document.getElementById('bsd');
    var entry = { id: idd.value };
    fetch(`${window.origin}/api/Clients`, {
        method: 'DELETE',
        credentials: 'include',
        body: JSON.stringify(entry),
        cache: 'no-cache',
        headers: new Headers({'content-type':'application/json'}),
    })
        .then(function (response) {
            if (response.status != 200) {
                console.log(`response status was not 200, was ${response.status}`);
                return;
            }
            response.json().then(function (data) {
                let str = "DELETED\tID:" + data.id + "\tBS:" + data.bs_name;
                printf(str);
            })
    })
}

function printf(str) {
    const outcon = document.getElementById("console");
    let d = new Date();
    outcon.value += '\n' + d.toLocaleString() + '\t' + str;
}