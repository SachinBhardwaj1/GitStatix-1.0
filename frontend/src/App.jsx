import ActivityGraph from "./components/ActivityGraph";
import MergeConflictTable from "./components/MergeConflictTable";

function App() {
    return (
        <div className="min-h-screen bg-gray-100 p-5">
            <h1 className="text-2xl font-bold text-center">GitHub Insights Dashboard</h1>
            <ActivityGraph />
            <MergeConflictTable />
        </div>
    );
}

export default App;
