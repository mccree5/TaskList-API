import React from "react";
import { useState } from "react";
import { useEffect } from "react";
import { deleteTasks, getTasks } from "../services/api";
import { addTasks } from "../services/api";
import { deleteTasks } from "../services/api";

const [tasks, setTasks] = useState([]);

export const fetchTasks = async () => {
    try {
        const fetchedTasks = await getTasks();
        setTasks(fetchedTasks);
    } catch (error) {
        console.log("Task could not be retrieved: "+ error);
    }
}