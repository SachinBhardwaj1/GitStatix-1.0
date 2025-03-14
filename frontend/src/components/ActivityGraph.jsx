import { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import axios from "axios";
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const API_BASE = "http://127.0.0.1:8000";

const ActivityGraph = () => {
    const [activity, setActivity] = useState({});
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get(`${API_BASE}/activity`)
            .then((res) => setActivity(res.data))
            .catch((err) => {
                console.error("API error:", err);
                setError("Failed to fetch data.");
            });
    }, []);

    if (error) return <p className="text-red-500">{error}</p>;

    const data = {
        labels: Object.keys(activity),
        datasets: [
            {
                label: "GitHub Activity",
                data: Object.values(activity),
                backgroundColor: ["#36a2eb", "#ff6384", "#ffcd56", "#4caf50"],
            },
        ],
    };

    return (
        <div className="w-full p-5">
            <h2 className="text-xl font-bold text-center">GitHub Activity Overview</h2>
            <Bar data={data} />
        </div>
    );
};

export default ActivityGraph;
