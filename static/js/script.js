function clicc(btn, val, id) {
    var xhr = new XMLHttpRequest();
    rv = 0;
    if (btn.style.color == "black") {
        btn.style.color = "red";
        rv = val;
    } else {
        btn.style.color = "black";
        rv = -val;
    };
    rates = document.getElementsByClassName("j_rating");
    r_id = 0
    for (let item of rates){
        if (item.id == -id){
              item.innerHTML = Number(item.innerHTML) + Number(rv);
            };
    };

    var json = id + ' ' + rv;

    xhr.open("POST", "/blog/vote.py", true);
    xhr.setRequestHeader("Content-type", 'application/x-www-form-urlencoded');
    xhr.send(json);

    xhr.onreadystatechange = function(){
        json = xhr.response;
        console.log(json);
    };

    xhr.onload = function() {
        x = `${xhr.status} ${xhr.response}`;
        console.log(`Загружено: ${xhr.status} ${xhr.response}`);
    };

    xhr.onerror = function() {
        alert(`Ошибка соединения`);
    };

    xhr.onprogress = function(event) {
        console.log(`Загружено ${event.loaded} из ${event.total}`);
    };

    return 0;
};