const url ='http://localhost:8080/to-do-list';

export const getTasks = async () => {
    try {
        const response = await fetch(url + "/allTasks");
    if (response.ok){
        const jsonResponse = await response.json();
        return jsonResponse;
    }

    } catch (error) {
        console.log(error);
    }
    }

    export const addTasks = async (newTask) => {
        try {
            const response = await fetch(url + "/addTasks", {
                method: 'POST',
                headers:  {
                    'Content-Type': 'application/json',
                  },
                body: JSON.stringfy(newTask)
            });
            if (response.ok){
                const jsonResponse = await response.json();
                return jsonResponse;

            }
        } catch (error) {
            console.log(error);
        }
    }

    export const updateTasks = async (newTask) => {
        try {
            const response = await fetch(url + "/addTasks", {
                method: 'PUT',
                headers:  {
                    'Content-Type': 'application/json',
                  },
                body: JSON.stringfy(newTask)
            });
            if (response.ok){
                const jsonResponse = await response.json();
                return jsonResponse;
            }
        } catch (error) {
            console.log(error);
        }
    }
    export const deleteTasks = async (taskId) => {
        try {
            const response = await fetch(`${url}/${taskId}`, {
                method: 'DELETE'
            });
            if (response.ok){
                const jsonResponse = await response.json();
            }
        } catch (error) {
            console.log(error);
        }
    }