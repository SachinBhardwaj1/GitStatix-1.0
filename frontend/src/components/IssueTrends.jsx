import { useEffect, useState } from "react";
import { fetchTrends } from "../api";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const IssueTrends = () => {
    const [trendData, setTrendData] = useState([]);

    useEffect(() => {
        fetchTrends().then(data => setTrendData(data));
    }, []);

    return (
        <div>
            <h2>Issue Trends Over Time</h2>
            <ResponsiveContainer width="100%" height={300}>
                <LineChart data={trendData}>
                    <XAxis dataKey="created_at" />
                    <YAxis />
                    <Tooltip />
                    <Line type="monotone" dataKey="issue_count" stroke="#8884d8" />
                </LineChart>
            </ResponsiveContainer>
        </div>
    );
};

export default IssueTrends;
