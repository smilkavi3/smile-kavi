const doc = document

function getTasks(url) {
    return fetch(url, {
        method: "GET"
    }).then((res) => res.json())
}
async function getpending() {
    const data = await getTasks("http://127.0.0.1:8000/getTask?status=pending")

    //console.log(data) see the collection of data
    display(data)

}

//get complete datas:

async function getComplete() {
    const data = await getTasks("http://127.0.0.1:8000/getTask?status=complet")

    //console.log(data) see the collection of data
    display(data)

}


// task add to mongo db:

//display the data:


function display(collection) {
    const divList = doc.getElementById("but")
    divList.innerHTML = "";
    collection.student.forEach((element, index) => {
        const text = `
                <div class="one">
                    <div class="inside" id="content">
                        <li>Name: ${element.name}</li>
                        <li>Person_id: ${element._id}</li>
                        <li>Status: ${element.status}</li>
                    </div>
                    <div class="two">
                        <button id="edit" onclick="editTask(${index})">Edit</button>
                        <button id="delet" onclick="deleteTask(${index})">Delete</button>
                        <button id="save" onclick="saveTask(${index})">Save</button>
                    </div>
                </div>`;
        divList.innerHTML += text;
    })
}

