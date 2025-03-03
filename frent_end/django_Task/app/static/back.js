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



    console.log(data) //see the collection of data
    display(data)

}


// fetch task: simple method
// async function getTaskAPI(url, ...object) {
//     return await fetch(url, ...object).then((res)=>res.json())
// }

async function getTaskAPI(url, ...object) {
    const res = await fetch(url, ...object)
    const data = await res.json()
    return data
}


// task Edit btn activate:

async function editTask(id) {

    const data = await getTaskAPI("http://127.0.0.1:8000/getSpecificData", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "id": id
        })
    })
    
    
     savefunction(data,id)


    // console.log(data,"return datas")//retuen datas from getspecific data:


}

async function savefunction(data, id) {
    const saveTask = doc.getElementById("Taskbtn")
    saveTask.textContent= "Save_Task"
    const retnTask = data.datas
    console.log(retnTask.status);
    if (retnTask.status === "complet" || retnTask.status === "pending") {
        const input = doc.getElementById("input").value = retnTask.name
        const options = doc.getElementById("input-status").value = retnTask.status
        
        const update_task = {
            "id": id,
            "name": input,
            "status": options
        }
        
        const update_data = await getTaskAPI("http://127.0.0.1:8000/getUpdateData", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(update_task)
        })
        
        
        
        console.log(update_data)
    } else {
        return ("Not in status")
    }
}

// const saveTask = doc.getElementById("Taskbtn");
const saveTask = doc.getElementById("Taskbtn")
saveTask.addEventListener("click",function () {
    saveTask.textContent="Add_Task"
});


//display the data:


function display(collection) {
    const divList = doc.getElementById("block")
    divList.innerHTML = "";
    collection.student.forEach((element, index) => {
        // const id=String(element.id)
        const text = `
                <div class="one">
                    <div class="inside" id="content">
                        <li>Person_id: ${element._id}</li>
                        <li>Name: ${element.name}</li>
                        <li>Status: ${element.status}</li>
                    </div>
                    <div class="two">
                        <button id="edit" onclick="editTask('${element._id}')">Edit</button>
                        <button id="delet" onclick="deleteTask(${index})">Delete</button>
                        <button id="save" onclick="saveTask(${index})">Save</button>
                    </div>
                </div>`;
        divList.innerHTML += text;
    })
}

