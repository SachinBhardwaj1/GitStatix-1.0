import { useEffect, useState } from "react";
import axios from "axios";

const MergeConflictTable = () => {
    const [conflicts, setConflicts] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/conflicts").then((res) => setConflicts(res.data));
    }, []);

    return (
        <div className="w-full p-5">
            <h2 className="text-xl font-bold">Merge Conflicts</h2>
            <table className="min-w-full border-collapse border border-gray-300">
                <thead>
                    <tr>
                        <th className="border border-gray-300 px-4 py-2">Repository</th>
                        <th className="border border-gray-300 px-4 py-2">Merge Conflict</th>
                    </tr>
                </thead>
                <tbody>
                    {conflicts.map((conflict, index) => (
                        <tr key={index}>
                            <td className="border border-gray-300 px-4 py-2">{conflict.repo}</td>
                            <td className="border border-gray-300 px-4 py-2">{conflict.message}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default MergeConflictTable;
